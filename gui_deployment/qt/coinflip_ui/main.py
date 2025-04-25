#!/usr/bin/env python3
import numpy as np
import sys
import os
import h5py
import time
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import pyqtSlot, pyqtBoundSignal, pyqtSignal, QThreadPool
from PyQt5 import QtCore

# use frames.py Created by: PyQt5 UI code generator 5.9.2
# from frames import *
# class MainWindow( QMainWindow, Ui_MainWindow):
# self.setupUi( self)
# class Popup( QMainWindow, Ui_Form):


######################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = uic.loadUi("qt_frames/qt_main.ui", self)
        self.h5fname = "coin_tosses.h5"
        self.save_location.setText('Results will be saved to: "{}"'.format(self.h5fname))
        if os.path.isfile(self.h5fname):
            self.existing_set.setChecked(True)
            self.new_set.setChecked(False)
        ### Parameters in the object

    ################ Morphological stuff #################
    @pyqtSlot(bool)
    def on_existing_set_toggled(self, state):
        if not os.path.isfile(self.h5fname) and state:
            """give feedback that the file does not exist"""
            reply = QMessageBox.warning(self, "Warning", "File of previous results does not exist.", QMessageBox.Ok)
            self.existing_set.setChecked(not state)
            self.new_set.setChecked(state)
            return
        else:
            self.existing_set.setChecked(state)
            self.new_set.setChecked(not state)

    @pyqtSlot(bool)
    def on_new_set_toggled(self, state):
        if os.path.isfile(self.h5fname) and state:
            """give feedback that the file does not exist"""
            reply = QMessageBox.warning(self, "Warning", "File of previous results will be deleted!", QMessageBox.Ok)
        self.new_set.setChecked(state)
        self.existing_set.setChecked(not state)

    @pyqtSlot()
    def on_open_toss_pressed(self):
        self.popup = Popup(self.new_set.isChecked(), self.h5fname, self)
        self.new_set.setChecked(False)
        self.existing_set.setChecked(True)
        self.popup.show()

    @pyqtSlot()
    def on_quit_pressed(self):
        sys.exit(0)


class Popup(QMainWindow):
    def __init__(self, new_set, h5fname, parent=None):
        super(Popup, self).__init__(parent)
        self.ui = uic.loadUi("qt_frames/qt_widget.ui", self)

        self.h5fname = h5fname
        if new_set:
            self.prev_label.hide()
            self.previous.hide()
            self.h5file = h5py.File(self.h5fname, "w")
        else:
            self.prev_label.show()
            self.previous.show()
            self.h5file = h5py.File(self.h5fname, "a")
            try:
                self.previous.setText(str(len(np.array(self.h5file["tosses"]))))
            except:
                self.previous.setText("0")
        self.counter = 0
        self.tosses = []
        self.delay = 1  # 1 second delay between coin tosses
        self.pause_button = FunctionThread(self.delay)
        # self.pause_button.signal_handle.connect( self.pause )
        self.pause_button.disable.connect(self.pause)
        self.pause_button.enable.connect(self.unpause)

    def pause(self):
        self.disable_box.setDisabled(True)

    def unpause(self):
        self.disable_box.setDisabled(False)

    @pyqtSlot()
    def on_heads_clicked(self):
        self.counter += 1
        self.current.setText(str(self.counter))
        self.tosses.append(0)
        self.pause_button.start()

    @pyqtSlot()
    def on_tails_clicked(self):
        self.counter += 1
        self.current.setText(str(self.counter))
        self.tosses.append(1)
        # self.pause_button.start()

    @pyqtSlot()
    def on_quit_pressed(self):
        if len(self.tosses) == 0:
            self.h5file.close()
            self.destroy()
            return
        if "tosses" in self.h5file:
            x = list(self.h5file["tosses"][:])
            x.extend(self.tosses)
            self.tosses = x
            del self.h5file["tosses"]
        if len(self.tosses) == 1:
            tosses = np.array([self.tosses])[0]
        else:
            tosses = np.array(self.tosses)
        print(tosses.shape)
        try:
            self.h5file.create_dataset("tosses", data=tosses, dtype="u1", compression="gzip")
        except:
            pass
        self.h5file.close()
        self.destroy()


## pyqt generator threads that the UI is updated in real time when clicking and 'resonding'
class FunctionThread(QtCore.QThread):  # , QtCore.QRunnable):
    disable = QtCore.pyqtSignal()
    enable = QtCore.pyqtSignal()

    def __init__(self, delay=1):
        super(FunctionThread, self).__init__()
        self.delay = delay

    def run(self, *args, **kwargs):
        self.disable.emit(*args, **kwargs)
        time.sleep(self.delay)
        self.enable.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
