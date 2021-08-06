# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class ClickableLineEdit(QtWidgets.QLineEdit):
    clicked = QtCore.pyqtSignal()
    
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()
        else:
            super().mousePressEvent(event)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 518)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.console_output = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console_output.sizePolicy().hasHeightForWidth())
        self.console_output.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        self.console_output.setFont(font)
        self.console_output.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.console_output.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.console_output.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.console_output.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.console_output.setUndoRedoEnabled(False)
        self.console_output.setReadOnly(True)
        self.console_output.setObjectName("console_output")
        self.gridLayout.addWidget(self.console_output, 1, 1, 1, 1)
        self.heading = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(40)
        self.heading.setFont(font)
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.gridLayout.addWidget(self.heading, 0, 0, 1, 2)
        self.left_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.left_tab.setObjectName("left_tab")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tab1_step_1 = QtWidgets.QLabel(self.tab1)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab1_step_1.setFont(font)
        self.tab1_step_1.setObjectName("tab1_step_1")
        self.horizontalLayout_6.addWidget(self.tab1_step_1)
        self.tab1_pyc_loc = ClickableLineEdit(self.tab1)
        self.tab1_pyc_loc.setReadOnly(True)
        self.tab1_pyc_loc.setObjectName("tab1_pyc_loc")
        self.horizontalLayout_6.addWidget(self.tab1_pyc_loc)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tab1_step_2 = QtWidgets.QLabel(self.tab1)
        self.tab1_step_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab1_step_2.setFont(font)
        self.tab1_step_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tab1_step_2.setObjectName("tab1_step_2")
        self.horizontalLayout_3.addWidget(self.tab1_step_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab1_python_source = QtWidgets.QComboBox(self.tab1)
        self.tab1_python_source.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1_python_source.sizePolicy().hasHeightForWidth())
        self.tab1_python_source.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab1_python_source.setFont(font)
        self.tab1_python_source.setObjectName("tab1_python_source")
        self.tab1_python_source.addItem("")
        self.tab1_python_source.addItem("")
        self.tab1_python_source.addItem("")
        self.tab1_python_source.addItem("")
        self.verticalLayout.addWidget(self.tab1_python_source)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tab1_download_python = QtWidgets.QPushButton(self.tab1)
        self.tab1_download_python.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab1_download_python.setFont(font)
        self.tab1_download_python.setObjectName("tab1_download_python")
        self.horizontalLayout.addWidget(self.tab1_download_python)
        self.tab1_progress_bar = QtWidgets.QProgressBar(self.tab1)
        self.tab1_progress_bar.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab1_progress_bar.setFont(font)
        self.tab1_progress_bar.setProperty("value", 0)
        self.tab1_progress_bar.setTextVisible(True)
        self.tab1_progress_bar.setInvertedAppearance(False)
        self.tab1_progress_bar.setObjectName("tab1_progress_bar")
        self.horizontalLayout.addWidget(self.tab1_progress_bar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tab1_wpsw_check = QtWidgets.QCheckBox(self.tab1)
        self.tab1_wpsw_check.setEnabled(False)
        self.tab1_wpsw_check.setObjectName("tab1_wpsw_check")
        self.verticalLayout.addWidget(self.tab1_wpsw_check)
        self.tab1_custom_source_loc = ClickableLineEdit(self.tab1)
        self.tab1_custom_source_loc.setEnabled(False)
        self.tab1_custom_source_loc.setReadOnly(True)
        self.tab1_custom_source_loc.setObjectName("tab1_custom_source_loc")
        self.verticalLayout.addWidget(self.tab1_custom_source_loc)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tab1_step_3 = QtWidgets.QLabel(self.tab1)
        self.tab1_step_3.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab1_step_3.setFont(font)
        self.tab1_step_3.setObjectName("tab1_step_3")
        self.horizontalLayout_2.addWidget(self.tab1_step_3)
        self.tab1_destination_loc = ClickableLineEdit(self.tab1)
        self.tab1_destination_loc.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab1_destination_loc.setFont(font)
        self.tab1_destination_loc.setReadOnly(True)
        self.tab1_destination_loc.setObjectName("tab1_destination_loc")
        self.horizontalLayout_2.addWidget(self.tab1_destination_loc)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.advanced_container = QtWidgets.QVBoxLayout()
        self.advanced_container.setObjectName("advanced_container")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tab1_advanced = QtWidgets.QPushButton(self.tab1)
        self.tab1_advanced.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab1_advanced.setFont(font)
        self.tab1_advanced.setFlat(True)
        self.tab1_advanced.setObjectName("tab1_advanced")
        self.horizontalLayout_5.addWidget(self.tab1_advanced)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.advanced_container.addLayout(self.horizontalLayout_5)
        self.widget = QtWidgets.QWidget(self.tab1)
        self.widget.setEnabled(True)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tab1_uncompyle_tool_label = QtWidgets.QLabel(self.widget)
        self.tab1_uncompyle_tool_label.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab1_uncompyle_tool_label.setFont(font)
        self.tab1_uncompyle_tool_label.setObjectName("tab1_uncompyle_tool_label")
        self.horizontalLayout_4.addWidget(self.tab1_uncompyle_tool_label)
        self.tab1_uncompyle_tools = QtWidgets.QComboBox(self.widget)
        self.tab1_uncompyle_tools.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1_uncompyle_tools.sizePolicy().hasHeightForWidth())
        self.tab1_uncompyle_tools.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab1_uncompyle_tools.setFont(font)
        self.tab1_uncompyle_tools.setObjectName("tab1_uncompyle_tools")
        self.tab1_uncompyle_tools.addItem("")
        self.tab1_uncompyle_tools.addItem("")
        self.tab1_uncompyle_tools.addItem("")
        self.tab1_uncompyle_tools.addItem("")
        self.tab1_uncompyle_tools.addItem("")
        self.tab1_uncompyle_tools.addItem("")
        self.tab1_uncompyle_tools.addItem("")
        self.tab1_uncompyle_tools.addItem("")
        self.horizontalLayout_4.addWidget(self.tab1_uncompyle_tools)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.advanced_container.addWidget(self.widget)
        self.verticalLayout_3.addLayout(self.advanced_container)
        spacerItem1 = QtWidgets.QSpacerItem(20, 56, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.tab1_uncompyle_button = QtWidgets.QPushButton(self.tab1)
        self.tab1_uncompyle_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab1_uncompyle_button.setFont(font)
        self.tab1_uncompyle_button.setObjectName("tab1_uncompyle_button")
        self.horizontalLayout_7.addWidget(self.tab1_uncompyle_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.left_tab.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.tab2_step_1 = QtWidgets.QLabel(self.tab2)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab2_step_1.setFont(font)
        self.tab2_step_1.setObjectName("tab2_step_1")
        self.horizontalLayout_11.addWidget(self.tab2_step_1)
        self.tab2_pyc_loc = ClickableLineEdit(self.tab2)
        self.tab2_pyc_loc.setReadOnly(True)
        self.tab2_pyc_loc.setObjectName("tab2_pyc_loc")
        self.horizontalLayout_11.addWidget(self.tab2_pyc_loc)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.tab2_step_2 = QtWidgets.QLabel(self.tab2)
        self.tab2_step_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab2_step_2.setFont(font)
        self.tab2_step_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.tab2_step_2.setObjectName("tab2_step_2")
        self.horizontalLayout_12.addWidget(self.tab2_step_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tab2_python_source = QtWidgets.QComboBox(self.tab2)
        self.tab2_python_source.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab2_python_source.sizePolicy().hasHeightForWidth())
        self.tab2_python_source.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab2_python_source.setFont(font)
        self.tab2_python_source.setObjectName("tab2_python_source")
        self.tab2_python_source.addItem("")
        self.tab2_python_source.addItem("")
        self.tab2_python_source.addItem("")
        self.tab2_python_source.addItem("")
        self.verticalLayout_4.addWidget(self.tab2_python_source)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.tab2_download_python = QtWidgets.QPushButton(self.tab2)
        self.tab2_download_python.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab2_download_python.setFont(font)
        self.tab2_download_python.setObjectName("tab2_download_python")
        self.horizontalLayout_10.addWidget(self.tab2_download_python)
        self.tab2_progress_bar = QtWidgets.QProgressBar(self.tab2)
        self.tab2_progress_bar.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab2_progress_bar.setFont(font)
        self.tab2_progress_bar.setProperty("value", 0)
        self.tab2_progress_bar.setTextVisible(True)
        self.tab2_progress_bar.setInvertedAppearance(False)
        self.tab2_progress_bar.setObjectName("tab2_progress_bar")
        self.horizontalLayout_10.addWidget(self.tab2_progress_bar)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.tab2_wpsw_check = QtWidgets.QCheckBox(self.tab2)
        self.tab2_wpsw_check.setEnabled(False)
        self.tab2_wpsw_check.setObjectName("tab2_wpsw_check")
        self.verticalLayout_4.addWidget(self.tab2_wpsw_check)
        self.tab2_custom_source_loc = ClickableLineEdit(self.tab2)
        self.tab2_custom_source_loc.setEnabled(False)
        self.tab2_custom_source_loc.setReadOnly(True)
        self.tab2_custom_source_loc.setObjectName("tab2_custom_source_loc")
        self.verticalLayout_4.addWidget(self.tab2_custom_source_loc)
        self.horizontalLayout_12.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tab2_step_3 = QtWidgets.QLabel(self.tab2)
        self.tab2_step_3.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab2_step_3.setFont(font)
        self.tab2_step_3.setObjectName("tab2_step_3")
        self.horizontalLayout_8.addWidget(self.tab2_step_3)
        self.tab2_destination_loc = ClickableLineEdit(self.tab2)
        self.tab2_destination_loc.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab2_destination_loc.setFont(font)
        self.tab2_destination_loc.setReadOnly(True)
        self.tab2_destination_loc.setObjectName("tab2_destination_loc")
        self.horizontalLayout_8.addWidget(self.tab2_destination_loc)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        spacerItem4 = QtWidgets.QSpacerItem(20, 138, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.tab2_extract_button = QtWidgets.QPushButton(self.tab2)
        self.tab2_extract_button.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(10)
        self.tab2_extract_button.setFont(font)
        self.tab2_extract_button.setObjectName("tab2_extract_button")
        self.horizontalLayout_9.addWidget(self.tab2_extract_button)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.left_tab.addTab(self.tab2, "")
        self.gridLayout.addWidget(self.left_tab, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 21))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionHow_to_use = QtWidgets.QAction(MainWindow)
        self.actionHow_to_use.setObjectName("actionHow_to_use")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuSettings.addAction(self.actionSettings)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.left_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UnPYC"))
        self.heading.setText(_translate("MainWindow", "UnPYC"))
        self.tab1_step_1.setText(_translate("MainWindow", "Step 1"))
        self.tab1_pyc_loc.setText(_translate("MainWindow", "Location of the .pyc or .pyo file"))
        self.tab1_step_2.setText(_translate("MainWindow", "Step 2"))
        self.tab1_python_source.setItemText(0, _translate("MainWindow", "Download portable python (recommended)"))
        self.tab1_python_source.setItemText(1, _translate("MainWindow", "Use currently installed python"))
        self.tab1_python_source.setItemText(2, _translate("MainWindow", "Use UnPYC bundled python"))
        self.tab1_python_source.setItemText(3, _translate("MainWindow", "Custom source (advanced)"))
        self.tab1_download_python.setText(_translate("MainWindow", "Download"))
        self.tab1_wpsw_check.setText(_translate("MainWindow", "Download the wpsw wu6 version"))
        self.tab1_custom_source_loc.setText(_translate("MainWindow", "Custom Python source"))
        self.tab1_step_3.setText(_translate("MainWindow", "Step 3"))
        self.tab1_destination_loc.setText(_translate("MainWindow", "Destination file"))
        self.tab1_advanced.setText(_translate("MainWindow", "Advanced ▶"))
        self.tab1_uncompyle_tool_label.setText(_translate("MainWindow", "Uncompile tool"))
        self.tab1_uncompyle_tools.setItemText(0, _translate("MainWindow", "rocky/uncompyle6 (1.0-3.8) (default)"))
        self.tab1_uncompyle_tools.setItemText(1, _translate("MainWindow", "zrax/pycdc (2.7 - 3.3)"))
        self.tab1_uncompyle_tools.setItemText(2, _translate("MainWindow", "rocky/decompile3 (3.7+)"))
        self.tab1_uncompyle_tools.setItemText(3, _translate("MainWindow", "wibiti/uncompyle2 (2.7)"))
        self.tab1_uncompyle_tools.setItemText(4, _translate("MainWindow", "figment/unpyc3 (3.3)"))
        self.tab1_uncompyle_tools.setItemText(5, _translate("MainWindow", "andrew-tavera/unpyc37 (3.7)"))
        self.tab1_uncompyle_tools.setItemText(6, _translate("MainWindow", "unpyc3 (3.2)"))
        self.tab1_uncompyle_tools.setItemText(7, _translate("MainWindow", "gtarnberger/uncompyle (2.7)"))
        self.tab1_uncompyle_button.setText(_translate("MainWindow", "Umcompyle!"))
        self.left_tab.setTabText(self.left_tab.indexOf(self.tab1), _translate("MainWindow", ".pyc/.pyo file"))
        self.tab2_step_1.setText(_translate("MainWindow", "Step 1"))
        self.tab2_pyc_loc.setText(_translate("MainWindow", "Location of Pyinstaller packaged file"))
        self.tab2_step_2.setText(_translate("MainWindow", "Step 2"))
        self.tab2_python_source.setItemText(0, _translate("MainWindow", "Download portable python (recommended)"))
        self.tab2_python_source.setItemText(1, _translate("MainWindow", "Use currently installed python"))
        self.tab2_python_source.setItemText(2, _translate("MainWindow", "Use UnPYC bundled python"))
        self.tab2_python_source.setItemText(3, _translate("MainWindow", "Custom source (advanced)"))
        self.tab2_download_python.setText(_translate("MainWindow", "Download"))
        self.tab2_wpsw_check.setText(_translate("MainWindow", "Download the wpsw wu6 version"))
        self.tab2_custom_source_loc.setText(_translate("MainWindow", "Custom Python source"))
        self.tab2_step_3.setText(_translate("MainWindow", "Step 3"))
        self.tab2_destination_loc.setText(_translate("MainWindow", "Destination folder"))
        self.tab2_extract_button.setText(_translate("MainWindow", "Extract!"))
        self.left_tab.setTabText(self.left_tab.indexOf(self.tab2), _translate("MainWindow", "Pyinstaller file"))
        self.menuSettings.setTitle(_translate("MainWindow", "Tools"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionHow_to_use.setText(_translate("MainWindow", "How to use"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
