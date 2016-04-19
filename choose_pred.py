from PySide.QtGui import QDialog
from choose_pred_view import Ui_choose_prediction

class ChoosePredDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.gui = Ui_choose_prediction()
        self.gui.setupUi(self)


    def accept(self, *args, **kwargs):
        print("Accept")
        pred = self.predictions[self.gui.comboBox.currentIndex()]
        self.parent.show_prediction(pred["termin"], pred["time"])
        self.hide()


    def reject(self, *args, **kwargs):
        print("Reject")
        self.hide()

    def hide(self, *args, **kwargs):
        super().hide()
        self.setDisabled(True)
        self.parent.setEnabled(True)

    def update_predictions(self, predictions):
        self.gui.comboBox.clear()
        self.predictions = predictions
        for pred in self.predictions:
            self.gui.comboBox.addItem(str(pred["termin"]) + " - " + str(pred["time"]))