import os
import sys
import subprocess


from PySide6.QtWidgets import QAbstractItemView, QTableWidgetItem, QApplication, QTreeWidgetItem, QListWidgetItem, QWidget, QListWidget, QLabel, QStackedWidget,QTableWidget, QVBoxLayout, QHBoxLayout
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

# class MyTableWidget(QTableWidget,image,texte,t2):
#     def __init__(self):
#         super().__init__()
#
#         # Configuration de la table avec 3 colonnes
#         self.setColumnCount(3)
#         self.setHorizontalHeaderLabels(['Image', 'Texte 1', 'Texte 2'])
#
#         # Remplissage de la table avec des exemples
#         self.addTableRow(image, texte, t2)
#
#         # Ajoutez d'autres lignes selon vos besoins
#
#         # Configuration du modèle de sélection
#         self.selectionModel().selectionChanged.connect(self.onSelectionChanged)
#
#         # Variables pour stocker la ligne sélectionnée
#         self.selectedRow = -1
#
#     def addTableRow(self, imagePath, text1, text2):
#         # (La même méthode que précédemment)
#         # Création d'un élément de ligne pour chaque colonne
#         imageItem = QTableWidgetItem()
#         text1Item = QTableWidgetItem(text1)
#         text2Item = QTableWidgetItem(text2)
#
#         # Configuration de l'élément de l'image avec une image
#         pixmap = QPixmap(imagePath)
#         imageItem.setIcon(QIcon(pixmap))
#
#         # Ajout des éléments à la table
#         rowPosition = self.rowCount()
#         self.insertRow(rowPosition)
#         self.setItem(rowPosition, 0, imageItem)
#         self.setItem(rowPosition, 1, text1Item)
#         self.setItem(rowPosition, 2, text2Item)
#
#     def onSelectionChanged(self, selected, deselected):
#         # Gérer la sélection en dessinant un rectangle autour de la ligne sélectionnée
#         if selected.indexes():
#             self.selectedRow = selected.indexes()[0].row()
#             self.viewport().update()
#         else:
#             self.selectedRow = -1
#
#     def paintEvent(self, event):
#         if self.selectedRow != -1:
#             painter = QPainter(self.viewport())
#             painter.setPen(Qt.NoPen)  # Pas de bordure
#             painter.setBrush(
#                 QColor(255, 0, 0, 50))  # Couleur de remplissage avec transparence (rouge avec 50% d'opacité)
#
#             # Obtenir le rectangle qui englobe toute la ligne
#             rect = self.visualRect(self.model().index(self.selectedRow, 0)).united(
#                 self.visualRect(self.model().index(self.selectedRow, self.columnCount() - 1))
#             )
#
#             # Dessiner un rectangle plein avec des bords arrondis
#             painter.drawRoundedRect(rect, 10, 10)  # 10 est le rayon des bords arrondis
#
#             # Appeler la méthode paintEvent par défaut à la fin
#         super().paintEvent(event)


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

        self.bdm_comboBox_type.addItems(os.listdir(ROOT_TYPE))
        self.bdm_comboBox_type.setCurrentText("3d")

        self.pushButton_openFolder.setIcon(QIcon("/home/fabrice/Dropbox/bin/icones/folder2.png"))
        self.pushButton_openFolder.setIconSize(QSize(24,24))

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

        self.bdm_comboBox_type.currentIndexChanged.connect(self.changed_bdm_comboBox_type)
        # self.listWidget_proj.clicked.connect(self.listWidget_proj_item_clicked)
        self.listWidget_fold.clicked.connect(self.listWidget_fold_item_clicked)
        self.listWidget_soft.clicked.connect(self.listWidget_soft_item_clicked)
        self.listWidget_fil1.clicked.connect(self.listWidget_fil1_item_clicked)
        self.listWidget_proj.itemClicked.connect(self.handle_item_click)


    def init(self, typ, prj, fld, sft):
        window.listWidget_proj.clear()
        window.listWidget_fold.clear()
        window.listWidget_soft.clear()
        window.listWidget_fil1.clear()
        window.listWidget_fil2.clear()

        self.fill_list_proj(typ.liste_item())
        fill_list_fold(prj.liste_item())
        fill_list_soft(fld.liste_item())
        fill_list_fil1(sft.liste_item())

    def fill_list_proj(self, items):

        n = 0
        for i in items:
            # Initialisation item
            item = QListWidgetItem(self.listWidget_proj)
            item.setSizeHint(QSize(150, 100))  # Taille de chaque élément

            # Création du widget pour chaque élément
            widget = QWidget()
            layout = QHBoxLayout(widget)

            # Ajout de l'image
            image_label = QLabel()
            image_path = typ.path() + "/" + i + "/screen/main.jpg"
            pixmap = QPixmap(image_path).scaled(QSize(150, 100), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            image_label.setPixmap(pixmap)
            layout.addWidget(image_label, alignment=Qt.AlignLeft)
            # image_label.setStyleSheet("border: 1px solid rgb(50,50,50); ")

            # image_label = QLabel()
            # image_path = typ.path() + "/" + i + "/screen/main.jpg"
            # rounded_pixmap = QPixmap(image_path).scaled(QSize(150, 100), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # image_label.setPixmap(rounded_pixmap)
            # image_label.setStyleSheet("border-radius: 50px;")
            # layout.addWidget(image_label, alignment=Qt.AlignLeft)

            # image_label = QLabel()
            # image_path = typ.path() + "/" + i + "/screen/main.jpg"
            #
            # rounded_pixmap = self.rounded_pixmap(image_path, QSize(150, 80))
            # image_label.setPixmap(rounded_pixmap)
            # layout.addWidget(image_label, alignment=Qt.AlignLeft)

            # pixmap = QPixmap(image_path)
            # pixmap = pixmap.scaled(QSize(150, 100), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # image_label.setPixmap(pixmap)
            # layout.addWidget(image_label, alignment=Qt.AlignLeft)




            # Ajout du nom
            name_label = QLabel(i)
            name_label.setFixedWidth(150)  # Largeur fixe
            layout.addWidget(name_label, alignment=Qt.AlignLeft)

            # Ajout de l'icône cliquable
            # icon_button = QPushButton("Cliquez moi")
            # icon_button.setFixedWidth(150)  # Largeur fixe
            # icon_button.clicked.connect(lambda: icon_click_handler(*icon_handler_args))
            # layout.addWidget(icon_button, alignment=Qt.AlignRight)

            self.listWidget_proj.setItemWidget(item, widget)
            item.setData(Qt.UserRole, widget)  # Sauvegarder le widget dans les données de l'élément


            # window.listWidget_proj.addItems(items)
            #
            # window.tableWidget.setColumnCount(3)
            # window.tableWidget.setRowCount(len(items))  # Ajout de cette ligne
            # window.tableWidget.setHorizontalHeaderLabels(['Projets', ''])
            # window.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
            # # window.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)  # Permet de sélectionner une seule cellule à la fois
            # window.tableWidget.setColumnWidth(0, 230)
            # window.tableWidget.setColumnWidth(1, 150)
            # window.tableWidget.setColumnWidth(2, 150)
            #
            #
            # # window.tableWidget.setStyleSheet("QTableWidget::item:selected { border: 2px solid red; }")
            #
            # # Masquer les en-têtes de colonnes et de lignes
            # window.tableWidget.horizontalHeader().hide()
            # window.tableWidget.verticalHeader().hide()




            # n=0
            # for i in items:
            #     window.tableWidget.setRowHeight(n, 112)
            #     image_path = typ.path() + "/" + i + "/screen/main.jpg"
            #     pixmap = QPixmap(image_path)
            #     pixmap = pixmap.scaledToWidth(200, Qt.SmoothTransformation)  # Utilisation de scaledToWidth pour redimensionner tout en conservant l'aspect d'origine
            #     image = QTableWidgetItem()
            #     image.setFlags(Qt.ItemIsEnabled)
            #     image.setData(Qt.DecorationRole, pixmap)
            #
            #     texte = QTableWidgetItem(i)
            #     t2 = QTableWidgetItem("ok")
            #
            #     # MyTableWidget(window.tableWidget)
            #
            #     window.tableWidget.setItem(n, 0, image)
            #     window.tableWidget.setItem(n, 1, texte)
            #     window.tableWidget.setItem(n, 2, t2)


    def handle_item_click(self, item):
        # Réinitialiser le style de tous les éléments
        for i in range(self.listWidget_proj.count()):
            current_item = self.listWidget_proj.item(i)
            if current_item is not None:
                widget = current_item.data(Qt.UserRole)
                if widget is not None:
                    widget.setStyleSheet("")

        # Appliquer le style à l'élément sélectionné
        widget = item.data(Qt.UserRole)
        widget.setStyleSheet("border-radius: 4px; border: none; background-color: rgb(0,125,255);")




    def icon_click_handler(arg1, arg2):
        print(f"Icône cliquée avec arguments: {arg1}, {arg2}")




    def onSelectionChanged(self, selected, deselected):
        # Gérer la sélection en dessinant un rectangle autour de la ligne sélectionnée
        if selected.indexes():
            self.selectedRow = selected.indexes()[0].row()
            # self.viewport().update()
        else:
            self.selectedRow = -1

    # def paintEvent(self, event):
    #     if window.tableWidget.selectedRow != -1:
    #         painter = QPainter(self.viewport())
    #         painter.setPen(Qt.NoPen)  # Pas de bordure
    #         painter.setBrush(
    #             QColor(255, 0, 0, 50))  # Couleur de remplissage avec transparence (rouge avec 50% d'opacité)
    #
    #         # Obtenir le rectangle qui englobe toute la ligne
    #         rect = self.visualRect(self.model().index(self.selectedRow, 0)).united(
    #             self.visualRect(self.model().index(self.selectedRow, self.columnCount() - 1))
    #         )
    #
    #         # Dessiner un rectangle plein avec des bords arrondis
    #         painter.drawRoundedRect(rect, 10, 10)  # 10 est le rayon des bords arrondis
    #
    #         # Appeler la méthode paintEvent par défaut à la fin
    #     super().paintEvent(event)











    def changed_bdm_comboBox_type(self):
        type_selected = window.bdm_comboBox_type.currentText()
        window.bdm_comboBox_type.setCurrentText(type_selected)

        run("type", type_selected, typ, prj, fld, sft)

        init(typ, prj, fld, sft )

    def listWidget_proj_item_clicked(self):
        tp = window.bdm_comboBox_type.currentText()

        proj_selected = window.listWidget_proj.currentItem().text()

        run('type', [tp, proj_selected], typ, prj, fld, sft)

        var(typ, prj, fld, sft)

        init(typ, prj, fld, sft)

    def listWidget_fold_item_clicked(self):
        tp = typ.current_name()
        pr = prj.current_name()


        fold_selected = window.listWidget_fold.currentItem().text()

        run('type', [tp, pr, fold_selected], typ, prj, fld, sft)

        var(typ, prj, fld, sft)

        init(typ, prj, fld, sft)

    def listWidget_soft_item_clicked(self):
        tp = typ.current_name()
        pr = prj.current_name()
        fl = fld.current_name()

        soft_selected = window.listWidget_soft.currentItem().text()

        run('type', [tp, pr, fl, soft_selected], typ, prj, fld, sft)

        var(typ, prj, fld, sft)

        init(typ, prj, fld, sft)

    def listWidget_fil1_item_clicked(self):
        pass

    def exit_program(self):  # Clique sur la liste des types
        exit()

    def explorer_TYPE(self):
        selected_type = self.treeWidget_TYPE.selectedItems()[0].text(0)

        os.system("nautilus " + typ.root() + "&")

    def test(self):
        print('ca marche!')




































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

    typ.set_current_name("3d")

    names = [typ.current_name(),prj.current_name(),fld.current_name(),sft.current_name()]

    step = run("type",names, typ, prj, fld, sft)
    window.init(typ, prj, fld, sft)

    # ==================================================================================================================

    window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec())

