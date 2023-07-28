import os
import time

from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QTreeWidgetItem, QPushButton
from PySide6.QtCore import Qt

from form_main_window import MainWindowForm as Form

from api.var import Type, Projet, Folder, Soft
from api.tools import *

import sys


class MainWindow(Form):

    def __init__(self):
        super().__init__()

        # ACTIONS :
        # ==============================================================================================================

        actNew = QAction(QIcon("icons/new.png"), "&New", self)
        actNew.setStatusTip("Tip a afficher concernant cette action.")
        actNew.setShortcut("Ctrl+N")
        actNew.triggered.connect(self.test)   # On appelle la methode qui sera declenchee par l'action

        # BARRE DE MENU :
        # ==============================================================================================================

        menuBar = self.menuBar()
        file = menuBar.addMenu("&File")
        file.addAction(actNew)

        # BARRE D'OUTILS :
        # ==============================================================================================================

        # Création de la barre d'outils avec son nom
        toolbar = self.addToolBar("First tool bar")  # self représente la fenêtre de type QMainWindow

        # Ajout d'une action dans la barre d'outils.
        actNew = QAction(QIcon("icons/new.png"), "&New", self)
        toolbar.addAction(actNew)

        # Ajout d'un widget quelconque dans la barre d'outils.
        toolbar.addWidget(QPushButton("A button"))

        # BARRE DE STATUTS :
        # ==============================================================================================================

        statusBar = self.statusBar()
        statusBar.showMessage(self.windowTitle())  # Définition du message initial

        # statusBar.showMessage("Message temporaire", 5_000)

        # CONNECTIONS :
        # ==============================================================================================================
        self.ui_listWidget1.clicked.connect(self.clic_list_1)
        self.ui_listWidget2.clicked.connect(self.clic_list_2)
        self.ui_listWidget3.clicked.connect(self.clic_list_3)

        self.ui_button_exit.clicked.connect(self.exit_program)

    # DECORATEURS :
    # ==================================================================================================================
    def clic_list_1(self):  # Clique sur la liste des types
        selected_type = self.ui_listWidget1.selectedItems()[0].text()

        TYPE.setcurrent(selected_type)
        PROJET.setcurrent("")
        FOLDER.setcurrent("")
        SOFT.setcurrent("")

        os.system("settype")

        reinit()

    def clic_list_2(self):  # Clique sur la liste des types
        selected_projet = self.ui_listWidget2.selectedItems()[0].text()

        PROJET.setcurrent(selected_projet)
        FOLDER.setcurrent("")
        SOFT.setcurrent("")

        reinit()

    def clic_list_3(self):  # Clique sur la liste des types
        selected_folder = self.ui_listWidget3.selectedItems()[0].text()

        FOLDER.setcurrent(selected_folder)
        SOFT.setcurrent("")

        reinit()

    def exit_program(self):  # Clique sur la liste des types
        exit()

    def test(self):
        print('ca marche!')


# METHODES :
# ======================================================================================================================

def reinit():
    doing_type = doing_projet = doing_folder = doing_soft = 0

    if TYPE.current() != "" and PROJET.current() == "" and FOLDER.current() == "" and SOFT.current() == "":
        doing_type = 1

        window.ui_listWidget2.clear()
        window.ui_listWidget3.clear()
        window.ui_listWidget4.clear()

    elif TYPE.current() != "" and PROJET.current() != "" and FOLDER.current() == "" and SOFT.current() == "":
        doing_type = 1
        doing_projet = 1

        window.ui_listWidget3.clear()
        window.ui_listWidget4.clear()

    elif TYPE.current() != "" and PROJET.current() != "" and FOLDER.current() != "" and SOFT.current() == "":
        doing_type = 1
        doing_projet = 1
        doing_folder = 1

        window.ui_listWidget4.clear()

    elif TYPE.current() != "" and PROJET.current() != "" and FOLDER.current() != "" and SOFT.current() != "":
        doing_type = 1
        doing_projet = 1
        doing_folder = 1
        doing_soft = 1

    # TRAITEMENT :

    # Type :
    if doing_type == 1:
        os.environ["ROOT_TYPE"] = os.environ["ROOT_CHANTIERS"] + "/" + TYPE.current()

        # On positionne le focus :
        item_type = window.ui_listWidget1.findItems(TYPE.current(), Qt.MatchFixedString)[0]
        window.ui_listWidget1.setCurrentItem(item_type)

        # On rempli la liste suivante :
        fill_list(window.ui_listWidget2, PROJET.liste())

    # Projet :
    if doing_projet == 1:
        os.environ["ROOT_PROJET"] = os.environ["ROOT_TYPE"] + "/" + PROJET.current()

        # On positionne le focus :
        item_projet = window.ui_listWidget2.findItems(PROJET.current(), Qt.MatchFixedString)[0]
        window.ui_listWidget2.setCurrentItem(item_projet)

        # On rempli la liste suivante :
        fill_list(window.ui_listWidget3, FOLDER.liste())

    # Folder :
    if doing_folder == 1:
        os.environ["ROOT_FOLDER"] = os.environ["ROOT_PROJET"] + "/" + FOLDER.current()

        # On positionne le focus :
        item_folder = window.ui_listWidget3.findItems(FOLDER.current(), Qt.MatchFixedString)[0]
        window.ui_listWidget3.setCurrentItem(item_folder)

        # On rempli la liste suivante :
        fill_list(window.ui_listWidget4, SOFT.liste())

    # Folder :
    if doing_soft == 1:
        os.environ["ROOT_SOFT"] = os.environ["ROOT_FOLDER"] + "/" + SOFT.current()

        # On positionne le focus :
        item_soft = window.ui_listWidget4.findItems(SOFT.current(), Qt.MatchFixedString)[0]
        window.ui_listWidget4.setCurrentItem(item_soft)


def fill_list(list_widget, liste):
    list_widget.clear()
    for item in liste:
        list_widget.addItem(item)


# ======================================================================================================================
# MAIN :
# ======================================================================================================================

if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)

    # Instancier et afficher votre fenêtre graphique.

    window = MainWindow()

    TYPE = Type()
    PROJET = Projet()
    FOLDER = Folder()
    SOFT = Soft()

    # CORPS DU PRG
    # ==================================================================================================================

    fill_list(window.ui_listWidget1, TYPE.liste())

    reinit()

    # ==================================================================================================================

    # On affiche la fenetre.
    window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())
