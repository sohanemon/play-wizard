#!/usr/bin/env python3

import dbus
import sys
import os
from dbus.mainloop.glib import DBusGMainLoop

directory = '/tmp/omniPause'
players   = []
DBusGMainLoop(set_as_default=True)
bus       = dbus.SessionBus()

def do_nothing(*args, **kwargs):
    pass

def get_version(pkgbuild_path="PKGBUILD"):
    version = "1.0.4"
    return version

def get_player_name(i, player):
    if i.startswith("org.mpris.MediaPlayer2."):
        return i[len("org.mpris.MediaPlayer2."):]
    else:
        return player.Get('org.mpris.MediaPlayer2','DesktopEntry', dbus_interface='org.freedesktop.DBus.Properties')

def pause():
    player_names = []
    for i in players:
        player = bus.get_object(i, '/org/mpris/MediaPlayer2')
        player_status = player.Get('org.mpris.MediaPlayer2.Player','PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
        if player_status == 'Playing':
            player_name = get_player_name(i, player)
            player_names.append(player_name)
            player.Pause(dbus_interface='org.mpris.MediaPlayer2.Player', reply_handler=do_nothing, error_handler=do_nothing)

    if player_names != []:
        for i in os.listdir(directory+'/paused-players/'):
            os.remove(directory+'/paused-players/'+i)
        for player_name in player_names:
            player_status_file = open(directory+'/paused-players/'+player_name, "w")
            player_status_file.close()

def play():
    for i in os.listdir(directory+'/paused-players/'):
        try:
            player = bus.get_object('org.mpris.MediaPlayer2.'+i, '/org/mpris/MediaPlayer2')
        except:
            if i in os.listdir(directory+'/paused-players'):
                os.remove(directory+'/paused-players/'+i)
            continue
        player_status = player.Get('org.mpris.MediaPlayer2.Player','PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
        if player_status == 'Paused':
            player.Play(dbus_interface='org.mpris.MediaPlayer2.Player', reply_handler=do_nothing, error_handler=do_nothing)
            if i in os.listdir(directory+'/paused-players'):
                os.remove(directory+'/paused-players/'+i)
        
def stop():
    for i in players:
        player = bus.get_object(i, '/org/mpris/MediaPlayer2')
        player_status = player.Get('org.mpris.MediaPlayer2.Player','PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
        if player_status == 'Playing' or player_status == 'Stopped':
            player.Stop(dbus_interface='org.mpris.MediaPlayer2.Player', reply_handler=do_nothing, error_handler=do_nothing)

def toggle():
    playing = False
    for i in players:
        player = bus.get_object(i, '/org/mpris/MediaPlayer2')
        player_status = player.Get('org.mpris.MediaPlayer2.Player','PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
        if player_status == 'Playing':
            playing = True
    if playing:
        pause()
    else:
        play()

def next():
    for i in players:
        player = bus.get_object(i, '/org/mpris/MediaPlayer2')
        player_status = player.Get('org.mpris.MediaPlayer2.Player','PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
        if player_status == 'Playing':
            player.Next(dbus_interface='org.mpris.MediaPlayer2.Player', reply_handler=do_nothing, error_handler=do_nothing)

def previous():
    for i in players:
        player = bus.get_object(i, '/org/mpris/MediaPlayer2')
        player_status = player.Get('org.mpris.MediaPlayer2.Player','PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
        if player_status == 'Playing':
            player.Previous(dbus_interface='org.mpris.MediaPlayer2.Player', reply_handler=do_nothing, error_handler=do_nothing)

def seek(offset):
    try:
        # Convert offset to microseconds (MPRIS uses microseconds)
        offset = int(offset) * 1000000
    except ValueError:
        print("Error: Offset must be an integer representing seconds (e.g., +10, -10, -30).")
        return

    for i in players:
        player = bus.get_object(i, '/org/mpris/MediaPlayer2')
        player_status = player.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
        if player_status in ['Playing', 'Paused']:
            try:
                # Perform the seek operation
                player.Seek(offset, dbus_interface='org.mpris.MediaPlayer2.Player', reply_handler=do_nothing, error_handler=do_nothing)
            except dbus.exceptions.DBusException as e:
                print(f"Error seeking player {i}: {e}")


def set_speed(speed):
    try:
        # Check if the input is relative (starts with '+' or '-')
        if speed.startswith(('+', '-')):
            relative = True
            delta = float(speed)  # Convert relative change to float
        else:
            relative = False
            new_speed = float(speed)  # Convert absolute speed to float
    except ValueError:
        print("Error: Speed must be a numeric value (e.g., 1.0, 0.5, 2.0, +0.1, -0.1).")
        return

    initial_speeds = {}
    if relative:
        # Store initial speeds for each player
        for i in players:
            player = bus.get_object(i, '/org/mpris/MediaPlayer2')
            player_status = player.Get(
                'org.mpris.MediaPlayer2.Player',
                'PlaybackStatus',
                dbus_interface='org.freedesktop.DBus.Properties'
            )

            if player_status in ['Playing', 'Paused']:
                current_speed = player.Get(
                    'org.mpris.MediaPlayer2.Player',
                    'Rate',
                    dbus_interface='org.freedesktop.DBus.Properties'
                )
                initial_speeds[i] = current_speed

        # Apply relative adjustment based on initial speeds
        for i, initial_speed in initial_speeds.items():
            new_speed = round(initial_speed + delta, 2)

            # Ensure the speed is positive
            if new_speed <= 0:
                print(f"Error: Resulting speed {new_speed} is invalid. Speed must be greater than 0.")
                continue

            player = bus.get_object(i, '/org/mpris/MediaPlayer2')
            player.Set(
                'org.mpris.MediaPlayer2.Player',
                'Rate',
                dbus.Double(new_speed),
                dbus_interface='org.freedesktop.DBus.Properties'
            )
            print(f"Set speed to {new_speed} for player {i}.")
    else:
        # Set absolute speed
        for i in players:
            player = bus.get_object(i, '/org/mpris/MediaPlayer2')
            player_status = player.Get(
                'org.mpris.MediaPlayer2.Player',
                'PlaybackStatus',
                dbus_interface='org.freedesktop.DBus.Properties'
            )

            if player_status in ['Playing', 'Paused']:
                try:
                    # Set the absolute new speed
                    new_speed = round(new_speed, 2)

                    # Ensure the speed is positive
                    if new_speed <= 0:
                        print(f"Error: Resulting speed {new_speed} is invalid. Speed must be greater than 0.")
                        continue

                    player.Set(
                        'org.mpris.MediaPlayer2.Player',
                        'Rate',
                        dbus.Double(new_speed),
                        dbus_interface='org.freedesktop.DBus.Properties'
                    )
                    print(f"Set speed to {new_speed} for player {i}.")
                except dbus.exceptions.DBusException as e:
                    print(f"Error setting speed for player {i}: {e}")


def getPlayerList():
    for i in bus.list_names():
        if i.startswith("org.mpris.MediaPlayer2."):
            players.append(i)

if not os.path.isdir(directory):
    os.makedirs(directory)
    if not os.path.isdir(directory+'/players'):
        os.makedirs(directory+'/players')
    if not os.path.isdir(directory+'/paused-players'):
        os.makedirs(directory+'/paused-players')

if len(sys.argv)-1 >= 1:
    getPlayerList()
    if sys.argv[1] in ['--version', '-v']:
        version = get_version()
        if version:
            print(f"Version: {version}")
        else:
            print("Error: Unable to determine version from PKGBUILD.")
    elif sys.argv[1] == 'pause':
        pause()
    elif sys.argv[1] == 'play':
        play()
    elif sys.argv[1] == 'stop':
        stop()
    elif sys.argv[1] == 'next':
        next()
    elif sys.argv[1] == 'previous':
        previous()
    elif sys.argv[1] == 'toggle':
        toggle()
    elif sys.argv[1] == 'seek' and len(sys.argv) == 3:
        seek(sys.argv[2])
    elif sys.argv[1] == 'speed' and len(sys.argv) == 3:
        set_speed(sys.argv[2])
    else:
        print("Error: Valid commands to "+sys.argv[0]+" are: pause, play, stop, next, previous, toggle, or seek <seconds>")
else:
    print("Usage: "+sys.argv[0]+" [pause|play|stop|next|previous|toggle|seek <seconds>]")
