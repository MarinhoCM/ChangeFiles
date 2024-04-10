import os, sys
from unidecode import unidecode

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from resource.templates.MainWindow import Ui_CommentsReviewer

from helpers.LogConfig import LogConfig

if __name__ == "__main__":
    LogConfig()
    app = QtWidgets.QApplication(sys.argv)
    main_wnd = QtWidgets.QMainWindow()
    ui = Ui_CommentsReviewer()
    ui.setupUi(main_wnd)
    main_wnd.show()
    sys.exit(app.exec_())
