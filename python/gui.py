import os
import sys
import subprocess


from PySide6.QtWidgets import QApplication, QTreeWidgetItem, QWidget
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from pathlib import Path

from api.cana_Step import Step
from api.cana_api import *
from api.cana_constants import *
from api.main_tools import *
from api.main_api import *
from api.cana_gui import *

from run import run

from interface.ui.main_window import Ui_Form as Form



BIN = os.environ["BIN"]


class MainWindow(QWidget, Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        BIN_ROOT = os.environ["BIN"]

        # STYLE :
        # ==============================================================================================================

        qss_file = 'dark.css'

        self.setStyleSheet(Path(BIN + "/python/interface/styles/" + qss_file).read_text())


        """
        # REGLAGE INTERFACE :
        # ==============================================================================================================

        # WIDGET NAVIGATION

        icon_fold = QIcon()
        icon_size = 20

        icon_fold.addFile(BIN_ROOT + "/interface/icones/fold2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_TYPE_explorer.setIcon(icon_fold)
        self.pushButton_TYPE_explorer.setIconSize(QSize(icon_size, icon_size))


        # WIDGET BUTTONS : Icone job
        icon_job = QIcon()
        icon_job.addFile(BIN_ROOT + "/interface/icones/terminal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_job.setIcon(icon_job)
        self.pushButton_job.setIconSize(QSize(icon_size, icon_size))

        # ACTIONS :
        # ==============================================================================================================

        actNew = QAction(QIcon("icons/new.png"), "&New", self)
        actNew.setStatusTip("Tip a afficher concernant cette action.")
        actNew.setShortcut("Ctrl+N")
        actNew.triggered.connect(self.tyty)   # On appelle la methode qui sera declenchee par l'action

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
        """

        # CONNECTIONS :
        # ==============================================================================================================
        self.treeWidget_navigation.clicked.connect(self.clic_list_navigation)

        self.pushButton_type.clicked.connect(self.clic_pushButton_type)
        self.pushButton_proj.clicked.connect(self.clic_pushButton_proj)
        self.pushButton_fold.clicked.connect(self.clic_pushButton_fold)
        self.pushButton_soft.clicked.connect(self.clic_pushButton_soft)



    #
    # DECORATEURS :
    # ==================================================================================================================
    def clic_list_navigation(self):  # Clique sur la liste des types

        liste_name = [typ.current_name(), prj.current_name(), fld.current_name(), sft.current_name()]
        selected_name = self.treeWidget_navigation.selectedItems()[0].text(0)  # Le 0 du text(0) est la colonne de liste
        current_step = determine_current_step()

        if sft.current_name() == "":
            step = run(current_step, selected_name, typ, prj, fld, sft)
            init(step, typ, prj, fld, sft)



    def clic_pushButton_type(self):
        step =  "type"
        names = ["", "", "", ""]
        # names = [typ.current_name(), "", "", ""]

        step = run(step, names, typ, prj, fld, sft)
        init(step, typ, prj, fld, sft)

    def clic_pushButton_proj(self):
        step = "type"
        names = [typ.current_name(), "", "", ""]
        # names = [typ.current_name(), prj.current_name(), "", ""]

        step = run(step, names, typ, prj, fld, sft)
        init(step, typ, prj, fld, sft)

    def clic_pushButton_fold(self):
        step = "type"
        names = [typ.current_name(), prj.current_name(), "", ""]
        # names = [typ.current_name(), prj.current_name(), fld.current_name(), ""]

        step = run(step, names, typ, prj, fld, sft)
        init(step, typ, prj, fld, sft)

    def clic_pushButton_soft(self):
        step = "type"
        names = [typ.current_name(), prj.current_name(), fld.current_name(), ""]
        # names = [typ.current_name(), prj.current_name(), fld.current_name(), sft.current_name()]

        step = run(step, names, typ, prj, fld, sft)
        init(step, typ, prj, fld, sft)




    # def job_terminal(self):
        # if TYPE.current_name() != "" and PROJ.current_name() != "" and FOLD.current_name():
        # buffer = "#!/bin/bash\n"
        # buffer += "export TYPE='" + typ.current_name() + "'\n"
        # buffer += "export PROJ='" + prj.current_name() + "'\n"
        # buffer += "export FOLD='" + fld.current_name() + "'\n"
        # buffer += "export SOFT='" + sft.current_name() + "'\n"
        #
        # BIN_ROOT = os.environ["BIN"]
        # file = BIN_ROOT + "/data/autorun.sh"
        # file = open(file, 'w')
        # file.write(str(buffer))
        # file.close()
        #
        # # On recupere le numero de process du terminal d'origine
        # parent_pid = os.getppid()
        #
        # # On ouvre un nouveau terminal
        # subprocess.run(["gnome-terminal"])
        #
        # # On kill l'ancien terminal
        # os.system(f"kill {parent_pid}")
        #
        # # On ferme l'interface
        # os._exit(0)

    def exit_program(self):  # Clique sur la liste des types
        exit()

    def explorer_TYPE(self):
        selected_type = self.treeWidget_TYPE.selectedItems()[0].text(0)

        os.system("nautilus " + typ.root() + "&")

    def test(self):
        print('ca marche!')




# METHODES :
# ======================================================================================================================

def fill_list_navigation(liste):
    window.treeWidget_navigation.clear()

    for item in liste:
        cg = QTreeWidgetItem(window.treeWidget_navigation, [item])


def fill_fil_ariane(step, typ, prj, fld, sft):
    window.pushButton_type.setText("")
    window.pushButton_proj.setText("")
    window.pushButton_fold.setText("")
    window.pushButton_soft.setText("")

    if step == "type":
        window.pushButton_type.setText(typ.current_name())
    elif step == "proj":
        window.pushButton_type.setText(typ.current_name())
        window.pushButton_proj.setText(prj.current_name())
    elif step == "fold":
        window.pushButton_type.setText(typ.current_name())
        window.pushButton_proj.setText(prj.current_name())
        window.pushButton_fold.setText(fld.current_name())
    elif step == "soft":
        window.pushButton_type.setText(typ.current_name())
        window.pushButton_proj.setText(prj.current_name())
        window.pushButton_fold.setText(fld.current_name())
        window.pushButton_soft.setText(sft.current_name())


def liste_items(step):

    if step == "type":
        liste = typ.liste_item()
    elif step == "proj":
        liste = prj.liste_item()
    elif step == "fold":
        liste = fld.liste_item()
    elif step == "soft":
        liste = sft.liste_item()

    return liste


def init(step, typ, prj, fld, sft):
    items = liste_items(step)
    fill_list_navigation(items)
    fill_fil_ariane(step, typ, prj, fld, sft)


# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================


if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)

    # Instanciation de la fenêtre graphique
    window = MainWindow()

    # Instanciation des variables principales
    typ = Step("type")
    prj = Step("proj")
    fld = Step("fold")
    sft = Step("soft")


    # CORPS DU PRG
    # ==================================================================================================================

    liste_name = [typ.current_name(),prj.current_name(),fld.current_name(),sft.current_name()]

    step = run("type",liste_name, typ, prj, fld, sft)

    init(step, typ, prj, fld, sft)



    # ==================================================================================================================

    # On affiche la fenêtre.
    window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())

