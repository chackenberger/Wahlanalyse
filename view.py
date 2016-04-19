# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WahlAnalyse_GUI.ui'
#
# Created: Tue Apr 19 08:59:32 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 563)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuWindows = QtGui.QMenu(self.menubar)
        self.menuWindows.setObjectName("menuWindows")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionNew.setObjectName("actionNew")
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionCopy.setObjectName("actionCopy")
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionClose.setObjectName("actionClose")
        self.actionAdd_Row = QtGui.QAction(MainWindow)
        self.actionAdd_Row.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionAdd_Row.setObjectName("actionAdd_Row")
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete_Row = QtGui.QAction(MainWindow)
        self.actionDelete_Row.setObjectName("actionDelete_Row")
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setCheckable(True)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(MainWindow)
        self.actionRedo.setCheckable(True)
        self.actionRedo.setObjectName("actionRedo")
        self.actionSave_DB = QtGui.QAction(MainWindow)
        self.actionSave_DB.setObjectName("actionSave_DB")
        self.actionOpen_DB = QtGui.QAction(MainWindow)
        self.actionOpen_DB.setObjectName("actionOpen_DB")
        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionDuplicate_Row = QtGui.QAction(MainWindow)
        self.actionDuplicate_Row.setObjectName("actionDuplicate_Row")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionAdd_Row)
        self.menuEdit.addAction(self.actionDelete_Row)
        self.menuEdit.addAction(self.actionDuplicate_Row)
        self.menuWindows.addAction(self.actionSave_DB)
        self.menuWindows.addAction(self.actionOpen_DB)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "WahlAnalyse", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuWindows.setTitle(QtGui.QApplication.translate("MainWindow", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setStatusTip(QtGui.QApplication.translate("MainWindow", "Open File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setStatusTip(QtGui.QApplication.translate("MainWindow", "Save File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("MainWindow", "Save as...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setStatusTip(QtGui.QApplication.translate("MainWindow", "Save File as...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create New File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setStatusTip(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setStatusTip(QtGui.QApplication.translate("MainWindow", "Close Program", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setShortcut(QtGui.QApplication.translate("MainWindow", "Meta+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Row.setText(QtGui.QApplication.translate("MainWindow", "Add Row", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Row.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add new Row", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setStatusTip(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Row.setText(QtGui.QApplication.translate("MainWindow", "Delete Rows", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Row.setStatusTip(QtGui.QApplication.translate("MainWindow", "Delete Row", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setText(QtGui.QApplication.translate("MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setStatusTip(QtGui.QApplication.translate("MainWindow", "Undo last Action", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setText(QtGui.QApplication.translate("MainWindow", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setStatusTip(QtGui.QApplication.translate("MainWindow", "Redo last Action", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_DB.setText(QtGui.QApplication.translate("MainWindow", "Save to Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_DB.setStatusTip(QtGui.QApplication.translate("MainWindow", "Save data to Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_DB.setText(QtGui.QApplication.translate("MainWindow", "Open from Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setStatusTip(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDuplicate_Row.setText(QtGui.QApplication.translate("MainWindow", "Duplicate Row", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDuplicate_Row.setStatusTip(QtGui.QApplication.translate("MainWindow", "Duplicate Row and insert after", None, QtGui.QApplication.UnicodeUTF8))

