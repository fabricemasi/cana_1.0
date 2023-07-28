import sys
import os

from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6.QtUiTools import QUiLoader

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    ui_file_name = "../UI/form_main_window.ui"
    ui_file = qtc.QFile(ui_file_name)

    loader = QUiLoader()

    window = loader.load(ui_file)

    ui_file.close()

    window.show()
    sys.exit(app.exec())