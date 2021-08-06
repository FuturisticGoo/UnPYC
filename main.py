# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 09:54:50 2020

@author: FuturisticGoo
"""
# Hey there random stranger! Have a nice day.

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QProcess, QThread, pyqtSignal
from modules import magic, py_source, pyinstxtractor
from modules.form import Ui_MainWindow
from modules.settings import Ui_Settings
import qt_material
import random
import subprocess
import threading
import platform
import shutil
from zipfile import ZipFile
import os
from urllib import request, error
import time
import sys

bundled_PyVersion = platform.python_version()
portable_git_link = r"https://github.com/FuturisticGoo/portable_python/raw/main/py_distros/"
#portable_git_link = "http://127.0.0.1:8000/"  # For testing
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

rand_font_loc = os.path.join(
    os.getcwd(), "fonts", fonts_list[random.randint(0, 3)])

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



class Settings(QtWidgets.QDialog, qt_material.QtStyleTools):
    theme_signal = pyqtSignal(list)
    def __init__(self):
        super(Settings, self).__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.material = qt_material.list_themes()
        self.material = [i.replace(".xml", "") for i in self.material]
        self.ui.theme_combo.addItems(self.material)
        self.ui.clear_button.clicked.connect(self.clear_py)
        self.ui.theme_combo.currentTextChanged.connect(self.change_theme)

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

    def change_theme(self, theme):
        if theme.startswith("dark"):
            self.apply_stylesheet(self, theme+".xml")
            self.theme_signal.emit([theme+".xml", False])
        else:
            self.apply_stylesheet(self, theme+".xml",invert_secondary=True)
            self.theme_signal.emit([theme+".xml", True])
        #Main.apply_stylesheet(self, theme+".xml")

class DownloadThread(QThread):
    dw_val = pyqtSignal(int)
    finish = pyqtSignal(list)
    console_message = pyqtSignal(str)

    def __init__(self, url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url

    def run(self):
        if(not os.path.exists("portable_python")):
            os.mkdir("portable_python")

        target_file = os.path.join(os.getcwd(),
                                   "portable_python",
                                   os.path.basename(self.url))

        if(os.path.exists(target_file)):
            self.console_message.emit("\nPrevious download exists")
            self.finish.emit([True, target_file,
                         os.path.join(os.getcwd(), "portable_python")])


        else:
            def reporthook(blocknum, blocksize, totalsize):
                readsofar = blocknum * blocksize
                percent = int(readsofar*100/totalsize)
                self.dw_val.emit(percent)

            self.console_message.emit("\nDownloading portable python")

            try:
                request.urlretrieve(self.url, target_file, reporthook)
                self.dw_val.emit(0)
                self.finish.emit([True, target_file,
                         os.path.join(os.getcwd(), "portable_python")])
            except error.URLError as err:
                self.finish.emit([False, err])
                self.console_message.emit("""\nError: Network error. \
Check if you're connected to the internet""")

