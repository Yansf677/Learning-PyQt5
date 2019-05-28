import sys
import time
from demo import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer

class Window(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start)

        self.timer = QTimer()
        self.timer.timeout.connect(self.time)

    def start(self):
        self.timer.start(2 * 1000)

    def time(self):
        self.label.setText('{} s'.format(time.time()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())