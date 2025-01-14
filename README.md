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

Play-Wizard lets you control media players with straightforward commands:  
- **Pause playback** for all running media players:  
  ```bash
  play-wizard pause
  ```  
- **Resume playback** of media players paused by Play-Wizard:  
  ```bash
  play-wizard play
  ```  
- **Stop playback** on all media players:  
  ```bash
  play-wizard stop
  ```  
- **Skip to the next track** on all playing media players:  
  ```bash
  play-wizard next
  ```  
- **Play the previous track** on all playing media players:  
  ```bash
  play-wizard previous
  ```  
- **Toggle playback state** of all media players:  
  ```bash
  play-wizard toggle
  ```  
  > **Note:** If any players are playing, the toggle command will pause them. If none are playing, it resumes playback on players paused by Play-Wizard.  

- **Seek** to a position in the current track:  
  ```bash
  play-wizard seek <seconds>
  ```  

- **Set playback speed** for all players:  
  ```bash
  play-wizard speed <multiplier>
  ```  
  Example: `play-wizard speed 1.5` for 1.5x playback speed.  

## **Contributing**

This project is built to bring simplicity and control to your media playback.  
If you find bugs or have suggestions for improvement, please submit a pull request or open an issue on the repository.  

## Acknowledgments

- OmniPause for inspiring the core concept of managing media players through DBus.

## **License**

This project is licensed under **GPL 3.0**.  

