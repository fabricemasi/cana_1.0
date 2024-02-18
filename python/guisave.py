import os
import sys
import subprocess


from PySide6.QtWidgets import QApplication, QTreeWidgetItem, QListWidgetItem, QWidget, QListWidget, QLabel, QStackedWidget
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap, QImage
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
        qss_file = 'test.css'

        self.setStyleSheet(Path(BIN + "/python/interface/styles/" + qss_file).read_text())

        self.pushButton_openFolder.setIcon(QIcon("/home/fabrice/Dropbox/bin/icones/folder2.png"))
        self.pushButton_openFolder.setIconSize(QSize(24,24))

        # self.img_sel.setGeometry(0, 0, 500, 500)
        # self.img_sel.setIcon(QIcon("/home/fabrice/Dropbox/bin/icones/folder2.png"))
        # self.img_sel.setIconSize(QSize(500, 500))
        self.img_projet.hide()

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

        self.bdm_comboBox_type.currentIndexChanged.connect(self.clic_bdm_comboBox_type)

        self.pushButton_proj.clicked.connect(self.clic_pushButton_proj)
        self.pushButton_fold.clicked.connect(self.clic_pushButton_fold)
        self.pushButton_soft.clicked.connect(self.clic_pushButton_soft)

        self.pushButton_openFolder.clicked.connect(self.clic_pushButton_openFolder)


    #
    # DECORATEURS :
    # ==================================================================================================================
    def clic_list_navigation(self):  # Clique sur la liste navigation

        names = [typ.current_name(), prj.current_name(), fld.current_name(), sft.current_name()]
        try:
            selected_name = self.treeWidget_navigation.selectedItems()[0].text(0)  # Le 0 du text(0) est la colonne de liste
        except:
            selected_name = self.treeWidget_navigation.selectedItems()[0].text(1)

        current_step = determine_current_step()

        # if fld.current_name() == "":
        step = run(current_step, selected_name, typ, prj, fld, sft)
        init(step, typ, prj, fld, sft)

    def clic_list_folder(self):  # Clique sur la liste navigation
        names = [typ.current_name(), prj.current_name(), fld.current_name(), sft.current_name()]
        try:
            selected_name = self.treeWidget_folder.selectedItems()[0].text(0)  # Le 0 du text(0) est la colonne de liste
        except:
            selected_name = self.treeWidget_folder.selectedItems()[0].text(1)
        current_step = determine_current_step()

        step = run(current_step, selected_name, typ, prj, fld, sft)
        init(step, typ, prj, fld, sft)

    def clic_bdm_comboBox_type(self):

        typ.set_current_name(window.bdm_comboBox_type.currentText())
        step = run("type", "", typ, prj, fld, sft)
        init("type", typ, prj, fld, sft)



        # step =  "type"
        # names = ["", "", "", ""]
        #
        # step = run(step, names, typ, prj, fld, sft)
        # init(step, typ, prj, fld, sft)

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

    def clic_pushButton_openFolder(self):
        if typ.path():
            path = typ.path()
        if prj.path():
            path = prj.path()
        if fld.path():
            path = fld.path()
        if sft.path():
            path = sft.path()

        os.system("nautilus "+path+ " &")






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

    def addImageToItem(self, item, image):
        # Créez un QLabel personnalisé pour afficher l'image
        label = QLabel()
        label.setPixmap(image)

        # Appliquez une feuille de style pour ajouter une bordure noire et des coins arrondis
        label.setStyleSheet("QLabel { border: 1px solid rgba(32,34,35,1); border-radius: 0px; background-color: rgba(255,255,255,0.1); }")

        # Alignez l'image au centre vertical du QLabel
        label.setAlignment(Qt.AlignCenter)

        # Créez un QStackedWidget pour afficher soit l'image, soit le texte
        stacked_widget = QStackedWidget()
        stacked_widget.addWidget(label)

        # Stockez l'image dans les données de l'élément pour une référence ultérieure si nécessaire
        item.setData(0, Qt.UserRole, image)

        # Définissez le widget empilé dans la colonne 0 de l'élément
        self.treeWidget_navigation.setItemWidget(item, 0, stacked_widget)
        self.treeWidget_files.setItemWidget(item, 0, stacked_widget)





# METHODES :
# ======================================================================================================================




