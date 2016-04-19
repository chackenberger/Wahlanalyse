# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_pred_view.ui'
#
# Created: Tue Apr 19 21:36:37 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_create_prediction(object):
    def setupUi(self, create_prediction):
        create_prediction.setObjectName("create_prediction")
        create_prediction.resize(400, 192)
        self.buttonBox = QtGui.QDialogButtonBox(create_prediction)
        self.buttonBox.setGeometry(QtCore.QRect(30, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtGui.QWidget(create_prediction)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 131))
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
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.timeEdit = QtGui.QTimeEdit(self.verticalLayoutWidget)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)

        self.retranslateUi(create_prediction)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), create_prediction.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), create_prediction.reject)
        QtCore.QMetaObject.connectSlotsByName(create_prediction)

    def retranslateUi(self, create_prediction):
        create_prediction.setWindowTitle(QtGui.QApplication.translate("create_prediction", "Create Prediction", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("create_prediction", "Choose Election", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("create_prediction", "Set Time of Prediction", None, QtGui.QApplication.UnicodeUTF8))

