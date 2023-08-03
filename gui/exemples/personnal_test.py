from PySide6 import QtGui
from PySide6.QtCore import QRect, QSize
from PySide6.QtWidgets import QMainWindow, QWidget, QListWidget, QLineEdit, QPushButton, QFrame, QGridLayout


class MainWindowForm(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Type")

        self.resize(1600, 800)

        self.setStyleSheet(u"QWidget{\n"
                           "	border-width: 3px; \n"
                           "    border-style: solid; \n"
                           "    border-color: rgb(125,125,125); \n"
                           "}\n"
                           "QFrame{\n"
                           "	border-width: 2px; \n"
                           "    border-style: dashed; \n"
                           "    border-color: rgba(0,125,255,50); \n"
                           "}")

        # Le type QWidget représente un conteneur de widgets (et il est lui-même un widget).
        # On crée une instance que l'on va mettre au centre de la fenêtre.
        centralArea = QWidget()
        # On injecte ce widget en tant que zone centrale.
        self.setCentralWidget(centralArea)

        # FRAME NAVIGATION :
        self.widget_navigation = QFrame(centralArea)
        self.widget_navigation.setGeometry(QRect(10, 10, 900, 600))
        self.widget_navigation.setMinimumSize(QSize(1031, 0))

        self.widget_navigation_gridLayout = QGridLayout(self.widget_navigation)

        self.type_frame = QFrame(self.widget_navigation_gridLayout)

        # On place maintenant chacun des composants souhaités dans la zone centrale.
        self.listView_TYPE = QListWidget(self.type_frame)
        # self.ui_listWidget1.setGeometry(5, 5, 200, 400)

        self.listView_PROJET = QListWidget(self.type_frame)
        # self.ui_listWidget2.setGeometry(210, 5, 200, 400)

        self.listView_FOLDER = QListWidget(self.type_frame)
        # self.ui_listWidget3.setGeometry(415, 5, 200, 400)

        self.listView_SOFT = QListWidget(self.type_frame)
        # self.ui_listWidget4.setGeometry(620, 5, 200, 400)








        self.type_frame.addWidget(self.listView_TYPE, 0, 0)
        self.type_frame.addWidget(self.listView_PROJET, 0, 1)
        self.type_frame.addWidget(self.listView_FOLDER, 0, 2)
        self.type_frame.addWidget(self.listView_SOFT, 0, 3)

        # self.ui_lineEdit_type = QLineEdit(widget)
        # self.ui_lineEdit_type.setGeometry(5, 410, 200, 30)
        #
        self.ui_button_exit = QPushButton("Exit", self.widget_navigation)
        self.ui_button_exit.setGeometry(5, 445, 200, 30)
