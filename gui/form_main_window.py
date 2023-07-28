from PySide6 import QtGui
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QMainWindow, QWidget, QListWidget, QLineEdit, QPushButton, QFrame, QGridLayout


class MainWindowForm(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Type")

        self.resize(1600, 800)

        # Le type QWidget représente un conteneur de widgets (et il est lui-même un widget).
        # On crée une instance que l'on va mettre au centre de la fenêtre.
        centralArea = QWidget()
        # On injecte ce widget en tant que zone centrale.
        self.setCentralWidget(centralArea)

        # WIDGET DE NAVIGATION:
        frame_navigation = QFrame(centralArea)
        frame_navigation.setGeometry(QRect(10, 10, 900, 600))

        layout = QGridLayout(frame_navigation)

        # On place maintenant chacun des composants souhaités dans la zone centrale.
        self.ui_listWidget1 = QListWidget(frame_navigation)
        # self.ui_listWidget1.setGeometry(5, 5, 200, 400)

        self.ui_listWidget2 = QListWidget(frame_navigation)
        # self.ui_listWidget2.setGeometry(210, 5, 200, 400)

        self.ui_listWidget3 = QListWidget(frame_navigation)
        # self.ui_listWidget3.setGeometry(415, 5, 200, 400)

        self.ui_listWidget4 = QListWidget(frame_navigation)
        # self.ui_listWidget4.setGeometry(620, 5, 200, 400)

        layout.addWidget(self.ui_listWidget1, 0, 0, 1, 4)
        layout.addWidget(self.ui_listWidget2, 1, 0, 1, 1)
        layout.addWidget(self.ui_listWidget3, 1, 1, 1, 1)
        layout.addWidget(self.ui_listWidget4, 1, 2, 1, 1)

        # self.ui_lineEdit_type = QLineEdit(widget)
        # self.ui_lineEdit_type.setGeometry(5, 410, 200, 30)
        #
        self.ui_button_exit = QPushButton("Exit", frame_navigation)
        self.ui_button_exit.setGeometry(5, 445, 200, 30)
