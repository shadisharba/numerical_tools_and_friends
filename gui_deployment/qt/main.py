import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('main.ui', self)
        self.ui.show()

    @pyqtSlot()    
    def on_pushButton1_pressed(self):
        print("pressed")
        self.ui.StatusLabel1.setText("pressed")

    @pyqtSlot()    
    def slot1(self):
        print("pushed")
        self.ui.StatusLabel1.setText("pushed")

def main(args):
    app = QApplication(args)
    window = Gui()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main(sys.argv)
