# Seagull Scaring V2 Lite
A minimal seagull scaring program with GUI that has no external dependencies.
Sound effects come separately.

### ⚠ This program will only run on Windows!

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Static Badge](https://img.shields.io/badge/formatter-black-formatter)
![Static Badge](https://img.shields.io/badge/linter-pylint-linter)
![Static Badge](https://img.shields.io/badge/type_checker-mypy-blue)

> [!WARNING]
> Seagull Scaring V2 Lite will reach end of support in July 2026. There will be no further updates to the program after this date.

The days of having me run around scaring seagulls manually are over! With Seagull Scaring, you can just start the program, choose a time to scare seagulls for, and relax as the seagulls fly away when you want.\
Recommended settings: 2700 seconds (timer), 60 seconds (min time), 300 seconds (max time), seagull (sound).

### About this project
Seagull Scaring was created to stop the biggest problem plaguing my school since I can’t remember when. 
It has been tested to have a 98% success rate against seagulls (or shall I say gulls) of all shapes and sizes! 
Seagull Scaring V2 Lite is a user-friendly GUI interface for Seagull Scaring 1.4 written using the Tkinter library. 
The recommended settings are meant to be used during 1 lunchtime (45 minutes).

### Install instructions
1. Unzip the program folder.
2. Make sure you have Tkinter installed.
3. Copy a `media.zip` to the program folder, and run `main.pyw`.

### Config file documentation
In the program directory, there is a file called `ssv2cfg.ini`.

You may edit this file as you desire.

**All settings must go in the [main] section.**

Valid settings: 

`scaring_time (int)`: How long to run the program for.

`min_time (int)`: Minimum time to wait.

`max_time (int)`: Maximum time to wait.

`default_volume (int)`: Default volume from 0-100.

`default_sound (str)`: Seagull sound to use. Valid options: seagull, sad seagull, angry seagull, confused seagull, disgust seagull, robot seagull, alarm seagull, Seagull 2, sea gull.

`autostart (str)`: Enable/disable autostart feature. Valid options: yes/no.

`autostart_delay (int)`: Delay seconds for the autostart feature.

### Sending announcements
To send an announcement, you will need an `alarm_seagull.wav` either from Gabriel's Seagull Sound Pack (available separately) or your own choosing.
Click "send announcement" in the program window and a text box will appear for you to enter your message.
Once you click OK, the alarm seagull sound effect will play twice, then a TTS voice will say "This is a Seagull Wars public service announcement", read out your message, and play the alarm seagull sound twice again.

### Errors/warnings
"No sound effects" - The `media` folder is not present. To fix, download sound effects and move them into the folder.

"No alarm seagull" - The `alarm_seagull.wav` file is not present. Without this file, you will not be able to send announcements. To fix, download a WAV file, name it `alarm_seagull.wav` and place it into the `media` folder.