class ExtractThread(QThread):
    ext_val = pyqtSignal(int)
    finish = pyqtSignal(list)
    console_message = pyqtSignal(str)

    def __init__(self, source_zip, target_folder, py_v, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.source_zip = source_zip
        self.target_folder = target_folder
        self.py_v = py_v
    
    def run(self):
        current = 0
        total = 0
        self.python_folder = os.path.join(
            self.target_folder, "python_"+self.py_v[0:3])
        self.python_binary = os.path.join(self.python_folder, "python")
        if(os.path.exists(self.python_folder)):
            self.console_message.emit("Zip already extracted")
            self.finish.emit([True, self.python_folder, self.python_binary])
            #self.other.check_py_v(self.python_folder)

        else:
            self.console_message.emit("Extracting")
            with ZipFile(self.source_zip) as zf:
                for i in zf.filelist:
                    total += i.file_size
                for member in zf.namelist():
                    try:
                        current += zf.getinfo(member).file_size
                        percentage = int(current*100/total)
                        self.ext_val.emit(percentage)
                        zf.extract(member, self.target_folder)
                    except Exception as err:
                        self.console_message.emit(str(err))
                        self.finish.emit([False, err])
                        return None
            self.console_message.emit("Finished extraction")
            self.finish.emit([True, self.python_folder, self.python_binary])

class Main(QtWidgets.QMainWindow, qt_material.QtStyleTools):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_theme = ["light_red.xml", True]
        self.p = None
        self.download_thread = None
        self.extract_thread = None
        font_id = QtGui.QFontDatabase.addApplicationFont(rand_font_loc)
        font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]
        heading_font = QtGui.QFont(font_family)
        heading_font.setPointSize(40)
        console_font = QtGui.QFont()
        console_font.setPointSize(9)
        self.tab_change() # To abstract the variable names on start
        self.ensure_disabled()
        self.ui.tab1_step_1.setEnabled(False)
        self.ui.tab1_pyc_loc.setEnabled(False)
        self.ui.tab2_step_1.setEnabled(False)
        self.ui.tab2_pyc_loc.setEnabled(False)
        self.ui.console_output.setFont(console_font)
        self.ui.heading.setFont(heading_font)
        py_thread = threading.Thread(target=self.getting_sources)
        py_thread.start()
        self.register_connections()
    
    def register_connections(self):
        self.ui.actionSettings.triggered.connect(self.settings)
        self.ui.left_tab.currentChanged.connect(self.tab_change)

        self.ui.tab1_pyc_loc.clicked.connect(self.open_pyc)
        self.ui.tab1_python_source.currentIndexChanged.connect(self.py_source_changed)
        self.ui.tab1_custom_source_loc.clicked.connect(self.get_custom_pysource)
        self.ui.tab1_destination_loc.clicked.connect(self.save_file)
        self.ui.tab1_download_python.clicked.connect(self.down_then_extract)
        self.ui.tab1_advanced.clicked.connect(self.advanced_vis)
        self.ui.tab1_uncompyle_tools.currentIndexChanged.connect(self.choose_tool)
        self.uncompyle_button.clicked.connect(self.uncompile)

        self.ui.tab2_pyc_loc.clicked.connect(self.open_pyc)
        self.ui.tab2_python_source.currentIndexChanged.connect(self.py_source_changed)
        self.ui.tab2_custom_source_loc.clicked.connect(self.get_custom_pysource)
        self.ui.tab2_destination_loc.clicked.connect(self.save_file)
        self.ui.tab2_download_python.clicked.connect(self.down_then_extract)
        self.ui.tab2_extract_button.clicked.connect(self.uncompile)

    def ensure_disabled(self):
        self.step_2.setEnabled(False)
        self.python_source.setEnabled(False)
        self.download_python.setEnabled(False)
        self.wpsw_check.setEnabled(False)
        self.progress_bar.reset()
        self.progress_bar.setEnabled(False)
        self.custom_source_loc.setVisible(False)
        self.step_3.setEnabled(False)
        self.destination_loc.setEnabled(False)
        self.ui.tab1_advanced.setEnabled(False)
        self.ui.tab1_uncompyle_tool_label.setVisible(False)
        self.ui.tab1_uncompyle_tools.setVisible(False)
        self.uncompyle_button.setEnabled(False)
    
    def tab_change(self):
        if self.ui.left_tab.currentIndex() == 0:
            self.ui.tab2_step_2.setEnabled(False)
            self.ui.tab2_python_source.setEnabled(False)
            self.ui.tab2_download_python.setEnabled(False)
            self.ui.tab2_progress_bar.setEnabled(False)
            self.ui.tab2_wpsw_check.setEnabled(False)
            self.ui.tab2_custom_source_loc.setVisible(False)
            self.ui.tab2_step_3.setEnabled(False)
            self.ui.tab2_destination_loc.setEnabled(False)
            self.ui.tab2_extract_button.setEnabled(False)

            self.step_1 = self.ui.tab1_step_1
            self.pyc_loc = self.ui.tab1_pyc_loc
            self.step_2 = self.ui.tab1_step_2
            self.python_source = self.ui.tab1_python_source
            self.download_python = self.ui.tab1_download_python
            self.progress_bar = self.ui.tab1_progress_bar
            self.wpsw_check = self.ui.tab1_wpsw_check
            self.custom_source_loc = self.ui.tab1_custom_source_loc
            self.step_3 = self.ui.tab1_step_3
            self.destination_loc = self.ui.tab1_destination_loc
            self.uncompyle_button = self.ui.tab1_uncompyle_button

        else:
            self.ui.tab1_step_2.setEnabled(False)
            self.ui.tab1_python_source.setEnabled(False)
            self.ui.tab1_download_python.setEnabled(False)
            self.ui.tab1_progress_bar.setEnabled(False)
            self.ui.tab1_wpsw_check.setEnabled(False)
            self.ui.tab1_custom_source_loc.setVisible(False)
            self.ui.tab1_step_3.setEnabled(False)
            self.ui.tab1_destination_loc.setEnabled(False)
            self.ui.tab1_uncompyle_button.setEnabled(False)

            self.step_1 = self.ui.tab2_step_1
            self.pyc_loc = self.ui.tab2_pyc_loc
            self.step_2 = self.ui.tab2_step_2
            self.python_source = self.ui.tab2_python_source
            self.download_python = self.ui.tab2_download_python
            self.progress_bar = self.ui.tab2_progress_bar
            self.wpsw_check = self.ui.tab2_wpsw_check
            self.custom_source_loc = self.ui.tab2_custom_source_loc
            self.step_3 = self.ui.tab2_step_3
            self.destination_loc = self.ui.tab2_destination_loc
            self.uncompyle_button = self.ui.tab2_extract_button

    def getting_sources(self):
        self.ui.console_output.append("""Finding Python installations in \
system, please wait...""")
        self.installed_python = py_source.get_py()
        self.ui.tab1_step_1.setEnabled(True)
        self.ui.tab1_pyc_loc.setEnabled(True)
        self.ui.tab2_step_1.setEnabled(True)
        self.ui.tab2_pyc_loc.setEnabled(True)
        self.ui.console_output.append(f"""Finished. Found \
{len(self.installed_python)} installations""")


    def change_theme(self, theme):
        self.apply_stylesheet(self, theme[0], invert_secondary=theme[1])
        self.current_theme = theme

    def settings(self):
        settings_dialog = Settings()
        settings_dialog.apply_stylesheet(settings_dialog, self.current_theme[0],
        invert_secondary=self.current_theme[1])
        settings_dialog.theme_signal.connect(self.change_theme)
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
            self.python_source.setCurrentText(
                "Use currently installed python")
            self.ensure_disabled()
            self.step_2.setEnabled(True)
            self.python_source.setEnabled(True)
            self.download_python.setVisible(False)
            self.progress_bar.setVisible(False)
            self.wpsw_check.setVisible(False)
            self.custom_source_loc.setVisible(False)
            self.step_3.setEnabled(True)
            self.destination_loc.setEnabled(True)

                
        elif(bundled_PyVersion.startswith(self.py_v[0:3])):
            self.ui.console_output.append("""The version used in pyc bytecode \
doesn't match any installed Python or no Python installation found, but \
Python bundled with UnPYC matches it.""")

            self.ui.python_source.setCurrentText("Use UnPYC bundled python")
            self.ensure_disabled()
            self.step_2.setEnabled(True)
            self.python_source.setEnabled(True)
            self.download_python.setVisible(False)
            self.progress_bar.setVisible(False)
            self.step_3.setEnabled(True)
            self.destination_loc.setEnabled(True)


        else:
            if self.installed_python:
                self.ui.console_output.append("""Python installation found in \
system but doesn't match the version used in pyc bytecode magic number.
Press the Download button to download the portable Python or use a custom \
source.\nIt will look for previous downloads if any.\nTick the checkbox if \
you plan on using uncompile tools other than uncompyle6""")
            else:
                self.ui.console_output.append("""No python installation, download \
the required Python version or use a custom source.\nTick the checkbox if you \
plan on using uncompile tools other than uncompyle6""")
            
            self.python_source.setCurrentText(
                "Download portable python (recommended)")
            self.ensure_disabled()
            self.step_2.setEnabled(True)
            self.python_source.setEnabled(True)
            self.download_python.setVisible(True)
            self.progress_bar.setVisible(True)
            self.wpsw_check.setVisible(True)
            self.custom_source_loc.setVisible(False)
            self.download_python.setEnabled(True)
            self.progress_bar.setEnabled(True)
            self.wpsw_check.setEnabled(True)
            self.progress_bar.setTextVisible(True)



    def py_source_changed(self):
        index = self.python_source.currentIndex()
        if index == 0:
            self.ui.console_output.append("""Press the Download button to \
download the portable Python or use a custom source.\nIt will look for \
previous downloads if any\nTick the checkbox if you plan on using uncompile \
tools other than uncompyle6""")        
            self.ensure_disabled()
            self.step_2.setEnabled(True)
            self.python_source.setEnabled(True)
            self.download_python.setVisible(True)
            self.progress_bar.setVisible(True)
            self.wpsw_check.setVisible(True)
            self.download_python.setEnabled(True)
            self.progress_bar.setEnabled(True)
            self.wpsw_check.setEnabled(True)
            
        elif index == 1:
            if(not self.py_match):
                self.ui.console_output.append("""\nError: Installed Python \
version doesn't match pyc bytecode number""")      
                self.ensure_disabled()
                self.step_2.setEnabled(True)
                self.python_source.setEnabled(True)

            else:
                self.ensure_disabled()
                self.step_2.setEnabled(True)
                self.python_source.setEnabled(True)
                self.step_3.setEnabled(True)
                self.destination_loc.setEnabled(True)

        elif index == 2:
            if(bundled_PyVersion[0:3] != self.py_v[0:3]):
                self.ui.console_output.append("""\nError: Bundled Python \
version doesn't match pyc bytecode number""")
                self.ensure_disabled()
                self.step_2.setEnabled(True)
                self.python_source.setEnabled(True)

            else:
                self.ui.console_output.append("Not implemented yet")
            
        elif index == 3:
            self.ensure_disabled()
            self.download_python.setVisible(False)
            self.progress_bar.setVisible(False)
            self.wpsw_check.setVisible(False)
            self.step_2.setEnabled(True)
            self.python_source.setEnabled(True)
            self.custom_source_loc.setVisible(True)
            self.custom_source_loc.setEnabled(True)



    def open_pyc(self):
        self.ensure_disabled()
        try:
            if self.ui.left_tab.currentIndex() == 0:
                self.open_file = QtWidgets.QFileDialog.getOpenFileName(
                    self, "Open pyc/pyo file",
                    filter="Python bytecode(*.pyc *.pyo)")[0]
            else:
                self.open_file = QtWidgets.QFileDialog.getOpenFileName(
                    self, "Open pyinstaller executable file")[0]
            if(not self.open_file):
                raise FileNotFoundError

            self.pyc_loc.setText(self.open_file)
            self.destination_loc.setText("Destination folder")
            self.ui.console_output.setText("")

            if self.ui.left_tab.currentIndex() == 0:
                self.py_v = magic.get_magic(self.open_file)
            else:
                sys.argv = ["pyinstxtractor.py", self.open_file, None]
                self.py_v = pyinstxtractor.main()
            
            error_code = {"Error:1" : "Wrong magic number in the pyc bytecode",
                          "Error:2" : "Unknown python version",
                          "Error:3" : "File is not a python bytecode or is corrupt",
                          "Error:4" : "Unknown error",
                          None : ("File might not be pyinstaller file or it "
                                  + "might be corrupt")}
            
            if self.py_v in error_code:
                self.ui.console_output.append(error_code[self.py_v])
                self.ensure_disabled()
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
        if(self.ui.tab1_uncompyle_tool_label.isVisible()):
            self.ui.tab1_advanced.setText("Advanced ▶")
            self.ui.tab1_uncompyle_tool_label.setVisible(False)
            self.ui.tab1_uncompyle_tools.setVisible(False)
        else:
            self.ui.tab1_advanced.setText("Advanced ▾")
            self.ui.tab1_uncompyle_tool_label.setVisible(True)
            self.ui.tab1_uncompyle_tools.setVisible(True)

    def choose_tool(self):
        self.current = self.ui.tab1_uncompyle_tools.currentText()
        if(self.py_v[0:3] in ["3.9", "3.10"]):
            self.ui.console_output.append("""\nNo uncompile tool supports\
Python 3.9 or 3.10 currently.""")
            self.uncompyle_button.setEnabled(False)

        elif(self.py_v[0:3] in py_support[self.current]):
            self.ui.console_output.append("""\nThe uncompyle tool supports \
the pyc version.""")
            self.uncompyle_button.setEnabled(True)

        else:
            self.ui.console_output.append("""\nThis uncompile tool doesn't \
support the version used for the pyc""")
            self.uncompyle_button.setEnabled(False)

    def download_finish(self, return_value):
        if return_value[0]:
            if self.extract_thread is None:
                self.extract_thread = ExtractThread(*return_value[1:], self.py_v)
                self.extract_thread.ext_val.connect(self.progress_bar.setValue)
                self.extract_thread.finish.connect(self.extract_finish)
                self.extract_thread.console_message.connect(self.ui.console_output.append)
                self.extract_thread.start()
        else:
            self.download_thread = None

    def extract_finish(self, return_value):
        if return_value[0]:
            self.python_folder = return_value[1]
            self.python_binary = return_value[2]
            self.check_py_v(self.python_folder)
        self.download_thread = None
        self.extract_thread = None

    def down_then_extract(self):
        if (self.wpsw_check.isChecked()):
            url = portable_py_links[self.py_v[0:3]][1]
        else:
            url = portable_py_links[self.py_v[0:3]][0]
        if self.download_thread is None:
            self.download_thread = DownloadThread(url)
            self.download_thread.dw_val.connect(self.progress_bar.setValue)
            self.download_thread.finish.connect(self.download_finish)
            self.download_thread.console_message.connect(self.ui.console_output.append)
            self.download_thread.start()

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
                self.ui.console_output.append("""\nPython interpreter \
version matches pyc bytecode version.
Proceed to Step 3""")
                self.step_3.setEnabled(True)
                self.destination_loc.setEnabled(True)

            else:
                self.ui.console_output.append("""\nPython interpreter \
version does not matches pyc bytecode version.
Use another Python source""")
                self.step_3.setEnabled(False)
                self.destination_loc.setEnabled(False)

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
                self.destination_loc.setText(self.save_folder)
                if self.ui.left_tab.currentIndex() == 0:
                    self.ui.tab1_advanced.setVisible(True)
                self.uncompyle_button.setEnabled(True)

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
                self.custom_source_loc.setText(self.python_folder)
                self.check_py_v(self.python_folder)

        except FileNotFoundError:
            pass

    def uncompile(self):
        if self.ui.left_tab.currentIndex() == 0:
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
{self.python_binary} using {self.python_binary} -m pip install uncompyle6""")

        else:
            py_extractor_source = os.path.join(os.getcwd(), "modules",
                                               "pyinstxtractor.py")
            if(os.path.exists(py_extractor_source)):
                unc_command = (self.python_binary, [py_extractor_source,
                               self.open_file, self.save_folder])
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
win = Main()
qt_material.apply_stylesheet(app, theme="light_red.xml", invert_secondary=True)
win.show()
app.exec_()
