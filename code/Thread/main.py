import sys
from demo import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread

class Window(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window,self).__init__(parent)
        self.setupUi(self)

        self.new_thread = new_thread(self)
        self.pushButton.clicked.connect(self.new_thread.start)

class new_thread(QThread):

    def __init__(self, Window):
        super(new_thread, self).__init__()
        self.window = Window

    def run(self):
        self.window.label.setText('hello')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())