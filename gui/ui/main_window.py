# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowUeYxPz.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1366, 1265)
        Form.setStyleSheet(u"/*QWidget{\n"
"	border-width: 0px; \n"
"    border-style: solid; \n"
"    border-color: rgb(0,0,0); \n"
"}\n"
"\n"
"QFrame{\n"
"	border-right-width: 1px; \n"
"    border-style: solid; \n"
"    border-color: rgb(0,0,0); \n"
"\n"
"}\n"
"QListView{\n"
"	border-width: 0px; \n"
"    border-style: solid; \n"
"    border-color: rgb(0,0,0); \n"
"}\n"
"QLabel{\n"
"	border-width: 0px; \n"
"    border-style: solid; \n"
"    border-color: rgb(0,0,0); \n"
"}*/")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_navigation = QWidget(Form)
        self.widget_navigation.setObjectName(u"widget_navigation")
        self.widget_navigation.setMinimumSize(QSize(1200, 600))
        self.gridLayout_widget_navigation = QGridLayout(self.widget_navigation)
        self.gridLayout_widget_navigation.setSpacing(0)
        self.gridLayout_widget_navigation.setObjectName(u"gridLayout_widget_navigation")
        self.gridLayout_widget_navigation.setContentsMargins(0, 0, 0, 0)
        self.frame_PROJET = QFrame(self.widget_navigation)
        self.frame_PROJET.setObjectName(u"frame_PROJET")
        self.frame_PROJET.setMinimumSize(QSize(0, 0))
        self.frame_PROJET.setFrameShape(QFrame.StyledPanel)
        self.frame_PROJET.setFrameShadow(QFrame.Raised)
        self.gridLayout_frame_PROJET = QGridLayout(self.frame_PROJET)
        self.gridLayout_frame_PROJET.setObjectName(u"gridLayout_frame_PROJET")
        self.gridLayout_frame_PROJET.setHorizontalSpacing(10)
        self.gridLayout_frame_PROJET.setVerticalSpacing(0)
        self.gridLayout_frame_PROJET.setContentsMargins(0, 0, 0, 0)
        self.frame_PROJET_liste = QFrame(self.frame_PROJET)
        self.frame_PROJET_liste.setObjectName(u"frame_PROJET_liste")
        self.frame_PROJET_liste.setFrameShape(QFrame.StyledPanel)
        self.frame_PROJET_liste.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_PROJET_liste)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 10, 0, 10)
        self.label_PROJET_liste = QLabel(self.frame_PROJET_liste)
        self.label_PROJET_liste.setObjectName(u"label_PROJET_liste")
        self.label_PROJET_liste.setMinimumSize(QSize(0, 35))
        self.label_PROJET_liste.setMaximumSize(QSize(16777215, 35))
        self.label_PROJET_liste.setMargin(0)
        self.label_PROJET_liste.setIndent(-1)

        self.verticalLayout.addWidget(self.label_PROJET_liste)

        self.treeWidget_PROJET = QTreeWidget(self.frame_PROJET_liste)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget_PROJET.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_PROJET.setObjectName(u"treeWidget_PROJET")
        self.treeWidget_PROJET.setEnabled(True)
        self.treeWidget_PROJET.setColumnCount(1)
        self.treeWidget_PROJET.header().setVisible(True)

        self.verticalLayout.addWidget(self.treeWidget_PROJET)


        self.gridLayout_frame_PROJET.addWidget(self.frame_PROJET_liste, 0, 0, 1, 1)

        self.frame_PROJET_buttons = QFrame(self.frame_PROJET)
        self.frame_PROJET_buttons.setObjectName(u"frame_PROJET_buttons")
        self.frame_PROJET_buttons.setMinimumSize(QSize(48, 0))
        self.frame_PROJET_buttons.setMaximumSize(QSize(48, 16777215))
        self.frame_PROJET_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_PROJET_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_frame_PROJET_buttons = QVBoxLayout(self.frame_PROJET_buttons)
        self.verticalLayout_frame_PROJET_buttons.setSpacing(0)
        self.verticalLayout_frame_PROJET_buttons.setObjectName(u"verticalLayout_frame_PROJET_buttons")
        self.verticalLayout_frame_PROJET_buttons.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_PROJET_buttons = QSpacerItem(20, 440, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_frame_PROJET_buttons.addItem(self.verticalSpacer_PROJET_buttons)

        self.pushButton_PROJET_explorer = QPushButton(self.frame_PROJET_buttons)
        self.pushButton_PROJET_explorer.setObjectName(u"pushButton_PROJET_explorer")
        self.pushButton_PROJET_explorer.setMinimumSize(QSize(48, 48))
        self.pushButton_PROJET_explorer.setMaximumSize(QSize(48, 48))
        icon = QIcon()
        icon.addFile(u"../icones/folder2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_PROJET_explorer.setIcon(icon)
        self.pushButton_PROJET_explorer.setIconSize(QSize(24, 24))

        self.verticalLayout_frame_PROJET_buttons.addWidget(self.pushButton_PROJET_explorer)


        self.gridLayout_frame_PROJET.addWidget(self.frame_PROJET_buttons, 0, 1, 1, 1)

        self.frame_PROJET_status = QFrame(self.frame_PROJET)
        self.frame_PROJET_status.setObjectName(u"frame_PROJET_status")
        self.frame_PROJET_status.setMinimumSize(QSize(0, 50))
        self.frame_PROJET_status.setMaximumSize(QSize(16777215, 50))
        self.frame_PROJET_status.setFrameShape(QFrame.StyledPanel)
        self.frame_PROJET_status.setFrameShadow(QFrame.Raised)
        self.gridLayout_frame_PROJET_status = QGridLayout(self.frame_PROJET_status)
        self.gridLayout_frame_PROJET_status.setObjectName(u"gridLayout_frame_PROJET_status")
        self.gridLayout_frame_PROJET_status.setHorizontalSpacing(10)
        self.gridLayout_frame_PROJET_status.setVerticalSpacing(8)
        self.gridLayout_frame_PROJET_status.setContentsMargins(10, 0, 10, 0)
        self.label_PROJET_status = QLabel(self.frame_PROJET_status)
        self.label_PROJET_status.setObjectName(u"label_PROJET_status")
        self.label_PROJET_status.setMinimumSize(QSize(0, 31))
        self.label_PROJET_status.setMaximumSize(QSize(16777215, 31))

        self.gridLayout_frame_PROJET_status.addWidget(self.label_PROJET_status, 0, 0, 1, 1)


        self.gridLayout_frame_PROJET.addWidget(self.frame_PROJET_status, 1, 0, 1, 2)


        self.gridLayout_widget_navigation.addWidget(self.frame_PROJET, 0, 1, 1, 1)

        self.frame_FOLDER = QFrame(self.widget_navigation)
        self.frame_FOLDER.setObjectName(u"frame_FOLDER")
        self.frame_FOLDER.setMinimumSize(QSize(0, 0))
        self.frame_FOLDER.setFrameShape(QFrame.StyledPanel)
        self.frame_FOLDER.setFrameShadow(QFrame.Raised)
        self.gridLayout_frame_FOLDER = QGridLayout(self.frame_FOLDER)
        self.gridLayout_frame_FOLDER.setObjectName(u"gridLayout_frame_FOLDER")
        self.gridLayout_frame_FOLDER.setHorizontalSpacing(10)
        self.gridLayout_frame_FOLDER.setVerticalSpacing(0)
        self.gridLayout_frame_FOLDER.setContentsMargins(0, 0, 0, 0)
        self.frame_FOLDER_liste = QFrame(self.frame_FOLDER)
        self.frame_FOLDER_liste.setObjectName(u"frame_FOLDER_liste")
        self.frame_FOLDER_liste.setFrameShape(QFrame.StyledPanel)
        self.frame_FOLDER_liste.setFrameShadow(QFrame.Raised)
        self.verticalLayout_frame_FOLDER_liste = QVBoxLayout(self.frame_FOLDER_liste)
        self.verticalLayout_frame_FOLDER_liste.setSpacing(10)
        self.verticalLayout_frame_FOLDER_liste.setObjectName(u"verticalLayout_frame_FOLDER_liste")
        self.verticalLayout_frame_FOLDER_liste.setContentsMargins(0, 10, 0, 10)
        self.label_FOLDER_liste = QLabel(self.frame_FOLDER_liste)
        self.label_FOLDER_liste.setObjectName(u"label_FOLDER_liste")
        self.label_FOLDER_liste.setMinimumSize(QSize(0, 35))
        self.label_FOLDER_liste.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_frame_FOLDER_liste.addWidget(self.label_FOLDER_liste)

        self.treeWidget_FOLDER = QTreeWidget(self.frame_FOLDER_liste)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.treeWidget_FOLDER.setHeaderItem(__qtreewidgetitem1)
        self.treeWidget_FOLDER.setObjectName(u"treeWidget_FOLDER")
        self.treeWidget_FOLDER.setColumnCount(1)
        self.treeWidget_FOLDER.header().setVisible(True)

        self.verticalLayout_frame_FOLDER_liste.addWidget(self.treeWidget_FOLDER)


        self.gridLayout_frame_FOLDER.addWidget(self.frame_FOLDER_liste, 0, 0, 1, 1)

        self.frame_FOLDER_buttons = QFrame(self.frame_FOLDER)
        self.frame_FOLDER_buttons.setObjectName(u"frame_FOLDER_buttons")
        self.frame_FOLDER_buttons.setMinimumSize(QSize(48, 0))
        self.frame_FOLDER_buttons.setMaximumSize(QSize(48, 16777215))
        self.frame_FOLDER_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_FOLDER_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_frame_FOLDER_buttons = QVBoxLayout(self.frame_FOLDER_buttons)
        self.verticalLayout_frame_FOLDER_buttons.setSpacing(0)
        self.verticalLayout_frame_FOLDER_buttons.setObjectName(u"verticalLayout_frame_FOLDER_buttons")
        self.verticalLayout_frame_FOLDER_buttons.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_FOLDER_buttons = QSpacerItem(20, 440, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_frame_FOLDER_buttons.addItem(self.verticalSpacer_FOLDER_buttons)

        self.pushButton_FOLDER_explorer = QPushButton(self.frame_FOLDER_buttons)
        self.pushButton_FOLDER_explorer.setObjectName(u"pushButton_FOLDER_explorer")
        self.pushButton_FOLDER_explorer.setMinimumSize(QSize(48, 48))
        self.pushButton_FOLDER_explorer.setMaximumSize(QSize(48, 48))
        self.pushButton_FOLDER_explorer.setIcon(icon)
        self.pushButton_FOLDER_explorer.setIconSize(QSize(24, 24))

        self.verticalLayout_frame_FOLDER_buttons.addWidget(self.pushButton_FOLDER_explorer)


        self.gridLayout_frame_FOLDER.addWidget(self.frame_FOLDER_buttons, 0, 1, 1, 1)

        self.frame_FOLDER_status = QFrame(self.frame_FOLDER)
        self.frame_FOLDER_status.setObjectName(u"frame_FOLDER_status")
        self.frame_FOLDER_status.setMinimumSize(QSize(0, 50))
        self.frame_FOLDER_status.setMaximumSize(QSize(16777215, 50))
        self.frame_FOLDER_status.setFrameShape(QFrame.StyledPanel)
        self.frame_FOLDER_status.setFrameShadow(QFrame.Raised)
        self.gridLayout_frame_FOLDER_status = QGridLayout(self.frame_FOLDER_status)
        self.gridLayout_frame_FOLDER_status.setSpacing(10)
        self.gridLayout_frame_FOLDER_status.setObjectName(u"gridLayout_frame_FOLDER_status")
        self.gridLayout_frame_FOLDER_status.setContentsMargins(10, 0, 10, 0)
        self.label_FOLDER_status = QLabel(self.frame_FOLDER_status)
        self.label_FOLDER_status.setObjectName(u"label_FOLDER_status")
        self.label_FOLDER_status.setMinimumSize(QSize(0, 31))
        self.label_FOLDER_status.setMaximumSize(QSize(16777215, 31))

        self.gridLayout_frame_FOLDER_status.addWidget(self.label_FOLDER_status, 0, 0, 1, 1)


        self.gridLayout_frame_FOLDER.addWidget(self.frame_FOLDER_status, 1, 0, 1, 2)


        self.gridLayout_widget_navigation.addWidget(self.frame_FOLDER, 0, 2, 1, 1)

        self.frame_TYPE = QFrame(self.widget_navigation)
        self.frame_TYPE.setObjectName(u"frame_TYPE")
        self.frame_TYPE.setMinimumSize(QSize(0, 0))
        self.frame_TYPE.setFrameShape(QFrame.StyledPanel)
        self.frame_TYPE.setFrameShadow(QFrame.Raised)
        self.gridLayout_frame_TYPE = QGridLayout(self.frame_TYPE)
        self.gridLayout_frame_TYPE.setObjectName(u"gridLayout_frame_TYPE")
        self.gridLayout_frame_TYPE.setHorizontalSpacing(10)
        self.gridLayout_frame_TYPE.setVerticalSpacing(0)
        self.gridLayout_frame_TYPE.setContentsMargins(0, 0, 0, 0)
        self.frame_TYPE_buttons = QFrame(self.frame_TYPE)
        self.frame_TYPE_buttons.setObjectName(u"frame_TYPE_buttons")
        self.frame_TYPE_buttons.setMinimumSize(QSize(48, 0))
        self.frame_TYPE_buttons.setMaximumSize(QSize(48, 16777215))
        self.frame_TYPE_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_TYPE_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_frame_TYPE_buttons = QVBoxLayout(self.frame_TYPE_buttons)
        self.verticalLayout_frame_TYPE_buttons.setSpacing(0)
        self.verticalLayout_frame_TYPE_buttons.setObjectName(u"verticalLayout_frame_TYPE_buttons")
        self.verticalLayout_frame_TYPE_buttons.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_TYPE_buttons = QSpacerItem(20, 615, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_frame_TYPE_buttons.addItem(self.verticalSpacer_TYPE_buttons)

        self.pushButton_TYPE_explorer = QPushButton(self.frame_TYPE_buttons)
        self.pushButton_TYPE_explorer.setObjectName(u"pushButton_TYPE_explorer")
        self.pushButton_TYPE_explorer.setMinimumSize(QSize(48, 48))
        self.pushButton_TYPE_explorer.setMaximumSize(QSize(48, 48))
        icon1 = QIcon(QIcon.fromTheme(u"user-desktop"))
        self.pushButton_TYPE_explorer.setIcon(icon1)
        self.pushButton_TYPE_explorer.setIconSize(QSize(24, 24))

        self.verticalLayout_frame_TYPE_buttons.addWidget(self.pushButton_TYPE_explorer)


        self.gridLayout_frame_TYPE.addWidget(self.frame_TYPE_buttons, 0, 1, 1, 1)

        self.frame_TYPE_status = QFrame(self.frame_TYPE)
        self.frame_TYPE_status.setObjectName(u"frame_TYPE_status")
        self.frame_TYPE_status.setMinimumSize(QSize(0, 50))
        self.frame_TYPE_status.setMaximumSize(QSize(16777215, 50))
        self.frame_TYPE_status.setFrameShape(QFrame.StyledPanel)
        self.frame_TYPE_status.setFrameShadow(QFrame.Raised)
        self.gridLayout_frame_TYPE_status = QGridLayout(self.frame_TYPE_status)
        self.gridLayout_frame_TYPE_status.setSpacing(10)
        self.gridLayout_frame_TYPE_status.setObjectName(u"gridLayout_frame_TYPE_status")
        self.gridLayout_frame_TYPE_status.setContentsMargins(10, 0, 10, 0)
        self.label_TYPE_status = QLabel(self.frame_TYPE_status)
        self.label_TYPE_status.setObjectName(u"label_TYPE_status")
        self.label_TYPE_status.setMinimumSize(QSize(0, 31))
        self.label_TYPE_status.setMaximumSize(QSize(16777215, 31))

        self.gridLayout_frame_TYPE_status.addWidget(self.label_TYPE_status, 0, 0, 1, 1)


        self.gridLayout_frame_TYPE.addWidget(self.frame_TYPE_status, 1, 0, 1, 2)

        self.frame_TYPE_liste = QFrame(self.frame_TYPE)
        self.frame_TYPE_liste.setObjectName(u"frame_TYPE_liste")
        self.frame_TYPE_liste.setFrameShape(QFrame.StyledPanel)
        self.frame_TYPE_liste.setFrameShadow(QFrame.Raised)
        self.verticalLayout_frame_TYPE_liste = QVBoxLayout(self.frame_TYPE_liste)
        self.verticalLayout_frame_TYPE_liste.setSpacing(10)
        self.verticalLayout_frame_TYPE_liste.setObjectName(u"verticalLayout_frame_TYPE_liste")
        self.verticalLayout_frame_TYPE_liste.setContentsMargins(0, 10, 0, 10)
        self.label_TYPE_liste = QLabel(self.frame_TYPE_liste)
        self.label_TYPE_liste.setObjectName(u"label_TYPE_liste")
        self.label_TYPE_liste.setMinimumSize(QSize(0, 35))
        self.label_TYPE_liste.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_frame_TYPE_liste.addWidget(self.label_TYPE_liste)

        self.treeWidget_TYPE = QTreeWidget(self.frame_TYPE_liste)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setText(0, u"1");
        self.treeWidget_TYPE.setHeaderItem(__qtreewidgetitem2)
        self.treeWidget_TYPE.setObjectName(u"treeWidget_TYPE")
        self.treeWidget_TYPE.setColumnCount(1)
        self.treeWidget_TYPE.header().setVisible(True)

        self.verticalLayout_frame_TYPE_liste.addWidget(self.treeWidget_TYPE)


        self.gridLayout_frame_TYPE.addWidget(self.frame_TYPE_liste, 0, 0, 1, 1)


        self.gridLayout_widget_navigation.addWidget(self.frame_TYPE, 0, 0, 1, 1)

        self.frame_SOFT = QFrame(self.widget_navigation)
        self.frame_SOFT.setObjectName(u"frame_SOFT")
        self.frame_SOFT.setMinimumSize(QSize(0, 0))
        self.frame_SOFT.setFrameShape(QFrame.StyledPanel)
        self.frame_SOFT.setFrameShadow(QFrame.Raised)
        self.gridLayout_frame_SOFT = QGridLayout(self.frame_SOFT)
        self.gridLayout_frame_SOFT.setObjectName(u"gridLayout_frame_SOFT")
        self.gridLayout_frame_SOFT.setHorizontalSpacing(10)
        self.gridLayout_frame_SOFT.setVerticalSpacing(0)
        self.gridLayout_frame_SOFT.setContentsMargins(0, 0, 0, 0)
        self.frame_SOFT_status = QFrame(self.frame_SOFT)
        self.frame_SOFT_status.setObjectName(u"frame_SOFT_status")
        self.frame_SOFT_status.setMinimumSize(QSize(0, 50))
        self.frame_SOFT_status.setMaximumSize(QSize(16777215, 50))
        self.frame_SOFT_status.setFrameShape(QFrame.StyledPanel)
        self.frame_SOFT_status.setFrameShadow(QFrame.Raised)
        self.gridLayout_frame_SOFT_status = QGridLayout(self.frame_SOFT_status)
        self.gridLayout_frame_SOFT_status.setSpacing(10)
        self.gridLayout_frame_SOFT_status.setObjectName(u"gridLayout_frame_SOFT_status")
        self.gridLayout_frame_SOFT_status.setContentsMargins(10, 0, 10, 0)
        self.label_SOFT_status = QLabel(self.frame_SOFT_status)
        self.label_SOFT_status.setObjectName(u"label_SOFT_status")
        self.label_SOFT_status.setMinimumSize(QSize(0, 31))
        self.label_SOFT_status.setMaximumSize(QSize(16777215, 31))

        self.gridLayout_frame_SOFT_status.addWidget(self.label_SOFT_status, 0, 0, 1, 1)


        self.gridLayout_frame_SOFT.addWidget(self.frame_SOFT_status, 1, 0, 1, 2)

        self.frame_SOFT_buttons = QFrame(self.frame_SOFT)
        self.frame_SOFT_buttons.setObjectName(u"frame_SOFT_buttons")
        self.frame_SOFT_buttons.setMinimumSize(QSize(48, 0))
        self.frame_SOFT_buttons.setMaximumSize(QSize(48, 16777215))
        self.frame_SOFT_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_SOFT_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_frame_SOFT_buttons = QVBoxLayout(self.frame_SOFT_buttons)
        self.verticalLayout_frame_SOFT_buttons.setSpacing(0)
        self.verticalLayout_frame_SOFT_buttons.setObjectName(u"verticalLayout_frame_SOFT_buttons")
        self.verticalLayout_frame_SOFT_buttons.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_SOFT_buttons = QSpacerItem(20, 440, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_frame_SOFT_buttons.addItem(self.verticalSpacer_SOFT_buttons)

        self.pushButton_SOFT_explorer = QPushButton(self.frame_SOFT_buttons)
        self.pushButton_SOFT_explorer.setObjectName(u"pushButton_SOFT_explorer")
        self.pushButton_SOFT_explorer.setMinimumSize(QSize(48, 48))
        self.pushButton_SOFT_explorer.setMaximumSize(QSize(48, 48))
        self.pushButton_SOFT_explorer.setIcon(icon)
        self.pushButton_SOFT_explorer.setIconSize(QSize(24, 24))

        self.verticalLayout_frame_SOFT_buttons.addWidget(self.pushButton_SOFT_explorer)


        self.gridLayout_frame_SOFT.addWidget(self.frame_SOFT_buttons, 0, 1, 1, 1)

        self.frame_SOFT_liste = QFrame(self.frame_SOFT)
        self.frame_SOFT_liste.setObjectName(u"frame_SOFT_liste")
        self.frame_SOFT_liste.setFrameShape(QFrame.StyledPanel)
        self.frame_SOFT_liste.setFrameShadow(QFrame.Raised)
        self.verticalLayout_frame_SOFT_liste = QVBoxLayout(self.frame_SOFT_liste)
        self.verticalLayout_frame_SOFT_liste.setSpacing(10)
        self.verticalLayout_frame_SOFT_liste.setObjectName(u"verticalLayout_frame_SOFT_liste")
        self.verticalLayout_frame_SOFT_liste.setContentsMargins(0, 10, 0, 10)
        self.label_SOFT_liste = QLabel(self.frame_SOFT_liste)
        self.label_SOFT_liste.setObjectName(u"label_SOFT_liste")
        self.label_SOFT_liste.setMinimumSize(QSize(0, 35))
        self.label_SOFT_liste.setMaximumSize(QSize(16777215, 35))
        self.label_SOFT_liste.setLineWidth(1)

        self.verticalLayout_frame_SOFT_liste.addWidget(self.label_SOFT_liste)

        self.treeWidget_SOFT = QTreeWidget(self.frame_SOFT_liste)
        __qtreewidgetitem3 = QTreeWidgetItem()
        __qtreewidgetitem3.setText(0, u"1");
        self.treeWidget_SOFT.setHeaderItem(__qtreewidgetitem3)
        self.treeWidget_SOFT.setObjectName(u"treeWidget_SOFT")
        self.treeWidget_SOFT.setColumnCount(1)
        self.treeWidget_SOFT.header().setVisible(True)

        self.verticalLayout_frame_SOFT_liste.addWidget(self.treeWidget_SOFT)


        self.gridLayout_frame_SOFT.addWidget(self.frame_SOFT_liste, 0, 0, 1, 1)


        self.gridLayout_widget_navigation.addWidget(self.frame_SOFT, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.widget_navigation, 0, 0, 1, 1)

        self.widget_buttons = QWidget(Form)
        self.widget_buttons.setObjectName(u"widget_buttons")
        self.verticalLayout_2 = QVBoxLayout(self.widget_buttons)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalSpacer = QSpacerItem(20, 1227, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton_job = QPushButton(self.widget_buttons)
        self.pushButton_job.setObjectName(u"pushButton_job")
        self.pushButton_job.setMinimumSize(QSize(48, 48))
        self.pushButton_job.setMaximumSize(QSize(48, 48))
        icon2 = QIcon()
        icon2.addFile(u"../icones/terminal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_job.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.pushButton_job)

        self.pushButton_exit = QPushButton(self.widget_buttons)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setMinimumSize(QSize(48, 48))
        self.pushButton_exit.setMaximumSize(QSize(48, 48))
        icon3 = QIcon()
        iconThemeName = u"exit"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.pushButton_exit.setIcon(icon3)
        self.pushButton_exit.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.pushButton_exit)


        self.gridLayout.addWidget(self.widget_buttons, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_PROJET_liste.setText(QCoreApplication.translate("Form", u"Projet :", None))
        self.pushButton_PROJET_explorer.setText("")
        self.label_PROJET_status.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_FOLDER_liste.setText(QCoreApplication.translate("Form", u"Sous repertoire :", None))
        self.pushButton_FOLDER_explorer.setText("")
        self.label_FOLDER_status.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton_TYPE_explorer.setText("")
        self.label_TYPE_status.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_TYPE_liste.setText(QCoreApplication.translate("Form", u"Type :", None))
        self.label_SOFT_status.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton_SOFT_explorer.setText("")
        self.label_SOFT_liste.setText(QCoreApplication.translate("Form", u"Soft :", None))
        self.pushButton_job.setText("")
        self.pushButton_exit.setText("")
    # retranslateUi

