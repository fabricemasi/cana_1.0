import sys
import os

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "../main_window.ui"
    ui_file = QFile(ui_file_name)
    loader = QUiLoader()
    window = loader.load(ui_file)

    ui_file.close()

    window.show()
    sys.exit(app.exec())
