# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 09:54:50 2020

@author: FuturisticGoo
"""

from PyQt5 import QtWidgets, QtGui
from form import Ui_MainWindow
import qt_material
import random
import subprocess
import threading
import magic
import py_source
import platform
from zipfile import ZipFile
import os
from urllib import request, error
import time

bundled_PyVersion = platform.python_version()

portable_py_links = {"2.6": r"https://github.com/FuturisticGoo/portable_python/raw/main/python_2.6_wu6.zip",
                     "2.7": r"https://github.com/FuturisticGoo/portable_python/raw/main/python_2.7_wu6.zip",
                     "3.1": r"https://github.com/FuturisticGoo/portable_python/raw/main/python_3.1_wu6.zip",
                     "3.2": r"https://github.com/FuturisticGoo/portable_python/raw/main/python_3.2_wu6.zip",
                     "3.3": r"https://github.com/FuturisticGoo/portable_python/raw/main/python_3.3_wu6.zip",
                     "3.4": r"https://github.com/FuturisticGoo/portable_python/raw/main/python_3.4_wu6.zip",
                     "3.5": r"https://github.com/FuturisticGoo/portable_python/raw/main/python_3.5_wu6.zip",
                     "3.6": r"https://github.com/FuturisticGoo/portable_python/raw/main/python_3.6_wu6.zip",
                     "3.7": r"https://github.com/FuturisticGoo/portable_python/raw/main/python_3.7_wu6.zip",
                     "3.8": r"https://github.com/FuturisticGoo/portable_python/raw/main/python_3.8_wu6.zip"}

fonts_list = ["antar.ttf", "Bombardment3D.ttf", "BorderBase.ttf",
              "dignity of labour.ttf"]

rand_font_loc = os.path.join("fonts", fonts_list[random.randint(0, 3)])

py_support = {"rocky/uncompyle6 (1.0-3.8) (default)": ["1.0", "1.2", "1.3",
                                                       "1.4", "1.5", "1.6",
                                                       "2.0", "2.1", "2.2",
                                                       "2.3", "2.4", "2.5",
                                                       "2.6", "2.7", "3.0",
                                                       "3.1", "3.2", "3.3",
                                                       "3.4", "3.5", "3.6",
                                                       "3.7", "3.8"],
              "zrax/pycdc (2.7 - 3.3)": ["2.7", "3.0", "3.1", "3.2", "3.3"],
              "rocky/decompile3 (3.7+)": ["3.7", "3.8"],
              "wibiti/uncompyle2 (2.7)": ["2.7"],
              "figment/unpyc3 (3.3)": ["3.3"],
              "andrew-tavera/unpyc37 (3.7)": ["3.7"],
              "unpyc3 (3.2)": ["3.2"],
              "gtarnberger/uncompyle (2.7)": ["2.7"]
              }


class main(QtWidgets.QMainWindow):

    def ensure_disabled(self):
        self.ui.step_2.setVisible(False)
        self.ui.python_source.setVisible(False)
        self.ui.download_python.setVisible(False)
        self.ui.progress_bar.reset()
        self.ui.progress_bar.setVisible(False)
        self.ui.custom_source_loc.setVisible(False)
        self.ui.source_button.setVisible(False)
        self.ui.step_3.setVisible(False)
        self.ui.destination_loc.setVisible(False)
        self.ui.save_as.setVisible(False)
        self.ui.advanced.setVisible(False)
        self.ui.uncompyle_tool_label.setVisible(False)
        self.ui.uncompyle_tools.setVisible(False)
        self.ui.uncompyle_button.setVisible(False)

    def __init__(self):
        super(main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        font_id = QtGui.QFontDatabase.addApplicationFont(rand_font_loc)
        font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]
        heading_font = QtGui.QFont(font_family)
        heading_font.setPointSize(40)
        console_font = QtGui.QFont("Arial")
        console_font.setPointSize(8)
        self.ui.console_output.setFont(console_font)
        self.ui.heading.setFont(heading_font)
        self.ensure_disabled()

        self.ui.open_pyc_file.clicked.connect(self.open_pyc)
        self.ui.python_source.currentIndexChanged.connect(
                                                        self.py_source_changed)
        self.ui.source_button.clicked.connect(self.get_custom_pysource)
        self.ui.save_as.clicked.connect(self.save_file)
        self.ui.download_python.clicked.connect(self.down_then_extract)
        self.ui.advanced.clicked.connect(self.advanced_vis)
        self.ui.uncompyle_tools.currentIndexChanged.connect(self.choose_tool)
        self.ui.uncompyle_button.clicked.connect(self.uncompile)

    def do_process(self, commands, output, background=False, message=""):
        self.result = []
        process = subprocess.Popen(
            commands,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8',
            errors='replace'
        )

        while True:
            realtime_output = process.stdout.readline()

            if realtime_output == '' and process.poll() is not None:
                break

            if realtime_output:
                if(background):
                    self.result.append(realtime_output.strip())
                elif(not message):
                    output.append(realtime_output.strip())
                else:
                    pass
        output.append(message)

    def auto_python_source(self):
        self.installed_python = py_source.get_py()
        self.py_match = False
        for version in self.installed_python:
            if(version.startswith(self.py_v[0:3])):
                self.py_match = True

        if(self.installed_python and self.py_match):
            self.ui.console_output.append("""Python installation found in \
