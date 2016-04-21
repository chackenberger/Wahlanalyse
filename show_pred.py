from PySide.QtGui import QDialog, QAbstractItemView
from show_pred_view import Ui_show_prediction
from dicttablemodel import DictTableModel

class ShowPredDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.gui = Ui_show_prediction()
        self.gui.setupUi(self)
        self.tbm = DictTableModel(data= [], header=[], parent=self)
        self.gui.tableView.setSortingEnabled(True)
        self.gui.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def accept(self, *args, **kwargs):
        print("Accept")
        self.hide()

    def hide(self, *args, **kwargs):
        super().hide()
        self.setDisabled(True)
        self.parent.setEnabled(True)

    def update_prediction(self, datalist, header, termin, time):
        self.tbm.set_data(datalist, header)
        self.gui.hrdesc.setText(str(termin) + " at " + str(time))
        self.gui.tableView.reset()
        self.gui.tableView.setModel(self.tbm)
