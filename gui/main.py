import os
import subprocess
import time
# import psutil

from PySide6.QtWidgets import QApplication, QTreeWidgetItem, QPushButton, QWidget, QHeaderView, QSizePolicy
from PySide6.QtCore import Qt, QSize, QFile

from PySide6 import QtCore as qtc


from PySide6.QtGui import QIcon
from pathlib import Path

# from form_main_window import MainWindowForm as Form
from ui.main_window import Ui_Form as Form

from api.var import Type, Projet, Folder, Soft
from api.tools import pause

from PySide6.QtUiTools import QUiLoader

import sys

BIN = os.environ["BIN"]


class MainWindow(QWidget, Form):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # STYLE :
        # ==============================================================================================================

        qss_file = 'dark.css'

        self.setStyleSheet(Path(BIN + "/gui/styles/" + qss_file).read_text())

        # REGLAGE INTERFACE :
        # ==============================================================================================================

        # WIDGET NAVIGATION : Largeur des colonnes a l'interieur des treeWidget
        self.treeWidget_TYPE.setColumnWidth(0, 220)
        self.treeWidget_PROJET.setColumnWidth(0, 220)
        self.treeWidget_FOLDER.setColumnWidth(0, 220)
        self.treeWidget_SOFT.setColumnWidth(0, 220)

        # WIDGET NAVIGATION : On masque le header des treeWidget
        self.treeWidget_TYPE.setHeaderHidden(1)
        self.treeWidget_PROJET.setHeaderHidden(1)
        self.treeWidget_FOLDER.setHeaderHidden(1)
        self.treeWidget_SOFT.setHeaderHidden(1)

        self.pushButton_exit.setIconSize(QSize(35, 35))

        # WIDGET NAVIGATION : Icones folder
        BIN_ROOT = os.environ["BIN"]
        icon_folder = QIcon()
        icon_size = 20

        icon_folder.addFile(BIN_ROOT + "/gui/icones/folder2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_TYPE_explorer.setIcon(icon_folder)
        self.pushButton_TYPE_explorer.setIconSize(QSize(icon_size, icon_size))
        self.pushButton_PROJET_explorer.setIcon(icon_folder)
        self.pushButton_PROJET_explorer.setIconSize(QSize(icon_size, icon_size))
        self.pushButton_FOLDER_explorer.setIcon(icon_folder)
        self.pushButton_FOLDER_explorer.setIconSize(QSize(icon_size, icon_size))
        self.pushButton_SOFT_explorer.setIcon(icon_folder)
        self.pushButton_SOFT_explorer.setIconSize(QSize(icon_size, icon_size))

        # WIDGET BUTTONS : Icone job
        icon_job = QIcon()
        icon_job.addFile(BIN_ROOT + "/gui/icones/terminal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_job.setIcon(icon_job)
        self.pushButton_job.setIconSize(QSize(icon_size, icon_size))

        # ACTIONS :
        # ==============================================================================================================

        # actNew = QAction(QIcon("icons/new.png"), "&New", self)
        # actNew.setStatusTip("Tip a afficher concernant cette action.")
        # actNew.setShortcut("Ctrl+N")
        # actNew.triggered.connect(self.test)   # On appelle la methode qui sera declenchee par l'action

        # BARRE DE MENU :
        # ==============================================================================================================

        # menuBar = self.menuBar()
        # file = menuBar.addMenu("&File")
        # file.addAction(actNew)

        # BARRE D'OUTILS :
        # ==============================================================================================================

        # # Création de la barre d'outils avec son nom
        # toolbar = self.addToolBar("First tool bar")  # self représente la fenêtre de type QMainWindow
        #
        # # Ajout d'une action dans la barre d'outils.
        # actNew = QAction(QIcon("icons/new.png"), "&New", self)
        # toolbar.addAction(actNew)
        #
        # # Ajout d'un widget quelconque dans la barre d'outils.
        # toolbar.addWidget(QPushButton("A button"))

        # BARRE DE STATUTS :
        # ==============================================================================================================

        # statusBar = self.statusBar()
        # statusBar.showMessage(self.windowTitle())  # Définition du message initial
        #
        # # statusBar.showMessage("Message temporaire", 5_000)

        # CONNECTIONS :
        # ==============================================================================================================
        self.treeWidget_TYPE.clicked.connect(self.clic_list_TYPE)
        self.treeWidget_PROJET.clicked.connect(self.clic_list_PROJET)
        self.treeWidget_FOLDER.clicked.connect(self.clic_list_FOLDER)
        self.treeWidget_SOFT.clicked.connect(self.clic_list_SOFT)

        self.pushButton_exit.clicked.connect(self.exit_program)

        self.pushButton_TYPE_explorer.clicked.connect(self.explorer_TYPE)

        self.pushButton_job.clicked.connect(self.job_terminal)

    #
    # DECORATEURS :
    # ==================================================================================================================
    def clic_list_TYPE(self):  # Clique sur la liste des types
        selected_type = self.treeWidget_TYPE.selectedItems()[0].text(0)  # Le 0 du text(0) est la colonne de liste

        TYPE.setcurrent(selected_type)
        PROJET.setcurrent("")
        FOLDER.setcurrent("")
        SOFT.setcurrent("")

        # os.system("settype")

        reinit()

    def clic_list_PROJET(self):  # Clique sur la liste des types
        selected_projet = self.treeWidget_PROJET.selectedItems()[0].text(0)  # Le 0 du text(0) est la colonne de liste

        PROJET.setcurrent(selected_projet)
        FOLDER.setcurrent("")
        SOFT.setcurrent("")

        reinit()

    def clic_list_FOLDER(self):  # Clique sur la liste des types
        selected_folder = self.treeWidget_FOLDER.selectedItems()[0].text(0)  # Le 0 du text(0) est la colonne de liste

        FOLDER.setcurrent(selected_folder)
        SOFT.setcurrent("")

        reinit()

    def clic_list_SOFT(self):  # Clique sur la liste des types
        selected_soft = self.treeWidget_SOFT.selectedItems()[0].text(0)  # Le 0 du text(0) est la colonne de liste

        SOFT.setcurrent(selected_soft)

        reinit()

    def job_terminal(self):
        # if TYPE.current() != "" and PROJET.current() != "" and FOLDER.current():
        buffer = "#!/bin/bash\n"
        buffer += "export TYPE='" + TYPE.current() + "'\n"
        buffer += "export PROJET='" + PROJET.current() + "'\n"
        buffer += "export FOLDER='" + FOLDER.current() + "'\n"
        buffer += "export SOFT='" + SOFT.current() + "'\n"

        BIN_ROOT = os.environ["BIN"]
        file = BIN_ROOT + "/data/autorun.sh"
        file = open(file, 'w')
        file.write(str(buffer))
        file.close()

        # On recupere le numero de process du terminal d'origine
        parent_pid = os.getppid()

        # On ouvre un nouveau terminal
        subprocess.run(["gnome-terminal"])

        # On kill l'ancien terminal
        os.system(f"kill {parent_pid}")

        # On ferme l'interface
        os._exit(0)

    def exit_program(self):  # Clique sur la liste des types
        exit()

    def explorer_TYPE(self):
        selected_type = self.treeWidget_TYPE.selectedItems()[0].text(0)

        os.system("nautilus " + TYPE.root() + "&")

    def test(self):
        print('ca marche!')


# METHODES :
# ======================================================================================================================

def reinit():
    doing_type = doing_projet = doing_folder = doing_soft = 0

    if TYPE.current() != "" and PROJET.current() == "" and FOLDER.current() == "" and SOFT.current() == "":
        doing_type = 1

        window.treeWidget_PROJET.clear()
        window.treeWidget_FOLDER.clear()
        window.treeWidget_SOFT.clear()

    elif TYPE.current() != "" and PROJET.current() != "" and FOLDER.current() == "" and SOFT.current() == "":
        doing_type = 1
        doing_projet = 1

        window.treeWidget_FOLDER.clear()
        window.treeWidget_SOFT.clear()

    elif TYPE.current() != "" and PROJET.current() != "" and FOLDER.current() != "" and SOFT.current() == "":
        doing_type = 1
        doing_projet = 1
        doing_folder = 1

        window.treeWidget_SOFT.clear()

    elif TYPE.current() != "" and PROJET.current() != "" and FOLDER.current() != "" and SOFT.current() != "":
        doing_type = 1
        doing_projet = 1
        doing_folder = 1
        doing_soft = 1

    # TRAITEMENT :

    # Type :
    if doing_type == 1:
        os.environ["ROOT_TYPE"] = os.environ["ROOT_CHANTIERS"] + "/" + TYPE.current()

        window.treeWidget_TYPE.setHeaderLabels(['Type'])

        # On positionne le focus :
        item_type = window.treeWidget_TYPE.findItems(TYPE.current(), Qt.MatchFixedString)[0]
        window.treeWidget_TYPE.setCurrentItem(item_type)

        # On rempli la liste suivante :
        fill_list(window.treeWidget_PROJET, PROJET.liste())

    # Projet :
    if doing_projet == 1:
        os.environ["ROOT_PROJET"] = os.environ["ROOT_TYPE"] + "/" + PROJET.current()

        window.treeWidget_PROJET.setHeaderLabels(['Projet'])

        # On positionne le focus :
        item_projet = window.treeWidget_PROJET.findItems(PROJET.current(), Qt.MatchFixedString)[0]
        window.treeWidget_PROJET.setCurrentItem(item_projet)

        # On rempli la liste suivante :
        fill_list(window.treeWidget_FOLDER, FOLDER.liste())

    # Folder :
    if doing_folder == 1:
        os.environ["ROOT_FOLDER"] = os.environ["ROOT_PROJET"] + "/" + FOLDER.current()

        window.treeWidget_FOLDER.setHeaderLabels(['Folder'])

        # On positionne le focus :
        item_folder = window.treeWidget_FOLDER.findItems(FOLDER.current(), Qt.MatchFixedString)[0]
        window.treeWidget_FOLDER.setCurrentItem(item_folder)

        # On rempli la liste suivante :
        fill_list(window.treeWidget_SOFT, SOFT.liste())

    # Folder :
    if doing_soft == 1:
        os.environ["ROOT_SOFT"] = os.environ["ROOT_FOLDER"] + "/" + SOFT.current()

        window.treeWidget_SOFT.setHeaderLabels(['Soft'])

        # On positionne le focus :
        item_soft = window.treeWidget_SOFT.findItems(SOFT.current(), Qt.MatchFixedString)[0]
        window.treeWidget_SOFT.setCurrentItem(item_soft)


# def fill_list(list_widget, liste):
#     list_widget.clear()
#     for item in liste:
#         list_widget.addItem(item)


def fill_list(list_widget, liste):
    list_widget.clear()
    for item in liste:
        cg = QTreeWidgetItem(list_widget, [item])
        # list_widget.addItem(item)


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

    fill_list(window.treeWidget_TYPE, TYPE.liste())

    reinit()

    # ==================================================================================================================

    # On affiche la fenêtre.
    window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())

