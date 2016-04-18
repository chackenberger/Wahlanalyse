# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'load_db.ui'
#
# Created: Sun Apr 17 20:57:51 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_load_db(object):
    def setupUi(self, load_db):
        load_db.setObjectName("load_db")
        load_db.resize(400, 132)
        self.buttonBox = QtGui.QDialogButtonBox(load_db)
        self.buttonBox.setGeometry(QtCore.QRect(30, 90, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtGui.QWidget(load_db)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.dateList = QtGui.QComboBox(self.verticalLayoutWidget)
        self.dateList.setObjectName("dateList")
        self.verticalLayout.addWidget(self.dateList)

        self.retranslateUi(load_db)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), load_db.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), load_db.reject)
        QtCore.QMetaObject.connectSlotsByName(load_db)

    def retranslateUi(self, load_db):
        load_db.setWindowTitle(QtGui.QApplication.translate("load_db", "Load from Database", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("load_db", "Choose an election", None, QtGui.QApplication.UnicodeUTF8))

