import sys
from demo import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal

class Window(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window,self).__init__(parent)
        self.setupUi(self)

        self.message = message(self)
        self.message.signal.connect(self.box)

        self.pushButton.clicked.connect(self.message.start)


    def box(self):
        QMessageBox.information(self, 'Warning', 'Success', QMessageBox.Ok)


class message(QThread):
    signal = pyqtSignal()
    def __init__(self, Window):
        super(message, self).__init__()
        self.window = Window

    def run(self):
        self.signal.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())