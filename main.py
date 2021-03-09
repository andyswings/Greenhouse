#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import GHtouch

class GreenhouseApp(QtWidgets.QMainWindow, GHtouch.Ui_MainWindow):
    def __init__(self, parent=None):
        super(GreenhouseApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = GreenhouseApp()
    # form.show()
    form.showFullScreen()
    app.exec_()

if __name__ == '__main__':
    main()
