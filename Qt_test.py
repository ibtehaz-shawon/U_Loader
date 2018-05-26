import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Hello World! Immatur3 uTub3 Download3r'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(100, 70)
        button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        StatusBar(self.title)


class StatusBar(QMainWindow):

    def __init__(self, title):
        super().__init__(None)
        self.title = title
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.show_status_bar()

    def show_status_bar(self):
        self.setWindowTitle(self.title)
        self.statusBar().showMessage('Hello World!')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


