from PySide.QtGui import QStyledItemDelegate, QLineEdit

from commands import EditCommand


class ItemDelegate(QStyledItemDelegate):
    def __init__(self, undoStack, undoText, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.undoStack = undoStack
        self.edit = None
        self.undoText = undoText

    def setModelData(self, editor, model, index):
        newValue = editor.text()
        self.edit.newVal(newValue)
        self.undoStack.beginMacro("Edit Cell")
        self.undoStack.push(self.edit)
        self.undoStack.endMacro()
        self.undoText()

    def editorEvent(self, event, model, option, index):
        self.edit = EditCommand(model, index)

    def createEditor(self, parent, option, index):
        return QLineEdit(parent)