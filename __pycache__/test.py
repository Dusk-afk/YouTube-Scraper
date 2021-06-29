from PyQt5 import QtCore, QtWidgets

class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        lay = QtWidgets.QVBoxLayout(self)

        self.btn = QtWidgets.QPushButton("Press me")
        self.btn.installEventFilter(self)

        lay.addWidget(self.btn)
        lay.addWidget(QtWidgets.QLineEdit())

    def eventFilter(self, obj, event):
        if obj == self.btn and event.type() == QtCore.QEvent.HoverEnter:
            self.onHovered()
        return super(Widget, self).eventFilter(obj, event)

    def onHovered(self):
        print("hovered")


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())