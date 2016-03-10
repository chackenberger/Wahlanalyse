# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_db.ui'
#
# Created: Thu Mar 10 10:30:10 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_saveDB(object):
    def setupUi(self, saveDB):
        saveDB.setObjectName("saveDB")
        saveDB.resize(400, 300)
        self.verticalLayout_2 = QtGui.QVBoxLayout(saveDB)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(saveDB)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.calendarWidget = QtGui.QCalendarWidget(saveDB)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(saveDB)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(saveDB)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), saveDB.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), saveDB.reject)
        QtCore.QMetaObject.connectSlotsByName(saveDB)

    def retranslateUi(self, saveDB):
        saveDB.setWindowTitle(QtGui.QApplication.translate("saveDB", "Save to Database", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("saveDB", "Pick the date of the election", None, QtGui.QApplication.UnicodeUTF8))

