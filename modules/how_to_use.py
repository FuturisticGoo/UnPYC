# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'how_to_use.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HowToUse(object):
    def setupUi(self, HowToUse):
        HowToUse.setObjectName("HowToUse")
        HowToUse.resize(292, 228)
        self.verticalLayout = QtWidgets.QVBoxLayout(HowToUse)
        self.verticalLayout.setObjectName("verticalLayout")
        self.help_text = QtWidgets.QTextEdit(HowToUse)
        self.help_text.setReadOnly(True)
        self.help_text.setObjectName("help_text")
        self.verticalLayout.addWidget(self.help_text)

        self.retranslateUi(HowToUse)
        QtCore.QMetaObject.connectSlotsByName(HowToUse)

    def retranslateUi(self, HowToUse):
        _translate = QtCore.QCoreApplication.translate
        HowToUse.setWindowTitle(_translate("HowToUse", "How to use"))
