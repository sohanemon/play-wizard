# **Play-Wizard**

Play-Wizard is a Python program to control media players via DBus.

## **Description**

Ever wanted to control all your media players effortlessly with a single command or hotkey?  
With **Play-Wizard**, you can wave your wand and take command of playback across all your running media players—no scripting required!  

This program is inspired by OmniPause, which provided the foundational idea of managing multiple media players through a single interface.

Enjoy a seamless and magical experience managing your media.

## **Dependencies**

To use Play-Wizard, you need:  
- Python 3  
- `dbus-python` library  

## **Setup**

Setup is simple:  
1. Clone this repository:  
   ```bash
   git clone https://github.com/sohanemon/play-wizard
   cd play-wizard
   ```  
2. Install the program:  
   ```bash
   makepkg -si
   ```  

## **Usage**

Play-Wizard lets you control media players with straightforward commands. The following table summarizes the available commands:

| **Command**                | **Description**                                                                                   | **Example Usage**                    |
|----------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------|
| `play-wizard pause`        | Pause playback for all running media players.                                                    | `play-wizard pause`                 |
| `play-wizard play`         | Resume playback of media players paused by Play-Wizard.                                          | `play-wizard play`                  |
| `play-wizard stop`         | Stop playback on all media players.                                                              | `play-wizard stop`                  |
| `play-wizard next`         | Skip to the next track on all playing media players.                                             | `play-wizard next`                  |
| `play-wizard previous`     | Play the previous track on all playing media players.                                            | `play-wizard previous`              |
| `play-wizard toggle`       | Toggle playback state of all media players.                                                     | `play-wizard toggle`                |
| `play-wizard seek <seconds>` | Seek to a position in the current track.                                                       | `play-wizard seek 30`               |
| `play-wizard speed <value>` | Set playback speed for all players.                                                             | `play-wizard speed 1.5`             |
| `play-wizard speed +<value>` or `-<value>` | Adjust playback speed relative to the current speed (e.g., `+0.1` to increase by 0.1x). | `play-wizard speed +0.1`            |

### **Additional Notes**
- **Toggle Command**:  
  If any players are playing, the `toggle` command will pause them. If none are playing, it resumes playback on players paused by Play-Wizard.  

- **Playback Speed**:  
  - Use `play-wizard speed <value>` for absolute speed changes (e.g., `1.5` for 1.5x speed).  
  - Use `play-wizard speed +<value>` or `-<value>` for relative speed changes (e.g., `+0.1` to increase speed by 0.1x).  
  - The speed is rounded to two decimal places to ensure consistency.  


## **Contributing**

This project is built to bring simplicity and control to your media playback.  
If you find bugs or have suggestions for improvement, please submit a pull request or open an issue on the repository.  

## Acknowledgments

- OmniPause for inspiring the core concept of managing media players through DBus.

## **License**

This project is licensed under **GPL 3.0**.  

