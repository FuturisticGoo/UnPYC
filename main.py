# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 09:54:50 2020

@author: FuturisticGoo
"""
# Hey there random stranger! Have a nice day.

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QProcess
from modules import magic, py_source, pyinstxtractor
from modules.form import Ui_MainWindow
from modules.settings import Ui_Settings
from modules.how_to_use import Ui_HowToUse
from modules.about import Ui_About
import qt_material
import random
import subprocess
import threading
import platform
import shutil
from zipfile import ZipFile, BadZipFile
import os
from urllib import request, error
import time
import sys

bundled_PyVersion = platform.python_version()
portable_git_link = r"https://github.com/FuturisticGoo/portable_python/raw/main/py_distros/"
portable_py_links = {"2.6": [portable_git_link+"python_2.6_wu6.zip",
                             portable_git_link+"python_2.6_wpsw_wu6.zip"],
                     "2.7": [portable_git_link+"python_2.7_wu6.zip",
                             portable_git_link+"python_2.7_wpsw_wu6.zip"],
                     "3.1": [portable_git_link+"python_3.1_wu6.zip",
                             portable_git_link+"python_3.1_wpsw_wu6.zip"],
                     "3.2": [portable_git_link+"python_3.2_wu6.zip",
                             portable_git_link+"python_3.2_wpsw_wu6.zip"],
                     "3.3": [portable_git_link+"python_3.3_wu6.zip",
                             portable_git_link+"python_3.3_wpsw_wu6.zip"],
                     "3.4": [portable_git_link+"python_3.4_wu6.zip",
                             portable_git_link+"python_3.4_wpsw_wu6.zip"],
                     "3.5": [portable_git_link+"python_3.5_wu6.zip",
                             portable_git_link+"python_3.5_wpsw_wu6.zip"],
                     "3.6": [portable_git_link+"python_3.6_wu6.zip",
                             portable_git_link+"python_3.6_wpsw_wu6.zip"],
                     "3.7": [portable_git_link+"python_3.7_wu6.zip",
                             portable_git_link+"python_3.7_wpsw_wu6.zip"],
                     "3.8": [portable_git_link+"python_3.8_wu6.zip",
                             portable_git_link+"python_3.8_wpsw_wu6.zip"]}

fonts_list = ["antar.ttf", "Bombardment3D.ttf", "BorderBase.ttf",
              "dignity of labour.ttf"]

rand_font_loc = os.path.join(os.getcwd(), "fonts", fonts_list[random.randint(0, 3)])

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


class Settings(QtWidgets.QDialog):
    def __init__(self):
        super(Settings, self).__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.ui.clear_button.clicked.connect(self.clear_py)

    def clear_py(self):

        if(os.path.exists(os.path.join(os.getcwd(), "portable_python"))):
            self.ui.clear_button.setText("Clearing...")

            def clear_it():
                shutil.rmtree(os.path.join(os.getcwd(), "portable_python"))
                self.ui.clear_button.setText("Cleared!")
            clear = threading.Thread(target=clear_it)
            clear.start()

        else:
            self.ui.clear_button.setText("Cleared!")


class About(QtWidgets.QDialog):
    def __init__(self):
        super(About, self).__init__()
        self.ui = Ui_About()
        self.ui.setupUi(self)


class HowToUse(QtWidgets.QDialog):
    def __init__(self):
        super(HowToUse, self).__init__()
        self.ui = Ui_HowToUse()
        self.ui.setupUi(self)


class main(QtWidgets.QMainWindow):

    def ensure_disabled(self):
        self.ui.step_2.setVisible(False)
        self.ui.python_source.setVisible(False)
        self.ui.download_python.setVisible(False)
        self.ui.wpsw_check.setVisible(False)
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

    def getting_sources(self):
        self.ui.console_output.append("""Finding Python installations in \
