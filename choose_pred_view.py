# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose_pred_view.ui'
#
# Created: Tue Apr 19 21:36:57 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_choose_prediction(object):
    def setupUi(self, choose_prediction):
        choose_prediction.setObjectName("choose_prediction")
        choose_prediction.resize(400, 132)
        self.buttonBox = QtGui.QDialogButtonBox(choose_prediction)
        self.buttonBox.setGeometry(QtCore.QRect(30, 90, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtGui.QWidget(choose_prediction)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)

        self.retranslateUi(choose_prediction)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), choose_prediction.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), choose_prediction.reject)
        QtCore.QMetaObject.connectSlotsByName(choose_prediction)

    def retranslateUi(self, choose_prediction):
        choose_prediction.setWindowTitle(QtGui.QApplication.translate("choose_prediction", "Choose Prediction", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("choose_prediction", "Choose Prediction", None, QtGui.QApplication.UnicodeUTF8))

