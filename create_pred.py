from PySide.QtGui import QDialog
from create_pred_view import Ui_create_prediction

class CreatePredDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.gui = Ui_create_prediction()
        self.gui.setupUi(self)


    def accept(self, *args, **kwargs):
        print("Accept")
        time =  self.gui.timeEdit.time()
        self.parent.create_prediction(self.gui.dateList.currentText(), str(time.hour()).zfill(2) + ":" + str(time.minute()).zfill(2))
        self.hide()


    def reject(self, *args, **kwargs):
        print("Reject")
        self.hide()

    def hide(self, *args, **kwargs):
        super().hide()
        self.setDisabled(True)
        self.parent.setEnabled(True)

    def update_dates(self, termine):
        self.gui.dateList.clear()
        for termin in termine:
            self.gui.dateList.addItem(str(termin[0]))