system, please wait...""")
        self.ui.radio_pyc.setVisible(False)
        self.ui.radio_pyinstaller.setVisible(False)
        self.ui.step_1.setVisible(False)
        self.ui.pyc_loc.setVisible(False)
        self.ui.open_pyc_file.setVisible(False)
        self.installed_python = py_source.get_py()
        self.ui.radio_pyc.setVisible(True)
        self.ui.radio_pyinstaller.setVisible(True)
        self.ui.step_1.setVisible(True)
        self.ui.pyc_loc.setVisible(True)
        self.ui.open_pyc_file.setVisible(True)
        self.ui.console_output.append(f"""Finished. Found \
{len(self.installed_python)} installations""")

    def __init__(self):
        super(main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        py_thread = threading.Thread(target=self.getting_sources)
        py_thread.start()
        self.p = None
        font_id = QtGui.QFontDatabase.addApplicationFont(rand_font_loc)
        font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]
        heading_font = QtGui.QFont(font_family)
        heading_font.setPointSize(40)
        console_font = QtGui.QFont()
        console_font.setPointSize(9)
        self.ensure_disabled()
        self.ui.console_output.setFont(console_font)
        self.ui.heading.setFont(heading_font)

        def pyinstaller_radio():
            self.ui.open_pyc_file.setText("Open Pyinstaller executable")
            self.ui.console_output.setText("")
            self.ui.pyc_loc.setText("Source File")
            self.ensure_disabled()

        def pyc_radio():
            self.ui.open_pyc_file.setText("Open pyc/pyo file")
            self.ui.console_output.setText("")
            self.ui.pyc_loc.setText("Source File")
            self.ensure_disabled()

        self.ui.radio_pyinstaller.clicked.connect(pyinstaller_radio)
        self.ui.radio_pyc.clicked.connect(pyc_radio)
        self.ui.open_pyc_file.clicked.connect(self.open_pyc)
        self.ui.python_source.currentIndexChanged.connect(
                                                        self.py_source_changed)
        self.ui.source_button.clicked.connect(self.get_custom_pysource)
        self.ui.save_as.clicked.connect(self.save_file)
        self.ui.download_python.clicked.connect(self.down_then_extract)
        self.ui.advanced.clicked.connect(self.advanced_vis)
        self.ui.uncompyle_tools.currentIndexChanged.connect(self.choose_tool)
        self.ui.uncompyle_button.clicked.connect(self.uncompile)
        self.ui.actionSettings.triggered.connect(self.settings)
        self.ui.actionHow_to_use.triggered.connect(self.how_to_use)
        self.ui.actionAbout.triggered.connect(self.about)

    def about(self):
        about_dialog = About()
        about_dialog.exec_()

    def how_to_use(self):
        how_to_use_dialog = HowToUse()
        how_to_use_dialog.exec_()

    def settings(self):
        settings_dialog = Settings()
        settings_dialog.exec_()

    def do_process(self, commands, output):

        def handle_stdout():
            data = self.p.readAllStandardOutput()
            stdout = bytes(data).decode("utf8")
            output.append(stdout)

        def handle_stderr():
            data = self.p.readAllStandardError()
            stderr = bytes(data).decode("utf8")
            output.append(f"Error: {stderr}")

        def process_finished():
            self.p = None

        if self.p is None:  # No process running.
            self.p = QProcess()
            self.p.readyReadStandardOutput.connect(handle_stdout)
            self.p.readyReadStandardError.connect(handle_stderr)
            # Clean up once complete.
            self.p.finished.connect(process_finished)
            self.p.start(*commands)

    def auto_python_source(self):
        self.py_match = False
        for version in self.installed_python:
            if(version.startswith(self.py_v[0:3])):
                self.py_match = True
                self.python_folder = os.path.dirname(
                    self.installed_python[version])
                self.python_binary = self.installed_python[version]
                break

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
            if(self.ui.radio_pyc.isChecked()):
                self.ui.step_3.setVisible(True)
                self.ui.destination_loc.setVisible(True)
                self.ui.save_as.setVisible(True)
            else:
                self.ui.uncompyle_button.setVisible(True)
                self.ui.uncompyle_button.setText("Extract!")
                self.ui.step_3.setVisible(False)
                self.ui.destination_loc.setVisible(False)
                self.ui.save_as.setVisible(False)

        elif(bundled_PyVersion.startswith(self.py_v[0:3])):
            self.ui.console_output.append("""The version used in pyc bytecode \
