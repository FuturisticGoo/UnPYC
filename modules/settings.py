# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(285, 131)
        self.gridLayout = QtWidgets.QGridLayout(Settings)
        self.gridLayout.setObjectName("gridLayout")
        self.clear_label = QtWidgets.QLabel(Settings)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clear_label.setFont(font)
        self.clear_label.setObjectName("clear_label")
        self.gridLayout.addWidget(self.clear_label, 0, 0, 1, 1)
        self.clear_button = QtWidgets.QPushButton(Settings)
        self.clear_button.setObjectName("clear_button")
        self.gridLayout.addWidget(self.clear_button, 0, 1, 1, 1)
        self.theme_label = QtWidgets.QLabel(Settings)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.theme_label.setFont(font)
        self.theme_label.setObjectName("theme_label")
        self.gridLayout.addWidget(self.theme_label, 1, 0, 1, 1)
        self.theme_combo = QtWidgets.QComboBox(Settings)
        self.theme_combo.setObjectName("theme_combo")
        self.gridLayout.addWidget(self.theme_combo, 1, 1, 1, 1)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        self.clear_label.setText(_translate("Settings", "Clear Portable Python Folder"))
        self.clear_button.setText(_translate("Settings", "Clear"))
        self.theme_label.setText(_translate("Settings", "Change Theme"))