system and matches the version used in pyc bytecode magic number.
No need to download anything.\nSkip Step 2""")
            self.ui.step_2.setVisible(True)
            self.ui.python_source.setVisible(True)
            self.ui.download_python.setVisible(False)
            self.ui.progress_bar.setVisible(False)
            self.ui.python_source.setCurrentText(
                "Use currently installed python")
            self.ui.step_3.setVisible(True)
            self.ui.destination_loc.setVisible(True)
            self.ui.save_as.setVisible(True)

        elif(bundled_PyVersion.startswith(self.py_v[0:3])):
            self.ui.console_output.append("""The version used in pyc bytecode \
doesn't match any installed Python or no Python installation found, but \
Python bundled with UnPYC mathces it.""")
            self.ensure_disabled()
            self.ui.step_2.setVisible(True)
            self.ui.python_source.setVisible(True)
            self.ui.python_source.setCurrentText("Use UnPYC bundled python")
            self.ui.step_3.setVisible(True)
            self.ui.destination_loc.setVisible(True)
            self.ui.save_as.setVisible(True)

        elif(self.installed_python):
            self.ui.console_output.append("""Python installation found in \
system but doesn't match the version used in pyc bytecode magic number.
Press the Download button to download the portable Python or use a custom \
source.\nIt will look for previous downloads if any""")
            self.ensure_disabled()
            self.ui.step_2.setVisible(True)
            self.ui.python_source.setVisible(True)
            self.ui.python_source.setCurrentText(
                "Download portable python (recommended)")
            self.ui.step_3.setVisible(False)
            self.ui.destination_loc.setVisible(False)
            self.ui.save_as.setVisible(False)
            self.ui.download_python.setVisible(True)
            self.ui.progress_bar.setVisible(True)
            self.ui.progress_bar.setTextVisible(True)

        elif(not self.installed_python):
            self.ui.console_output.append("""No python installation, download \
                                             the required Python version or \
                                             use a custom source.""")
            self.ensure_disabled()
            self.ui.step_2.setVisible(True)
            self.ui.python_source.setVisible(True)
            self.ui.python_source.setCurrentText(
                "Download portable python (recommended)")
            self.ui.step_3.setVisible(False)
            self.ui.destination_loc.setVisible(False)
            self.ui.save_as.setVisible(False)
            self.ui.download_python.setVisible(True)
            self.ui.progress_bar.setVisible(True)
            self.ui.progress_bar.setTextVisible(True)

    def py_source_changed(self):
        if(self.ui.python_source.currentIndex() == 0):
            self.ensure_disabled()
            self.ui.step_2.setVisible(True)
            self.ui.python_source.setVisible(True)
            self.ui.download_python.setVisible(True)
            self.ui.progress_bar.setVisible(True)
        elif(self.ui.python_source.currentIndex() == 1):
            if(self.py_v[0:3] not in self.installed_python):
                self.ui.console_output.append("""\nError: Installed Python \
version doesn't match pyc bytecode number""")
                self.ensure_disabled()
                self.ui.step_2.setVisible(True)
                self.ui.python_source.setVisible(True)
        elif(self.ui.python_source.currentIndex() == 2):
            if(bundled_PyVersion[0:3] != self.py_v[0:3]):
                self.ui.console_output.append("""\nError: Bundled Python \
version doesn't match pyc bytecode number""")
                self.ensure_disabled()
                self.ui.step_2.setVisible(True)
                self.ui.python_source.setVisible(True)
        elif(self.ui.python_source.currentIndex() == 3):
            self.ensure_disabled()
            self.ui.step_2.setVisible(True)
            self.ui.python_source.setVisible(True)
            self.ui.source_button.setVisible(True)
            self.ui.custom_source_loc.setVisible(True)

    def open_pyc(self):
        self.ensure_disabled()
        try:
            self.open_file = QtWidgets.QFileDialog.getOpenFileName(
                self, "Open PYC file", filter="*.pyc")[0]
            if(not self.open_file):
                raise FileNotFoundError
            self.ui.destination_loc.setText("")
            self.ui.console_output.setText("")
            self.ui.pyc_loc.setText(self.open_file)
            self.py_v = magic.get_magic(self.open_file)

            if(self.py_v == "Error:1"):
                self.ui.console_output.append(
                    "Wrong magic number in the pyc bytecode")
                self.ensure_disabled()
            elif(self.py_v == "Error:2"):
                self.ui.console_output.append("Unknown python version")
                self.ensure_disabled()
            elif(self.py_v == "Error:3"):
                self.ui.console_output.append(
                    "File is not a python bytecode or is corrupt")
                self.ensure_disabled()
            elif(self.py_v == "Error:4"):
                self.ui.console_output.append("Unknown error")
                self.ensure_disabled()

            elif(self.py_v[0:3] in ["3.9", "3.10"]):
                self.ui.console_output.append(
                    f"Python Bytecode version {self.py_v}\n")
                self.ui.console_output.append("\nNo uncompile tool supports\
                                               Python 3.9 or 3.10 currently.")
                self.ensure_disabled()
            else:
                self.ui.console_output.append(
                    f"Python Bytecode version {self.py_v}\n")
                self.auto_python_source()
        except FileNotFoundError:
            pass

    def advanced_vis(self):
        if(self.ui.uncompyle_tool_label.isVisible()):
            self.ui.advanced.setText("Advanced ▶")
            self.ui.uncompyle_tool_label.setVisible(False)
            self.ui.uncompyle_tools.setVisible(False)
        else:
            self.ui.advanced.setText("Advanced ▾")
            self.ui.uncompyle_tool_label.setVisible(True)
            self.ui.uncompyle_tools.setVisible(True)

    def choose_tool(self):
        self.current = self.ui.uncompyle_tools.currentText()
        if(self.py_v[0:3] in ["3.9", "3.10"]):
            self.ui.console_output.append("""\nNo uncompile tool supports\
Python 3.9 or 3.10 currently.""")
            self.ui.uncompyle_button.setEnabled(False)

        elif(self.py_v[0:3] in py_support[self.current]):
            self.ui.console_output.append("""\nThe uncompyle tool supports the\
 pyc version.""")
            self.ui.uncompyle_button.setEnabled(True)

        else:
            self.ui.console_output.append("""\nThis uncompile tool doesn't \
support the version used for the pyc""")
            self.ui.uncompyle_button.setEnabled(False)

    def download_py(self, url):

        if(not os.path.exists("portable_python")):
            os.mkdir("portable_python")

        target_file = os.path.join(os.getcwd(),
                                   "portable_python",
                                   os.path.basename(url))

        if(os.path.exists(target_file)):
            self.ui.console_output.append("\nPrevious download exists")
            self.extract(target_file,
                         os.path.join(os.getcwd(), "portable_python"))

        else:
            def reporthook(blocknum, blocksize, totalsize):
                readsofar = blocknum * blocksize
                percent = int(readsofar * 100 / totalsize)
                self.ui.progress_bar.setValue(percent)

            self.ui.console_output.append("\nDownloading portable python")
            time.sleep(0.3)
            self.ui.progress_bar.reset()

            try:
                request.urlretrieve(url, target_file, reporthook)
                self.extract(target_file,
                             os.path.join(os.getcwd(), "portable_python"))
            except error.URLError:
                self.ui.console_output.append("""\nError: Network error. \
Check if you're connected to the internet""")

    def extract(self, source_zip, target_folder):
        current = 0
        total = 0
        self.python_folder = os.path.join(
            target_folder, "python_"+self.py_v[0:3])
        if(os.path.exists(self.python_folder)):
            self.ui.console_output.append("Zip already extracted")
            self.check_py_v(self.python_folder)

        else:
            self.ui.console_output.append("Extracting")
            time.sleep(1)
            self.ui.progress_bar.reset()
            with ZipFile(source_zip) as zf:
                for i in zf.filelist:
                    total += i.file_size
                for member in zf.namelist():
                    try:
                        current += (zf.getinfo(member).file_size)
                        percentage = int((current/total)*100)
                        self.ui.progress_bar.setValue(percentage)
                        zf.extract(member, target_folder)
                    except Exception as err:
                        print(err)
                        self.ui.console_output.append(err)

            self.ui.console_output.append("Finished extraction")
            self.check_py_v(self.python_folder)

    def down_then_extract(self):
        down = threading.Thread(target=self.download_py,
                                args=(portable_py_links[self.py_v[0:3]],))
        down.start()

    def check_py_v(self, python_folder):
        self.ui.console_output.append("\nChecking Python interpreter version")
        check = subprocess.Popen(f'''"{os.path.join(python_folder, 'python')}"''' +
                                 ' -c "import platform;\
                               print(platform.python_version())"',
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
        self.custom_py_v, err = check.communicate()

        if(err):
            print(err)
            self.ui.console_output.append("\nFolder doesn't contain Python")
        else:
            self.custom_py_v = self.custom_py_v.strip().decode("utf-8")[0:3]
            self.ui.console_output.append(f"""\nPython interpreter version\
 {self.custom_py_v}""")

            if(self.custom_py_v == self.py_v[0:3]):
                self.ui.console_output.append("""\nPython interpreter version \
matches pyc bytecode version.
Proceed to Step 3""")
                self.ui.step_3.setVisible(True)
                self.ui.destination_loc.setVisible(True)
                self.ui.save_as.setVisible(True)
            else:
                self.ui.console_output.append("""\nPython interpreter version\
 does not matches pyc bytecode version.
Use another Python source""")

    def save_file(self):
        try:
            self.save_folder = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Save")

            if(not self.save_folder):
                raise FileNotFoundError
            else:
                self.ui.destination_loc.setText(self.save_folder)
                self.ui.advanced.setVisible(True)
                self.ui.uncompyle_button.setVisible(True)
                self.ui.console_output.append("\nPress Uncompyle!")

        except FileNotFoundError:
            pass

    def get_custom_pysource(self):
        try:
            self.python_folder = QtWidgets.QFileDialog.getOpenFileName(
                self, "Custom Python Source", filter="python*")[0]

            if(not self.python_folder):
                raise FileNotFoundError
            else:
                self.python_folder = os.path.dirname(self.python_folder)
                self.check_py_v(self.python_folder)
                self.ui.custom_source_loc.setText(self.python_folder)
        except FileNotFoundError:
            pass

    def uncompile(self):
        c1 = os.path.join(self.python_folder, "python")
        c2 = os.path.join(self.python_folder, "Lib", "site-packages",
                          "uncompyle6", "bin", "uncompile.py")
        unc_command = f'"{c1}"' + f' "{c2}"' +\
                      f' -o "{self.save_folder}" "{self.open_file}" '
        self.ui.console_output.append("\nUncompiling...")
        thread = threading.Thread(target=self.do_process,
                                  args=(unc_command, self.ui.console_output,
                                        False, "\nUncompiling finished!"))
        thread.start()


if not QtWidgets.QApplication.instance():
    app = QtWidgets.QApplication([])
else:
    app = QtWidgets.QApplication.instance()
win = main()
qt_material.apply_stylesheet(app, theme="dark_teal.xml")
win.show()
app.exec_()
