# UnPYC

## Overview

*Important: I won't push more updates to this tool, since it was merely a hobby + learning project.*

This is a GUI tool for decompiling Python bytecode `.pyc/.pyo` back to `.py` using existing tools.   

It's also bundled with a modified [pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor/) for making it easy to extract pyinstaller packaged executables. 

## Features

* Can decompile Python bytecode versions `2.6, 2.7, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8`, using tools like [uncompyle6](https://github.com/rocky/python-uncompyle6).

* Can extract pyinstaller package using pyinstxtractor.

* Makes it easy to decompile pyc's even without Python installed in the system.

* Helps in decompiling pyc's of different versions.

* Works offline if dependencies and Python sources are satisfied, which can be done easily.

  

## How to use

Currently, it's Windows only. Download the latest release here, unzip it and open the UnPYC.exe in the folder. The GUI is very straightforward. For most users, this will be the way to do stuff.  

This is an example of extracting a pyinstaller packaged .exe and decompiling the bytecode stored in it.

![Example Usage](https://raw.githubusercontent.com/FuturisticGoo/UnPYC/main/example/example.gif)

> You can change the theme from the settings menu.

## Portable Python

This project uses portable Python distributions from [here](https://github.com/FuturisticGoo/portable_python). 

## To do

There's a lot of stuff to do in this, like 

* ~~Adding preinstalled Python decompiling~~
* Using bundled Python for decompiling
* Lots (and I mean lots) of code refactoring
* Adding Linux support
* Adding more decompiling tools support
* Adding Python 3.9, 3.10
* Adding macOS support
* Add Linux release
* More user friendly UI
* ~~Cleanup after usage~~ Added a clean button in settings

This project is under development, so there might be tons of bugs and crashes. Also, the console isn't hidden right now, so that errors can be seen there.

## License

This project is under GPL v3.0 license, but the libraries and resources used here have their own respective licenses.   
Icon by [Icongeek26](https://www.flaticon.com/authors/icongeek26) under CC License  
The license file for the resources like fonts are stored in the same folder.

PyQt5 is licensed under GPL
