import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QDesktopWidget, QMainWindow


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Click Me!', self)
        # qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.clicked.connect(self.btn_click)
        qbtn.resize(qbtn.sizeHint())
        self.center()
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def btn_click(self):
        new_Window = QMainWindow()
        new_Window.title = 'PyQt5 status bar example - pythonspot.com'
        new_Window.left = 10
        new_Window.top = 10
        new_Window.width = 640
        new_Window.height = 480

        new_Window.setWindowTitle("Hello World?")
        new_Window.statusBar().showMessage('Message in statusbar.')
        self.new_Window.show()
        print("hello world!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
