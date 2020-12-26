# UnPYC

## Overview

This is a GUI tool for uncompiling Python bytecode `.pyc` back to `.py` using existing tools.

## Features

* Can uncompile Python bytecode versions `2.6, 2.7, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8`, using tools like [uncompyle6](https://github.com/rocky/python-uncompyle6).

* Makes it easy to uncompile pyc's even without Python installed in the system.

* Helps in uncompiling pyc's of different versions.

* Works offline if dependencies and Python sources are satisfied, which can be done easily.

  

## How to use

Currently, it's Windows only. Download the latest release here, unzip it and open the UnPYC.exe in the folder. The GUI is very straightforward. For most users, this will be the way to do stuff.

![Example GIF](https://github.com/FuturisticGoo/UnPYC/example/example.gif)

## Portable Python

This project uses portable Python distributions from [here](https://github.com/FuturisticGoo/portable_python). 

## To do

There's a lot of stuff to do in this, like 

* Adding preinstalled Python uncompiling
* Using bundled Python for uncompiling
* Lots (and I mean lots) of code refactoring
* Adding Linux support
* Adding more uncompiling tools support
* Adding Python 3.9, 3.10
* Adding macOS support
* Add Linux release
* More user friendly UI
* Cleanup after usage

This project is under heavy development, so there might be tons of bugs and crashes.

## License

This project is under GPL v3.0 license, but the libraries and resources used here have their own respective licenses. 

The license file for the resources like fonts are stored in the same folder.

PySide6 is licensed under LGPL