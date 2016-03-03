
from view import Ui_MainWindow
from PySide.QtGui import QApplication, QMainWindow, QFileDialog
import sys

from csvutil import CSVUtil
from dicttablemodel import DictTableModel

class WahlAnalyse(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.gui.actionOpen.triggered.connect(self.open_file)
        self.gui.actionSave.triggered.connect(self.save_file)
        self.gui.actionSave_as.triggered.connect(self.save_file_as)
        self.gui.actionNew.triggered.connect(self.new_file)
        self.gui.actionCopy_Cs.triggered.connect(self.copy_cs)
        self.gui.actionAdd_Row.triggered.connect(self.add_row)

        self.gui.tableView.setSortingEnabled(True)

        self.tbm = DictTableModel(list=[], parent=self)

    def add_row(self):
        self.tbm.insertRows(self.tbm.rowCount(self),1)

    def open_file(self):
        self.file = QFileDialog.getOpenFileName(self, "Choose File", filter="CSV-File (*.csv)")[0]
        if self.file != '':
            self.tbm.set_list(CSVUtil.read(self.file))
            self.gui.tableView.reset()
            self.gui.tableView.setModel(self.tbm)

    def save_file(self):
        if self.file != '' and self.file is not None:
            CSVUtil.write(self.file, self.tbm.get_list())

    def save_file_as(self):
        self.file = QFileDialog.getSaveFileName(self, "CSV-Datei speichern", dir=self.file, filter="CSV-Datei (*.csv)")[0]
        if self.file != '':
            self.save_file()

    def new_file(self):
        pass

    def copy_cs(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wa = WahlAnalyse()
    wa.show()
    sys.exit(app.exec_())
