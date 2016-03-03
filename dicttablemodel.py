from operator import itemgetter
from PySide import QtCore
from PySide.QtCore import QAbstractTableModel, Qt, QModelIndex, SIGNAL, QAbstractItemModel
from natsort import natsorted


class DictTableModel(QAbstractTableModel):
    def __init__(self, parent, list, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.header = []
        self.set_list(list)

    def generate_headers(self):
        self.header.clear()
        if len(self.list) > 0:
            for key in self.list[0]:
                self.header.append(key)

    def set_list(self, list):
        """
        for line in list:
            for key in line:
                if line[key].isdigit():
                    line[key] = int(line[key])
        """
        self.list = list
        self.generate_headers()
        self.emit(SIGNAL("layoutChanged()"))

    def get_list(self):
        return self.list

    def rowCount(self, parent):
        return len(self.list)

    def columnCount(self, parent):
        return len(self.header)

    def insertRows(self, row, count, parent=QModelIndex):
        self.beginInsertRows(QModelIndex(), count, count)
        for i in range(count):
            self.list.insert(row, {key: "" for key in self.header})
        self.endInsertRows()
        return True

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.list[index.row()][self.header[index.column()]]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def setData(self, index, value, role=Qt.EditRole):
        self.list[index.row()][self.header[index.column()]] = value
        self.emit(SIGNAL("dataChanged()"))
        return True

    def sort(self, ncol, order):
        if len(self.list) == 0:
            return
        self.emit(SIGNAL("layoutToBeChanged()"))
        self.list = natsorted(self.list, key=itemgetter(self.header[ncol]), reverse=(order == Qt.DescendingOrder))
        self.emit(SIGNAL("layoutChanged()"))