doesn't match any installed Python or no Python installation found, but \
Python bundled with UnPYC matches it.""")
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
source.\nIt will look for previous downloads if any.\nTick the checkbox if \
you plan on using uncompile tools other than uncompyle6""")
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
            self.ui.wpsw_check.setVisible(True)
            self.ui.progress_bar.setTextVisible(True)

        elif(not self.installed_python):
            self.ui.console_output.append("""No python installation, download \
the required Python version or use a custom source.\nTick the checkbox if you \
plan on using uncompile tools other than uncompyle6""")
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
            self.ui.wpsw_check.setVisible(True)
            self.ui.progress_bar.setTextVisible(True)

    def py_source_changed(self):
        if(self.ui.python_source.currentIndex() == 0):
            self.ui.console_output.append("""Press the Download button to \
download the portable Python or use a custom source.\nIt will look for \
previous downloads if any\nTick the checkbox if you plan on using uncompile \
tools other than uncompyle6""")
            self.ensure_disabled()
            self.ui.step_2.setVisible(True)
            self.ui.python_source.setVisible(True)
            self.ui.download_python.setVisible(True)
            self.ui.progress_bar.setVisible(True)
            self.ui.wpsw_check.setVisible(True)
        elif(self.ui.python_source.currentIndex() == 1):
            if(not self.py_match):
                self.ui.console_output.append("""\nError: Installed Python \