# def fill_list_navigation(liste, step, typ, prj, fld, sft):
#
#
#     new_liste = [];
#     filtre = ["screen",".DS_Store"]
#     # On modifie la liste (filtre + ordre) :
#     for item in liste:
#         it = str([item][0])
#         if it[0] == '_' and it not in filtre:
#             new_liste.append(it)
#
#     for item in liste:
#         it = str([item][0])
#         if it[0] != '_' and it not in filtre:
#             new_liste.append(it)
#
#     # lw = QListWidget(window.listView_navigation)
#     #
#     #
#     # for item in new_liste:
#     #     it = QListWidgetItem(item)
#     #     lw.addItem(it)
#     #
#     # lw.show()
#         # lst = QListWidgetItem(window.listView_navigation)
#
#         # lst.setText(item)
#
#     # window.treeWidget_navigation.clear()
#     # new_liste = [];
#     # filtre = ["screen",".DS_Store"]
#     # # On modifie la liste (filtre + ordre) :
#     # for item in liste:
#     #     it = str([item][0])
#     #     if it[0] == '_' and it not in filtre:
#     #         new_liste.append(it)
#     #
#     # for item in liste:
#     #     it = str([item][0])
#     #     if it[0] != '_' and it not in filtre:
#     #         new_liste.append(it)
#     #
#     #
#     #     # window.treeWidget_navigation.iconSize(QSize(200,200))  #setStyleSheet("height: 205px;")
#     #
#     # for item in new_liste:
#     #     cg = QTreeWidgetItem(window.treeWidget_navigation)
#     #     lst = QListWidgetItem(window.listView_navigation)
#     #
#     #     # type :
#     #     if typ.current_name()=="" and prj.current_name()=="" and fld.current_name()=="" and sft.current_name()=="":
#     #         window.treeWidget_navigation.setStyleSheet("QTreeWidget::item{height: 47px;}")
#     #         # TreeWidget_navigation TEXTE :
#     #         cg.setText(0, item)
#     #         lst.setText(item)
#     #         # img
#     #         window.img_sel.setIcon(QIcon(""))
#     #         window.img_sel.hide()
#     #
#     #     # projet :
#     #     if typ.current_name()!="" and prj.current_name()=="" and fld.current_name()=="" and sft.current_name()=="":
#     #
#     #         window.treeWidget_navigation.setStyleSheet("QTreeWidget::item{height: 115px;}")
#     #         # TreeWidget_navigation TEXTE :
#     #         cg.setText(0, item)
#     #
#     #         # TreeWidget_navigation IMAGE :
#     #         path_image = typ.path() + "/" + item + "/screen/main.png"
#     #         if not os.path.exists(path_image):
#     #             path_image = typ.path()+"/"+item+"/screen/main.jpg"
#     #         if not os.path.exists(path_image):
#     #             path_image = os.environ["BIN"]+"/../icones/cam.png"
#     #
#     #
#     #         if os.path.exists(path_image):
#     #             image = QPixmap(path_image).scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
#     #             window.addImageToItem(cg, image)
#     #
#     #             cg.setText(1, "  "+item)
#     #
#     #         # img
#     #         window.img_sel.setIcon(QIcon(""))
#     #
#     #     # folder :
#     #     if typ.current_name()!="" and prj.current_name()!="" and fld.current_name()=="" and sft.current_name()=="":
#     #         window.treeWidget_navigation.setStyleSheet("QTreeWidget::item{height: 47px;}")
#     #
#     #         # TreeWidget_navigation TEXTE :
#     #         cg.setText(0, item)
#     #
#     #         # img
#     #         path_image = prj.path() + "/screen/main.png"
#     #         if not os.path.exists(path_image):
#     #             path_image = prj.path() + "/screen/main.jpg"
#     #         if os.path.exists(path_image):
#     #             window.img_sel.show()
#     #             window.img_sel.setGeometry(0, 0, 500, 281)
#     #             window.img_sel.setIcon(QIcon(path_image))
#     #             window.img_sel.setIconSize(QSize(500, 281))
#     #
#     #
#     #         # window.label.setPixmap(path_image)
#     #         # window.label.setAlignment(Qt.AlignLeft)
#     #         # # stacked_widget = QStackedWidget()
#     #         # # stacked_widget.addWidget(window.label)
#     #         # stacked_widget = QStackedWidget()
#     #         # stacked_widget.addWidget(window.label)
#     #
#     #     # soft :
#     #     if typ.current_name()!="" and prj.current_name()!="" and fld.current_name()!="" and sft.current_name()=="":
#     #         window.treeWidget_navigation.setStyleSheet("QTreeWidget::item{height: 47px;}")
#     #         # TreeWidget_navigation TEXTE :
#     #         cg.setText(0, item)
#     #
#     #         # img
#     #         path_image = prj.path() + "/screen/main.png"
#     #         if not os.path.exists(path_image):
#     #             path_image = prj.path() + "/screen/main.jpg"
#     #         if os.path.exists(path_image):
#     #
#     #             window.img_sel.setGeometry(0, 0, 500, 281)
#     #             window.img_sel.setIcon(QIcon(path_image))
#     #             window.img_sel.setIconSize(QSize(500, 281))
#
#
#
#
#
#
#         # icone = QIcon("/media/partage/PIPELINE/pipe/PIPELINE/chantier/3d/hotrod/screen/main.jpg")
#         # pix = icone.pixmap(200,200)
#
#
#
#
#         # cg.setIcon(0,QIcon("/media/partage/PIPELINE/pipe/PIPELINE/chantier/3d/hotrod/screen/main.jpg").pixmap(300, 300))
#         # icon = QImage("/media/partage/PIPELINE/pipe/PIPELINE/chantier/3d/hotrod/screen/main.jpg")
#         # pixicon = icon
#         # cg.setIcon(0, icon)
#
#         # cg.setText(0, "")
#         # cg.setIcon(0,QIcon(pix))
#
#         # cg.setText(0, str([item][0]))
#         # cg.setText(1, str([item][0]))
#
# def fill_list_folder(liste, step, typ, prj, fld, sft):
#     window.treeWidget_folder.clear()
#     for item in liste:
#         cg = QTreeWidgetItem(window.treeWidget_folder, [item])
#         cg.setText(0, item)
#
# def fill_list_files(liste, step, typ, prj, fld, sft):
#     window.treeWidget_files.clear()
#     for item in liste:
#         cg = QTreeWidgetItem(window.treeWidget_files, [item])

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

    window.listWidget_projet.clear()

    fill_list_proj(typ.liste_item())





    # if step == "":
        # window.treeWidget_files.clear()
        # fill_list_navigation(items, step, typ, prj, fld, sft)


    # if step == "type":
    #     # window.treeWidget_files.clear()
    #     fill_list_navigation(items, step, typ, prj, fld, sft)
    # if step == "proj":
    #     # window.treeWidget_files.clear()
    #     fill_list_navigation(items, step, typ, prj, fld, sft)
    # if step == "fold":
    #     # window.treeWidget_folder.clear()
    #
    #     # window.img.icon("/media/partage/PIPELINE/pipe/PIPELINE/chantier/3d/hotrod/screen/main.jpg")
    #     # window.img_sel.setGeometry(0, 0, 500, 500)
    #     # window.img_sel.setIcon(QIcon("/media/partage/PIPELINE/pipe/PIPELINE/chantier/3d/hotrod/screen/main.jpg"))
    #     # window.img_sel.setIconSize(QSize(500,500))
    #     fill_list_folder(items, step, typ, prj, fld, sft)
    # if step == "soft":
    #     # window.treeWidget_files.clear()
    #     fill_list_files(items, step, typ, prj, fld, sft)


    # fill_fil_ariane(step, typ, prj, fld, sft)


def fill_list_projet(items):
    window.listWidget_projet.addItems(items)


def fill_combobox_type(items):
    window.bdm_comboBox_type.clear()
    window.bdm_comboBox_type.addItems(items)


# def fill_list_projet(liste, step, typ, prj, fld, sft):
#     new_liste = [];
#     filtre = ["screen", ".DS_Store"]
#     # On modifie la liste (filtre + ordre) :
#     for item in liste:
#         it = str([item][0])
#         if it[0] == '_' and it not in filtre:
#             new_liste.append(it)
#
#     for item in liste:
#         it = str([item][0])
#         if it[0] != '_' and it not in filtre:
#             new_liste.append(it)
#








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

    fill_combobox_type(liste_items('type'))
    window.bdm_comboBox_type.setCurrentText("3d")

    typ.set_current_name("3d")

    names = [typ.current_name(),prj.current_name(),fld.current_name(),sft.current_name()]
    step = run("type",names, typ, prj, fld, sft)

    init(step, typ, prj, fld, sft)


    # ==================================================================================================================

    # On affiche la fenêtre.
    window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())

