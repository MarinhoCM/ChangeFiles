import os, sys
from PyQt5 import QtWidgets

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from helpers.LogConfig import LogConfig
from resource.templates.MainWindow import Ui_CommentsReviewer


def start() -> None:
    try:
        app = QtWidgets.QApplication(sys.argv)
        main_wnd = QtWidgets.QMainWindow()
        ui = Ui_CommentsReviewer()
        ui.setupUi(main_wnd)
        main_wnd.show()
        sys.exit(app.exec_())
    except Exception as e:
        raise Exception(
            f"Ocorreu um erro ao tentar inicializar interface. \nError: {e}"
        )


if __name__ == "__main__":
    LogConfig()
    start()
