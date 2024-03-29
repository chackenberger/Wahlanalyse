from operator import itemgetter
from PySide import QtCore
from PySide.QtCore import QAbstractTableModel, Qt, QModelIndex, SIGNAL
from natsort import natsorted


class DictTableModel(QAbstractTableModel):
    def __init__(self, parent, data, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.header = []
        self.list = []
        self.set_data(data, header)

    def set_data(self, data, header):
        self.emit(SIGNAL("layoutToBeChanged()"))
        self.list = data
        self.header = header
        self.emit(SIGNAL("layoutChanged()"))

    def get_data(self):
        return self.list

    def get_header(self):
        return self.header

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.list[index.row()][self.header[index.column()]]

    def setData(self, *args, **kwargs):
        self.list[args[0].row()][self.header[args[0].column()]] = args[1]
        # self.emit(SIGNAL("dataChanged()"))
        return True

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def sort(self, ncol, order):
        if len(self.list) == 0:
            return
        self.emit(SIGNAL("layoutToBeChanged()"))
        self.list = natsorted(self.list, key=itemgetter(self.header[ncol]), reverse=(order == Qt.DescendingOrder))
        self.emit(SIGNAL("layoutChanged()"))

    def rowCount(self, parent):
        return len(self.list)

    def columnCount(self, parent):
        return len(self.header)

    def duplicate_row(self, row_index, parent=QModelIndex()):
        self.beginInsertRows(parent, row_index, 1)
        row = self.list[row_index].copy()
        self.list.insert(row_index+1, {key: "" for key in self.header})
        self.list[row_index+1] = row
        self.endInsertRows()

    def insertRows(self, row, count, parent=QModelIndex()):
        self.beginInsertRows(parent, row, row + count - 1)
        for i in range(count):
            self.list.insert(row, {key: "" for key in self.header})
        self.endInsertRows()
        return True

    def removeRows(self, row, count, parent=QModelIndex()):
        self.beginRemoveRows(parent, row, row + count - 1)
        del self.list[row:row + count]
        self.endRemoveRows()
        return True
