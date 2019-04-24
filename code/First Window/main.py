import sys
from demo import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal

class Window(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hello)

    def hello(self):
        self.label.setText('hello')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())