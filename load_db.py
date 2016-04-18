from PySide.QtGui import QDialog
from l_db_view import Ui_load_db

class LoadFromDBDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.gui = Ui_load_db()
        self.gui.setupUi(self)


    def accept(self, *args, **kwargs):
        print("Accept")
        self.parent.load_data_db(self.gui.dateList.currentText())
        self.hide()


    def reject(self, *args, **kwargs):
        print("Reject")
        self.hide()

    def hide(self, *args, **kwargs):
        super().hide()
        self.setDisabled(True)
        self.parent.setEnabled(True)

    def update_dates(self, termine):
        for termin in termine:
            self.gui.dateList.addItem(str(termin[0]))