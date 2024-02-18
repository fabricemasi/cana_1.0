import os
import sys
import subprocess


from PySide6.QtWidgets import (QAbstractItemView, QTableWidgetItem, QApplication, QTreeWidgetItem, QListWidgetItem,
                               QWidget, QListWidget, QLabel, QStackedWidget,QTableWidget, QVBoxLayout, QHBoxLayout,
                               QSpacerItem, QSizePolicy, QFileDialog, QMenu)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap, QImage, QPainter, QPainterPath
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
        ROOT_TYPE = os.environ["ROOT_TYPE"]





        # STYLE :
        # ==============================================================================================================

        qss_file = 'dark.css'
        qss_file = 'test.css'
        self.setStyleSheet(Path(BIN + "/python/interface/styles/" + qss_file).read_text())




        # MODIF INTERFACE :
        # ==============================================================================================================

        self.gridLayout.setContentsMargins(0,0,0,0)
        self.gridLayout.setSpacing(0)

        self.frame_toolbox_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_toolbox_layout.setSpacing(0)

        self.frame_proj_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_proj_layout.setSpacing(0)

        self.frame_fold_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_fold_layout.setSpacing(0)

        # Liaison du clic droit avec l'événement personnalisé
        self.listWidget_proj.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget_proj.customContextMenuRequested.connect(self.list_proj_menu)





        self.bdm_comboBox_type.addItems(os.listdir(ROOT_TYPE))
        self.bdm_comboBox_type.setCurrentText("3d")

        # self.pushButton_openFolder.setIcon(QIcon("/home/fabrice/Dropbox/bin/icones/folder2.png"))
        # self.pushButton_openFolder.setIconSize(QSize(24,24))


        # CONNECTIONS :
        # ==============================================================================================================

        self.bdm_comboBox_type.currentIndexChanged.connect(self.bdm_comboBox_type_changed)
        self.fold_pushButton_retour.clicked.connect(self.fold_button_retour_clicked)
        self.listWidget_proj.itemPressed.connect(self.list_proj_pressed)



    def init(self, typ, prj, fld, sft):

        step = determine_step()
        aa(step=step)
        if step == "proj":
            # if not self.frame_proj.isVisible():
            #     self.listWidget_proj.clear()
            #     self.frame_proj.show()
            self.frame_proj.show()



            self.image_proj.hide()
            self.frame_fold.hide()

            self.frame_proj.show()
            self.list_proj_fill(typ.liste_item())


        if step == "fold":
            self.frame_proj.hide()

            self.listWidget_fold.clear()

            self.image_proj_fill()
            self.fold_fill_infos(typ, prj, fld, sft)
            self.frame_fold.show()
            self.list_fold_fill(prj.liste_item())


    def bdm_comboBox_type_changed(self):
        selected_type = window.bdm_comboBox_type.currentText()
        window.bdm_comboBox_type.setCurrentText(selected_type)

        run("type", selected_type, typ, prj, fld, sft)

        self.frame_proj.hide()
        self.init(typ, prj, fld, sft)




    def list_proj_fill(self, items):

        item_height = 89
        image_bordure = 3
        image_height = item_height - (image_bordure * 2)
        image_ratio = 1.777777
        image_border_radius = 4

        list_widget = self.listWidget_proj

        # On remplie la liste avec les items de l'input :
        # n = 0
        for i in items:
            # Initialisation item
            item = QListWidgetItem(i, list_widget)
            item.setSizeHint(QSize(item_height,item_height))  # Taille de chaque élément

            # Création du widget pour chaque item :
            widget = QWidget()

            # Creation du layout :
            layout = QHBoxLayout(widget)

            # Modification interface :
            layout.setContentsMargins(0, 0, 0, 0)
            widget.setObjectName('list_proj')


            # ===========================
            # Ajout de l'image
            # ===========================
            image_label = QLabel()
            image_label.setObjectName("listWidget_proj_image")

            # Adresse de l'image
            image_path = typ.path() + "/" + i + "/.data/petit_format.png"

            # On reformate l'image
            pixmap = self.image_reformat(image_path, height=image_height, ratio=image_ratio)

            # On arrondi les angles
            pixmap = self.image_border_radius(pixmap,image_border_radius)

            # On affiche l'image
            image_label.setPixmap(pixmap)
            layout.addWidget(image_label, alignment=Qt.AlignLeft)


            # ===========================
            # Ajout du Qlabel texte (nom)
            # ===========================
            name_label = QLabel(i)
            name_label.setObjectName("listWidget_proj_text")
            # name_label.setFixedWidth(150)  # Largeur fixe
            layout.addWidget(name_label, alignment=Qt.AlignLeft)



            # ===========================
            # Ajout du spacer horizontal
            # ===========================
            spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            layout.addItem(spacer)



            # ===========================
            # Clique sur un item :
            self.listWidget_proj.setItemWidget(item, widget)
            # Clique droit (pour charger une image) :
            # self.listWidget_proj.setContextMenuPolicy(Qt.CustomContextMenu)
            # self.listWidget_proj.customContextMenuRequested.connect(self.openFileDialog)
            item.setData(Qt.UserRole, widget)  # Sauvegarder le widget dans les données de l'élément

    def list_proj_pressed(self, item):
        # On extrait le nom de la selection :
        widget = item.data(Qt.UserRole)
        if isinstance(widget, QWidget):
            for child in widget.children():         # Parcourez tous les enfants du widget
                if isinstance(child, QLabel):       # Vérifiez s'il s'agit d'un QLabel
                    choix = child.text()            # Obtenez le texte du QLabel
                    if choix != "":
                        projet = choix
                        self.list_proj_show_item_selected(projet)
                if isinstance(child, QHBoxLayout):
                    pass



        run("proj", projet, typ, prj, fld, sft)
        self.init(typ, prj, fld, sft)

    def list_proj_show_item_selected(self, projet_name):

        item_border_radius = 7
        couleur_selection = "rgba(0,100,200,1)"

        for i in range(self.listWidget_proj.count()):
            current_item = self.listWidget_proj.item(i)
            txt=""
            if current_item is not None:
                widget = current_item.data(Qt.UserRole)
                if isinstance(widget, QWidget):
                    for child in widget.children():
                        if isinstance(child, QLabel):
                            txt = child.text()
                        if txt==projet_name:
                            widget.setStyleSheet(
                                f"border-radius: {item_border_radius}px; border: none; background-color: {couleur_selection};")
                        else :
                            widget.setStyleSheet("")

    def list_proj_menu(self, point):
        """
        Permet d'afficher un menu lorsque l'on clique droit sur les items de listWidget_proj
        :param point: item de la liste
        """
        item = self.listWidget_proj.itemAt(point)
        if item is not None:
            # Calculer les coordonnées globales décalées
            global_point = self.listWidget_proj.mapToGlobal(point)
            global_point.setX(global_point.x() + 0)  # Décalage de 10 pixels vers la droite
            global_point.setY(global_point.y() + 0)  # Décalage de 10 pixels vers le bas

            menu = QMenu(self)
            select_file_action = menu.addAction("Sélectionner un fichier")
            select_file_action.triggered.connect(lambda: self.list_proj_choix_image(item.text()))
            menu.exec(global_point)

    def list_proj_choix_image(self, item_text):
        """
        Permet d'afficher une boite de dialogue afin de choisir un fichier
        :param item_text: nom de l'item, par exemple hotrod
        """

        # Path :
        path = typ.path() + "/" + item_text

        # Boite de dialog pour choisir le fichier :
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Sélectionner un fichier")
        file_dialog.setDirectory(path)  # Répertoire spécifique

        selected_file, _ = file_dialog.getOpenFileName(self, "Sélectionner un fichier", "","Images (*.png *.jpg *.jpeg *.bmp *.gif);;Tous les fichiers (*)")

        if selected_file:
            print(f"Fichier sélectionné pour '{item_text}': {selected_file}")

            pixmap = QPixmap(selected_file)


            # On formate l'image:
            width = pixmap.width()
            height = pixmap.height()

            ratio_goal = 1.7777777777
            ratio = width / height

            if ratio > ratio_goal:
                new_width = height * ratio_goal
                new_height = height

                dec = (width - new_width) / 2

                pixmap_crop = pixmap.copy(dec, 0, new_width, new_height)
            elif ratio < ratio_goal:
                new_width = width
                new_height = width / ratio_goal

                dec = (height - new_height) / 2

                pixmap_crop = pixmap.copy(0, dec, new_width, new_height)
            else:
                new_width = width
                new_height = height


            # On dimmensionne l'image et on l'enregistre :
            h = 300

            pixmap = pixmap_crop.scaled(h * ratio_goal, h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # Définir le chemin de sortie et s'assurer que les répertoires existent
            output_directory = typ.path() + "/" + item_text + "/.data/"
            os.makedirs(output_directory, exist_ok=True)
            # Enregistrer l'image dans un fichier PNG
            output_file = os.path.join(output_directory, "grand_format.png")
            pixmap.save(output_file, "PNG")


            h = 84

            pixmap = pixmap_crop.scaled(h * ratio_goal, h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # Définir le chemin de sortie et s'assurer que les répertoires existent
            output_directory = typ.path() + "/" + item_text + "/.data/"
            os.makedirs(output_directory, exist_ok=True)
            # Enregistrer l'image dans un fichier PNG
            output_file = os.path.join(output_directory, "petit_format.png")
            pixmap.save(output_file, "PNG")


            # On rafraichie la liste pour faire apparaitre l'image selectionnee :
            self.listWidget_proj.clear()
            self.list_proj_fill(typ.liste_item())





    def image_proj_fill(self):

        # Path de l'image :
        image_path = prj.path() + "/.data/grand_format.png"

        if not os.path.exists(image_path):
            image_path = BIN+"/../icones/camera.png"
            pixmap = self.image_reformat(image_path,height=300,ratio = 1.7777777)
        else:
            pixmap = QPixmap(image_path)


        # On arrondie les angles :
        pixmap = self.image_border_radius(pixmap,5)


        # On affiche l'image :
        self.image_proj.setPixmap(pixmap)
        self.image_proj.show()

    def fold_button_retour_clicked(self):
        fld.set_current_name("")
        sft.set_current_name("")

        aa(t2=fld.current_name())

        run("proj", prj.current_name(), typ, prj, fld, sft)

        self.init(typ, prj, fld, sft)



    def fold_fill_infos(self,typ, prj, fld, sft):
        self.fold_label_01.setText(prj.current_name())

    def list_fold_fill(self, items):

        item_height = 89
        image_bordure = 3
        image_height = item_height - (image_bordure * 2)
        image_ratio = 1.777777
        image_border_radius = 4

        list_widget = self.listWidget_fold

        # On remplie la liste avec les items de l'input :
        # n = 0
        for i in items:
            # Initialisation item
            item = QListWidgetItem(i, list_widget)
            item.setSizeHint(QSize(item_height,item_height))  # Taille de chaque élément

            # Création du widget pour chaque item :
            widget = QWidget()

            # Creation du layout :
            layout = QHBoxLayout(widget)

            # Modification interface :
            layout.setContentsMargins(0, 0, 0, 0)
            widget.setObjectName('list_fold')


            # ===========================
            # Ajout de l'image
            # ===========================
            image_label = QLabel()
            image_label.setObjectName("listWidget_fold_image")

            # Adresse de l'image
            image_path = prj.path() + "/" + i + "/.data/petit_format.png"
            if not os.path.exists(image_path):
                image_path = BIN + "/../icones/camera.png"



            # On reformate l'image
            pixmap = self.image_reformat(image_path, height=image_height, ratio=image_ratio)

            # On arrondi les angles
            pixmap = self.image_border_radius(pixmap,image_border_radius)

            # On affiche l'image
            image_label.setPixmap(pixmap)
            layout.addWidget(image_label, alignment=Qt.AlignLeft)


            # ===========================
            # Ajout du Qlabel texte (nom)
            # ===========================
            name_label = QLabel(i)
            name_label.setObjectName("listWidget_fold_text")
            # name_label.setFixedWidth(150)  # Largeur fixe
            layout.addWidget(name_label, alignment=Qt.AlignLeft)



            # ===========================
            # Ajout du spacer horizontal
            # ===========================
            spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            layout.addItem(spacer)



            # ===========================
            # Clique sur un item :
            self.listWidget_fold.setItemWidget(item, widget)
            # Clique droit (pour charger une image) :
            # self.listWidget_proj.setContextMenuPolicy(Qt.CustomContextMenu)
            # self.listWidget_proj.customContextMenuRequested.connect(self.openFileDialog)
            item.setData(Qt.UserRole, widget)  # Sauvegarder le widget dans les données de l'élément






    def image_border_radius(self, pixmap, radius):
        rounded_pixmap = QPixmap(pixmap.size())
        rounded_pixmap.fill(Qt.transparent)

        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        path.addRoundedRect(pixmap.rect(), radius, radius)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)

        return rounded_pixmap

    def image_reformat(self, path:str, width:int=0, height:int=0, ratio:int=1.5):
        """
        Si width!=0 et height!=0, le ratio n'est pas pris en compte \n
        Si width==0 et height==0, une valeur de 32 pixels en hauteur est prise en compte
        :param path: Parametre obligatoire
        :param width: Facultatif
        :param height: Facultatif
        :param ratio: Facultatif, 1.5 par default
        :return: pixmap de l'image
        """

        auto_height = 32    # Si width==0 et height==0

        original_image = path
        original_pixmap = QPixmap(original_image)
        original_width = original_pixmap.width()
        original_height = original_pixmap.height()
        original_ratio = original_width/original_height




        if original_ratio > ratio:
            temp_width = original_height * ratio
            temp_height = original_height

            dec = (original_width - temp_width) / 2

            pixmap_crop = original_pixmap.copy(dec, 0, temp_width, temp_height)

        elif original_ratio < ratio:
            temp_width = original_width
            temp_height = original_width / ratio

            dec = (original_height - temp_height) / 2

            pixmap_crop = original_pixmap.copy(0, dec, temp_width, temp_height)

        else:
            temp_width = original_width
            temp_height = original_height
            pixmap_crop = original_pixmap


        if width != 0 and height == 0:
            new_width = width
            new_height = width / ratio

        elif width == 0 and height != 0:
            new_width = height * ratio
            new_height = height

        elif width != 0 and width != 0:
            new_width = width
            new_height = height

        elif width == 0 and width == 0:
            new_width = auto_height * ratio
            new_height = auto_height


        pixmap = QPixmap(pixmap_crop).scaled(new_width, new_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        return pixmap



    def icon_click_handler(arg1, arg2):
        print(f"Icône cliquée avec arguments: {arg1}, {arg2}")


    def onSelectionChanged(self, selected, deselected):
        # Gérer la sélection en dessinant un rectangle autour de la ligne sélectionnée
        if selected.indexes():
            self.selectedRow = selected.indexes()[0].row()
            # self.viewport().update()
        else:
            self.selectedRow = -1





    def exit_program(self):  # Clique sur la liste des types
        exit()

    def explorer_TYPE(self):
        selected_type = self.treeWidget_TYPE.selectedItems()[0].text(0)

        os.system("nautilus " + typ.root() + "&")




        # n = n + 1

def fill_list_fold(items):
    window.listWidget_fold.addItems(items)

def fill_list_soft(items):
    window.listWidget_soft.addItems(items)

def fill_list_fil1(items):
    window.listWidget_fil1.addItems(items)


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



    # ==================================================================================================================

    # Debut du programme : on impose le type a 3D et donc la step a "type"
    typ.set_current_name("3d")

    names = [typ.current_name(),prj.current_name(),fld.current_name(),sft.current_name()]

    step = run("type",names, typ, prj, fld, sft)

    window.init(typ, prj, fld, sft)



    # ==================================================================================================================

    window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())

