from view import Ui_MainWindow
from PySide.QtGui import QApplication, QMainWindow, QFileDialog, QUndoStack
import sys
from save_db import SaveToDBDialog
from load_db import LoadFromDBDialog
from create_pred import CreatePredDialog
from choose_pred import ChoosePredDialog
from show_pred import ShowPredDialog

from csvutil import CSVUtil
from dicttablemodel import DictTableModel
from dbconnection import DBConnection
from itemdeleg import ItemDelegate
from commands import *


class WahlAnalyse(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.undoStack = QUndoStack()

        self.db = DBConnection("172.16.6.137", "root", "password", "wahl")

        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.gui.actionOpen.triggered.connect(self.open_file)
        self.gui.actionSave.triggered.connect(self.save_file)
        self.gui.actionSave_as.triggered.connect(self.save_file_as)
        self.gui.actionNew.triggered.connect(self.new_file)
        self.gui.actionCopy.triggered.connect(self.copy_cs)
        self.gui.actionAdd_Row.triggered.connect(self.add_rows)
        self.gui.actionSave_DB.triggered.connect(self.open_save_db)
        self.gui.actionOpen_DB.triggered.connect(self.open_load_db)
        self.gui.actionPaste.triggered.connect(self.paste)
        self.gui.actionCut.triggered.connect(self.cut)
        self.gui.actionDelete_Row.triggered.connect(self.remove_rows)
        self.gui.actionDuplicate_Row.triggered.connect(self.duplicate)
        self.gui.actionUndo.triggered.connect(self.undo)
        self.gui.actionRedo.triggered.connect(self.redo)
        self.gui.actionCreate_Prediction.triggered.connect(self.open_create_pred)
        self.gui.actionShow_Prediction.triggered.connect(self.open_choose_pred)

        self.gui.tableView.setSortingEnabled(True)
        self.gui.tableView.setItemDelegate(ItemDelegate(self.undoStack, self.set_unrdo_text))

        self.tbm = DictTableModel(data=[], header=[], parent=self)

        self.sdb_dialog = SaveToDBDialog(self)
        self.ldb_dialog = LoadFromDBDialog(self)
        self.create_pred_dialog = CreatePredDialog(self)
        self.choose_pred_dialog = ChoosePredDialog(self)
        self.show_pred_dialog = ShowPredDialog(self)

        self.file = "."

    def open_file(self):
        self.file = QFileDialog.getOpenFileName(self, "Choose File", filter="CSV-File (*.csv)")[0]
        if self.file != '':
            data, header = CSVUtil.read(self.file)
            self.tbm.set_data(data, header)
            self.gui.tableView.reset()
            self.gui.tableView.setModel(self.tbm)

    def save_file(self):
        if self.file != '' and self.file is not None:
            CSVUtil.write(self.file, self.tbm.get_data())

    def save_file_as(self):
        self.file = QFileDialog.getSaveFileName(self, "CSV-Datei speichern", dir=self.file, filter="CSV-Datei (*.csv)")[
            0]
        if self.file != '':
            self.save_file()

    def new_file(self):
        self.file = "."
        self.tbm.set_data([], [])
        self.gui.tableView.reset()
        self.gui.tableView.setModel(self.tbm)
        self.undoStack.clear()
        self.set_unrdo_text()

    def copy_cs(self):
        if len(self.gui.tableView.selectionModel().selectedIndexes()) == 0:
            return

        clipboard = QApplication.clipboard()
        selected_index = self.gui.tableView.selectionModel().selectedIndexes()[0]
        selected_text = str(self.tbm.data(selected_index))
        clipboard.setText(selected_text)

    def save_data_db(self, date):
        self.db.write_data(self.tbm.get_data(), date)

    def load_data_db(self, date):
        data, header = self.db.read_data(date)
        self.tbm.set_data(data, header)
        self.gui.tableView.reset()
        self.gui.tableView.setModel(self.tbm)
        self.undoStack.clear()
        self.set_unrdo_text()

    def create_prediction(self, termin, time):
        self.db.create_prediction(termin, time)

    def open_save_db(self):
        self.setDisabled(True)
        self.sdb_dialog.setEnabled(True)
        self.sdb_dialog.show()

    def open_load_db(self):
        self.ldb_dialog.update_dates(self.db.get_termine())
        self.setDisabled(True)
        self.ldb_dialog.setEnabled(True)
        self.ldb_dialog.show()

    def open_create_pred(self):
        self.create_pred_dialog.update_dates(self.db.get_termine())
        self.setDisabled(True)
        self.create_pred_dialog.setEnabled(True)
        self.create_pred_dialog.show()

    def open_choose_pred(self):
        self.choose_pred_dialog.update_predictions(self.db.get_predictions())
        self.setDisabled(True)
        self.choose_pred_dialog.setEnabled(True)
        self.choose_pred_dialog.show()

    def show_prediction(self, date, time):
        data, header = self.db.get_prediction_data(date, time)
        self.show_pred_dialog.update_prediction(data, header, date, time)
        self.setDisabled(True)
        self.show_pred_dialog.setEnabled(True)
        self.show_pred_dialog.show()

    def set_unrdo_text(self):
        undo = "Undo"
        redo = "Redo"
        undo_txt = self.undoStack.undoText()
        redo_txt = self.undoStack.redoText()
        if undo_txt:
            undo += " \"" + undo_txt + "\""
        if redo_txt:
            redo += " \"" + redo_txt + "\""
        self.gui.actionUndo.setText(undo)
        self.gui.actionRedo.setText(redo)

    def get_sel_indexes(self):
        sel_indexes = self.gui.tableView.selectedIndexes()
        if sel_indexes:
            return [index for index in sel_indexes if not index.column()]

    def get_sel(self):
        sel_indexes = self.get_sel_indexes()
        if not sel_indexes:
            return self.tbm.rowCount(self), 1
        first_sel_index = sel_indexes[0]
        sel_indexes = self.get_sel_indexes()

        if not first_sel_index or not first_sel_index.isValid():
            return False
        startingrow = first_sel_index.row()

        return startingrow, len(sel_indexes)

    def remove_rows(self):
        if len(self.tbm.get_data()) == 0:
            return
        start, amount = self.get_sel()
        if start != len(self.tbm.get_data()):
            self.undoStack.beginMacro("Remove Rows")
            self.undoStack.push(RemoveRowsCommand(self.tbm, start, amount))
            self.undoStack.endMacro()
            self.set_unrdo_text()

    def add_rows(self):
        if len(self.tbm.get_header()) == 0:
            return
        start, amount = self.get_sel()

        self.undoStack.beginMacro("Add Row")
        self.undoStack.push(InsertRowsCommand(self.tbm, start, 1))
        self.undoStack.endMacro()
        self.set_unrdo_text()

    def paste(self):
        if len(self.gui.tableView.selectionModel().selectedIndexes()) == 0:
            return

        clipboard = QApplication.clipboard()
        index = self.gui.tableView.selectionModel().selectedIndexes()[0]
        command = EditCommand(self.tbm, index)
        command.newVal(str(clipboard.text()))

        self.undoStack.beginMacro("Paste")
        self.undoStack.push(command)
        self.undoStack.endMacro()
        self.set_unrdo_text()
        self.gui.tableView.reset()

    def cut(self):
        self.copy()
        index = self.gui.tableView.selectionModel().selectedIndexes()[0]
        command = EditCommand(self.tbm, index)
        command.newVal("")
        self.undoStack.beginMacro("Cut")
        self.undoStack.push(command)
        self.undoStack.endMacro()
        self.set_unrdo_text()
        self.gui.tableView.reset()

    def duplicate(self):
        if len(self.gui.tableView.selectionModel().selectedIndexes()) == 0:
            return

        start, amount = self.get_sel()
        self.undoStack.beginMacro("Duplicate Row")
        self.undoStack.push(DuplicateRowCommand(self.tbm, start))
        self.undoStack.endMacro()
        self.set_unrdo_text()
        self.gui.tableView.reset()

    def undo(self):
        self.undoStack.undo()
        self.set_unrdo_text()
        self.gui.tableView.reset()

    def redo(self):
        self.undoStack.redo()
        self.set_unrdo_text()
        self.gui.tableView.reset()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wa = WahlAnalyse()
    wa.show()
    sys.exit(app.exec_())