version doesn't match pyc bytecode number""")
                self.ensure_disabled()
                self.ui.step_2.setVisible(True)
                self.ui.python_source.setVisible(True)
            else:
                self.ensure_disabled()
                self.ui.step_2.setVisible(True)
                self.ui.python_source.setVisible(True)
            if(self.ui.radio_pyc.isChecked()):
                self.ui.step_3.setVisible(True)
                self.ui.destination_loc.setVisible(True)
                self.ui.save_as.setVisible(True)
            else:
                self.ui.uncompyle_button.setVisible(True)
                self.ui.uncompyle_button.setText("Extract!")
                self.ui.step_3.setVisible(False)
                self.ui.destination_loc.setVisible(False)
                self.ui.save_as.setVisible(False)

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
            if(self.ui.radio_pyc.isChecked()):
                self.open_file = QtWidgets.QFileDialog.getOpenFileName(
                    self, "Open pyc/pyo file",
                    filter="Python bytecode(*.pyc *.pyo)")[0]
            else:
                self.open_file = QtWidgets.QFileDialog.getOpenFileName(
                    self, "Open pyinstaller executable file")[0]
            if(not self.open_file):
                raise FileNotFoundError
            self.ui.destination_loc.setText("")
            self.ui.console_output.setText("")
            self.ui.pyc_loc.setText(self.open_file)
            if(self.ui.radio_pyc.isChecked()):
                self.py_v = magic.get_magic(self.open_file)
            else:
                sys.argv = ["pyinstxtractor.py", self.open_file]
                self.py_v = pyinstxtractor.main()

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
            elif(self.py_v is None):
                self.ui.console_output.append("""File might not be \
pyinstaller file or it might be corrupt""")
            elif(self.py_v[0:3] in ["3.9", "3.10"]):
                self.ui.console_output.append(
                    f"Python Bytecode version {self.py_v}\n")
                self.ui.console_output.append("""\nNo uncompile tool supports \
Python 3.9 or 3.10 currently.""")
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
            self.ui.console_output.append("""\nThe uncompyle tool supports \
the pyc version.""")
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
                percent = int(readsofar*100/totalsize)
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
        self.python_binary = os.path.join(self.python_folder, "python")
        if(os.path.exists(self.python_folder)):
            self.ui.console_output.append("Zip already extracted")
            self.check_py_v(self.python_folder)

        else:
            self.ui.console_output.append("Extracting")
            time.sleep(0.5)
            self.ui.progress_bar.reset()
            with ZipFile(source_zip) as zf:
                for i in zf.filelist:
                    total += i.file_size
                for member in zf.namelist():
                    try:
                        current += zf.getinfo(member).file_size
                        percentage = int(current*100/total)
                        self.ui.progress_bar.setValue(percentage)
                        zf.extract(member, target_folder)
                    except Exception as err:
                        print(err)
                        self.ui.console_output.append(err)
            self.ui.console_output.append("Finished extraction")
            self.check_py_v(self.python_folder)

    def down_then_extract(self):
        if (self.ui.wpsw_check.isChecked()):
            url = portable_py_links[self.py_v[0:3]][1]
        else:
            url = portable_py_links[self.py_v[0:3]][0]

        down = threading.Thread(target=self.download_py,
                                args=(url,))
        down.start()

    def check_py_v(self, python_folder):
        self.ui.console_output.append("\nChecking Python interpreter version")
        try:
            check = subprocess.Popen([self.python_binary,
                                     "-c", "import platform;\
                                     print(platform.python_version())"],
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     encoding="utf-8")
            self.custom_py_v = check.communicate()[0]

            self.custom_py_v = self.custom_py_v.strip()[0:3]
            self.ui.console_output.append(f"""\nPython interpreter version \
{self.custom_py_v}""")

            if(self.custom_py_v == self.py_v[0:3]):
                if(self.ui.radio_pyc.isChecked()):
                    self.ui.console_output.append("""\nPython interpreter \
version matches pyc bytecode version.
Proceed to Step 3""")
                    self.ui.uncompyle_button.setText("Uncompyle!")
                    self.ui.step_3.setVisible(True)
                    self.ui.destination_loc.setVisible(True)
                    self.ui.save_as.setVisible(True)
                else:
                    self.ui.console_output.append("""\nPython interpreter \
version matches pyc bytecode version.
Proceed to extract.""")
                    self.ui.uncompyle_button.setVisible(True)
                    self.ui.uncompyle_button.setText("Extract!")
                    self.ui.step_3.setVisible(False)
                    self.ui.destination_loc.setVisible(False)
                    self.ui.save_as.setVisible(False)
                    self.ui.advanced.setVisible(False)
                    self.ui.uncompyle_tool_label.setVisible(False)
                    self.ui.uncompyle_tools.setVisible(False)
                    self.ui.uncompyle_button.setVisible(True)
            else:
                self.ui.console_output.append("""\nPython interpreter \
version does not matches pyc bytecode version.
Use another Python source""")
                self.ui.step_3.setVisible(False)
                self.ui.destination_loc.setVisible(False)
                self.ui.save_as.setVisible(False)

        except OSError as f:
            self.ui.console_output.append("Error: Folder doesn't contain \
Python binary")
            self.ui.console_output.append(f"Error text: {f}")

    def save_file(self):
        try:
            self.save_folder = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Save in Folder")

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
            self.python_binary = QtWidgets.QFileDialog.getOpenFileName(
                self, "Locate the Python Installation Folder",
                filter="python*")[0]

            if(not self.python_binary):
                raise FileNotFoundError
            else:
                self.python_folder = os.path.dirname(self.python_binary)
                self.ui.custom_source_loc.setText(self.python_folder)
                self.check_py_v(self.python_folder)

        except FileNotFoundError:
            pass

    def uncompile(self):
        if(self.ui.radio_pyc.isChecked()):
            uncompyle_py_source = os.path.join(self.python_folder,
                                               "Lib", "site-packages",
                                               "uncompyle6", "bin",
                                               "uncompile.py")
            if(os.path.exists(uncompyle_py_source)):
                unc_command = (self.python_binary, [uncompyle_py_source, "-o",
                               self.save_folder, self.open_file])
                self.ui.console_output.append("\nUncompiling...")
                self.do_process(unc_command, self.ui.console_output)
            else:
                self.ui.console_output.append(f"""\nUncompyle6 not installed \
in the current python location. Please install uncompyle6 for \
{self.python_binary} using pip install uncompyle6""")

        else:
            py_extractor_source = os.path.join(os.getcwd(), "modules",
                                               "pyinstxtractor.py")
            if(os.path.exists(py_extractor_source)):
                unc_command = (self.python_binary, [py_extractor_source,
                               self.open_file])
                self.ui.console_output.append("\nExtracting...")
                self.do_process(unc_command, self.ui.console_output)
            else:
                self.ui.console_output.append("""\npyinstxractor.py script \
not found in modules folder or python source is not valid. Redownload the \
UnPYC program or check the source for defects.""")


if not QtWidgets.QApplication.instance():
    app = QtWidgets.QApplication([])
else:
    app = QtWidgets.QApplication.instance()
win = main()
qt_material.apply_stylesheet(app, theme="dark_cyan.xml")
win.show()
app.exec_()
