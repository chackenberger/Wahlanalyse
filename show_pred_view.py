# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_pred_view.ui'
#
# Created: Tue Apr 19 21:48:51 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_show_prediction(object):
    def setupUi(self, show_prediction):
        show_prediction.setObjectName("show_prediction")
        show_prediction.resize(598, 408)
        self.verticalLayout = QtGui.QVBoxLayout(show_prediction)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(show_prediction)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.hrdesc = QtGui.QLabel(show_prediction)
        self.hrdesc.setObjectName("hrdesc")
        self.verticalLayout.addWidget(self.hrdesc)
        self.tableView = QtGui.QTableView(show_prediction)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.pushButton = QtGui.QPushButton(show_prediction)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(show_prediction)
        self.pushButton.pressed.connect(show_prediction.accept)
        QtCore.QMetaObject.connectSlotsByName(show_prediction)

    def retranslateUi(self, show_prediction):
        show_prediction.setWindowTitle(QtGui.QApplication.translate("show_prediction", "Show Prediction", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("show_prediction", "Hochrechnung:", None, QtGui.QApplication.UnicodeUTF8))
        self.hrdesc.setText(QtGui.QApplication.translate("show_prediction", "1.1.1900 at 18:00", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("show_prediction", "OK", None, QtGui.QApplication.UnicodeUTF8))

