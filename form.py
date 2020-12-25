# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(701, 493)
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_8 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.heading = QLabel(self.centralwidget)
        self.heading.setObjectName(u"heading")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(40)
        self.heading.setFont(font1)
        self.heading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.heading)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.step_1 = QLabel(self.centralwidget)
        self.step_1.setObjectName(u"step_1")
        font2 = QFont()
        font2.setFamily(u"Roboto Thin")
        font2.setPointSize(10)
        self.step_1.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.step_1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pyc_loc = QLineEdit(self.centralwidget)
        self.pyc_loc.setObjectName(u"pyc_loc")

        self.horizontalLayout_2.addWidget(self.pyc_loc)

        self.open_pyc_file = QPushButton(self.centralwidget)
        self.open_pyc_file.setObjectName(u"open_pyc_file")
        self.open_pyc_file.setFont(font2)

        self.horizontalLayout_2.addWidget(self.open_pyc_file)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.step_2 = QLabel(self.centralwidget)
        self.step_2.setObjectName(u"step_2")
        self.step_2.setEnabled(True)
        self.step_2.setFont(font2)
        self.step_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.step_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.python_source = QComboBox(self.centralwidget)
        self.python_source.addItem("")
        self.python_source.addItem("")
        self.python_source.addItem("")
        self.python_source.addItem("")
        self.python_source.setObjectName(u"python_source")
        self.python_source.setEnabled(True)
        self.python_source.setFont(font2)

        self.verticalLayout.addWidget(self.python_source)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.download_python = QPushButton(self.centralwidget)
        self.download_python.setObjectName(u"download_python")
        self.download_python.setEnabled(True)
        self.download_python.setFont(font2)

        self.horizontalLayout.addWidget(self.download_python)

        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setEnabled(True)
        self.progress_bar.setFont(font2)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setInvertedAppearance(False)

        self.horizontalLayout.addWidget(self.progress_bar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.custom_source_loc = QLineEdit(self.centralwidget)
        self.custom_source_loc.setObjectName(u"custom_source_loc")

        self.horizontalLayout_6.addWidget(self.custom_source_loc)

        self.source_button = QPushButton(self.centralwidget)
        self.source_button.setObjectName(u"source_button")

        self.horizontalLayout_6.addWidget(self.source_button)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.verticalLayout)

        self.step_3 = QLabel(self.centralwidget)
        self.step_3.setObjectName(u"step_3")
        self.step_3.setEnabled(True)
        self.step_3.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.step_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.destination_loc = QLineEdit(self.centralwidget)
        self.destination_loc.setObjectName(u"destination_loc")
        self.destination_loc.setEnabled(True)
        self.destination_loc.setFont(font2)

        self.horizontalLayout_3.addWidget(self.destination_loc)

        self.save_as = QPushButton(self.centralwidget)
        self.save_as.setObjectName(u"save_as")
        self.save_as.setEnabled(True)
        self.save_as.setFont(font2)

        self.horizontalLayout_3.addWidget(self.save_as)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.advanced_container = QVBoxLayout()
        self.advanced_container.setObjectName(u"advanced_container")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.advanced = QPushButton(self.centralwidget)
        self.advanced.setObjectName(u"advanced")
        self.advanced.setEnabled(True)
        self.advanced.setFont(font2)
        self.advanced.setFlat(True)

        self.horizontalLayout_5.addWidget(self.advanced)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.advanced_container.addLayout(self.horizontalLayout_5)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.uncompyle_tool_label = QLabel(self.widget)
        self.uncompyle_tool_label.setObjectName(u"uncompyle_tool_label")
        self.uncompyle_tool_label.setEnabled(True)
        self.uncompyle_tool_label.setFont(font2)

        self.horizontalLayout_4.addWidget(self.uncompyle_tool_label)

        self.uncompyle_tools = QComboBox(self.widget)
        self.uncompyle_tools.addItem("")
        self.uncompyle_tools.addItem("")
        self.uncompyle_tools.addItem("")
        self.uncompyle_tools.addItem("")
        self.uncompyle_tools.addItem("")
        self.uncompyle_tools.addItem("")
        self.uncompyle_tools.addItem("")
        self.uncompyle_tools.addItem("")
        self.uncompyle_tools.setObjectName(u"uncompyle_tools")
        self.uncompyle_tools.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uncompyle_tools.sizePolicy().hasHeightForWidth())
        self.uncompyle_tools.setSizePolicy(sizePolicy)
        self.uncompyle_tools.setFont(font2)

        self.horizontalLayout_4.addWidget(self.uncompyle_tools)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.advanced_container.addWidget(self.widget)


        self.verticalLayout_3.addLayout(self.advanced_container)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.space_left_uncompyle = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.space_left_uncompyle)

        self.uncompyle_button = QPushButton(self.centralwidget)
        self.uncompyle_button.setObjectName(u"uncompyle_button")
        self.uncompyle_button.setEnabled(True)
        self.uncompyle_button.setFont(font2)

        self.horizontalLayout_7.addWidget(self.uncompyle_button)

        self.space_right_uncompyle = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.space_right_uncompyle)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_8.addLayout(self.verticalLayout_3)

        self.console_output = QTextEdit(self.centralwidget)
        self.console_output.setObjectName(u"console_output")
        font3 = QFont()
        font3.setFamily(u"Terminal")
        font3.setPointSize(12)
        self.console_output.setFont(font3)
        self.console_output.setFrameShape(QFrame.StyledPanel)
        self.console_output.setFrameShadow(QFrame.Sunken)
        self.console_output.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.console_output.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.console_output.setUndoRedoEnabled(False)
        self.console_output.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.console_output)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 701, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"UnPYC", None))
        self.heading.setText(QCoreApplication.translate("MainWindow", u"UnPYC", None))
        self.step_1.setText(QCoreApplication.translate("MainWindow", u"Step 1", None))
        self.open_pyc_file.setText(QCoreApplication.translate("MainWindow", u"Open .pyc file", None))
        self.step_2.setText(QCoreApplication.translate("MainWindow", u"Step 2", None))
        self.python_source.setItemText(0, QCoreApplication.translate("MainWindow", u"Download portable python (recommended)", None))
        self.python_source.setItemText(1, QCoreApplication.translate("MainWindow", u"Use currently installed python", None))
        self.python_source.setItemText(2, QCoreApplication.translate("MainWindow", u"Use UnPYC bundled python", None))
        self.python_source.setItemText(3, QCoreApplication.translate("MainWindow", u"Custom source (advanced)", None))

        self.download_python.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.source_button.setText(QCoreApplication.translate("MainWindow", u"Python Source", None))
        self.step_3.setText(QCoreApplication.translate("MainWindow", u"Step 3", None))
        self.destination_loc.setText(QCoreApplication.translate("MainWindow", u"Destination file", None))
        self.save_as.setText(QCoreApplication.translate("MainWindow", u"Save in folder", None))
        self.advanced.setText(QCoreApplication.translate("MainWindow", u"Advanced \u25b6", None))
        self.uncompyle_tool_label.setText(QCoreApplication.translate("MainWindow", u"Uncompile tool", None))
        self.uncompyle_tools.setItemText(0, QCoreApplication.translate("MainWindow", u"rocky/uncompyle6 (1.0-3.8) (default)", None))
        self.uncompyle_tools.setItemText(1, QCoreApplication.translate("MainWindow", u"zrax/pycdc (2.7 - 3.3)", None))
        self.uncompyle_tools.setItemText(2, QCoreApplication.translate("MainWindow", u"rocky/decompile3 (3.7+)", None))
        self.uncompyle_tools.setItemText(3, QCoreApplication.translate("MainWindow", u"wibiti/uncompyle2 (2.7)", None))
        self.uncompyle_tools.setItemText(4, QCoreApplication.translate("MainWindow", u"figment/unpyc3 (3.3)", None))
        self.uncompyle_tools.setItemText(5, QCoreApplication.translate("MainWindow", u"andrew-tavera/unpyc37 (3.7)", None))
        self.uncompyle_tools.setItemText(6, QCoreApplication.translate("MainWindow", u"unpyc3 (3.2)", None))
        self.uncompyle_tools.setItemText(7, QCoreApplication.translate("MainWindow", u"gtarnberger/uncompyle (2.7)", None))

        self.uncompyle_button.setText(QCoreApplication.translate("MainWindow", u"Umcompyle!", None))
    # retranslateUi

