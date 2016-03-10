
from PySide.QtGui import QDialog
from s_db_view import Ui_saveDB

class SaveToDBDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.gui = Ui_saveDB()
        self.gui.setupUi(self)

    def accept(self, *args, **kwargs):
        print("Accept")
        self.hide()
        self.parent.save_data_db(self.gui.calendarWidget.selectedDate().toPython())

    def reject(self, *args, **kwargs):
        print("Reject")
        self.hide()
        
    def hide(self, *args, **kwargs):
        super().hide()
        self.setDisabled(True)
        self.parent.setEnabled(True)