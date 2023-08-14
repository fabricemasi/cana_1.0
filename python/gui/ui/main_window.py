# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(2192, 1435)
        font = QFont()
        font.setFamilies([u"Inter"])
        Form.setFont(font)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"/*QWidget{\n"
"	border-width: 3px; \n"
"    border-style: solid; \n"
"    border-color: rgb(0,0,0); \n"
"}\n"
"\n"
"QFrame{\n"
"	border-right-width: 1px; \n"
"    border-style: solid; \n"
"    border-color: rgb(225,225,225); \n"
"\n"
"}\n"
"QTreeView{\n"
"	border-width: 1px; \n"
"    border-style: solid; \n"
"    border-color: rgb(0,0,225); \n"
"}\n"
"QLabel{\n"
"	border-width: 1px; \n"
"    border-style: solid; \n"
"    border-color: rgb(225,0,0); \n"
"}\n"
"QPushButton{\n"
"	border-width: 1px; \n"
"    border-style: solid; \n"
"    border-color: rgb(0,225,0); \n"
"}*/")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_navigation = QWidget(Form)
        self.widget_navigation.setObjectName(u"widget_navigation")
        self.widget_navigation.setMinimumSize(QSize(1200, 300))
        self.widget_navigation.setMaximumSize(QSize(16777215, 600))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_navigation)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        self.pushButton_TYPE_explorer = QPushButton(self.frame_TYPE_buttons)
        self.pushButton_TYPE_explorer.setObjectName(u"pushButton_TYPE_explorer")
        self.pushButton_TYPE_explorer.setMinimumSize(QSize(48, 48))
        self.pushButton_TYPE_explorer.setMaximumSize(QSize(48, 48))
        icon = QIcon()
        iconThemeName = u"user-desktop"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.pushButton_TYPE_explorer.setIcon(icon)
        self.pushButton_TYPE_explorer.setIconSize(QSize(24, 24))

        self.verticalLayout_frame_TYPE_buttons.addWidget(self.pushButton_TYPE_explorer)

        self.verticalSpacer_TYPE_buttons = QSpacerItem(20, 615, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_frame_TYPE_buttons.addItem(self.verticalSpacer_TYPE_buttons)


        self.gridLayout_frame_TYPE.addWidget(self.frame_TYPE_buttons, 0, 1, 1, 1)

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
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget_TYPE.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_TYPE.setObjectName(u"treeWidget_TYPE")
        self.treeWidget_TYPE.setColumnCount(1)
        self.treeWidget_TYPE.header().setVisible(True)

        self.verticalLayout_frame_TYPE_liste.addWidget(self.treeWidget_TYPE)


        self.gridLayout_frame_TYPE.addWidget(self.frame_TYPE_liste, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_TYPE)

        self.frame_PROJ = QFrame(self.widget_navigation)
        self.frame_PROJ.setObjectName(u"frame_PROJ")
        self.frame_PROJ.setMinimumSize(QSize(0, 0))
        self.frame_PROJ.setFrameShape(QFrame.StyledPanel)
        self.frame_PROJ.setFrameShadow(QFrame.Raised)
        self.gridLayout_frame_PROJ = QGridLayout(self.frame_PROJ)
        self.gridLayout_frame_PROJ.setObjectName(u"gridLayout_frame_PROJ")
        self.gridLayout_frame_PROJ.setHorizontalSpacing(10)
        self.gridLayout_frame_PROJ.setVerticalSpacing(0)
        self.gridLayout_frame_PROJ.setContentsMargins(0, 0, 0, 0)
        self.frame_PROJ_liste = QFrame(self.frame_PROJ)
        self.frame_PROJ_liste.setObjectName(u"frame_PROJ_liste")
        self.frame_PROJ_liste.setFrameShape(QFrame.StyledPanel)
        self.frame_PROJ_liste.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_PROJ_liste)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 10, 0, 10)
        self.label_PROJ_liste = QLabel(self.frame_PROJ_liste)
        self.label_PROJ_liste.setObjectName(u"label_PROJ_liste")
        self.label_PROJ_liste.setMinimumSize(QSize(0, 35))
        self.label_PROJ_liste.setMaximumSize(QSize(16777215, 35))
        self.label_PROJ_liste.setMargin(0)
        self.label_PROJ_liste.setIndent(-1)

        self.verticalLayout.addWidget(self.label_PROJ_liste)

        self.treeWidget_PROJ = QTreeWidget(self.frame_PROJ_liste)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.treeWidget_PROJ.setHeaderItem(__qtreewidgetitem1)
        self.treeWidget_PROJ.setObjectName(u"treeWidget_PROJ")
        self.treeWidget_PROJ.setEnabled(True)
        self.treeWidget_PROJ.setColumnCount(1)
        self.treeWidget_PROJ.header().setVisible(True)

        self.verticalLayout.addWidget(self.treeWidget_PROJ)


        self.gridLayout_frame_PROJ.addWidget(self.frame_PROJ_liste, 0, 0, 1, 1)

        self.frame_PROJ_buttons = QFrame(self.frame_PROJ)
        self.frame_PROJ_buttons.setObjectName(u"frame_PROJ_buttons")
        self.frame_PROJ_buttons.setMinimumSize(QSize(48, 0))
        self.frame_PROJ_buttons.setMaximumSize(QSize(48, 16777215))
        self.frame_PROJ_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_PROJ_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_frame_PROJ_buttons = QVBoxLayout(self.frame_PROJ_buttons)
        self.verticalLayout_frame_PROJ_buttons.setSpacing(0)
        self.verticalLayout_frame_PROJ_buttons.setObjectName(u"verticalLayout_frame_PROJ_buttons")
        self.verticalLayout_frame_PROJ_buttons.setContentsMargins(0, 0, 0, 0)
        self.pushButton_PROJ_explorer = QPushButton(self.frame_PROJ_buttons)
        self.pushButton_PROJ_explorer.setObjectName(u"pushButton_PROJ_explorer")
        self.pushButton_PROJ_explorer.setMinimumSize(QSize(48, 48))
        self.pushButton_PROJ_explorer.setMaximumSize(QSize(48, 48))
        icon1 = QIcon()
        icon1.addFile(u"../icones/fold2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_PROJ_explorer.setIcon(icon1)
        self.pushButton_PROJ_explorer.setIconSize(QSize(24, 24))

        self.verticalLayout_frame_PROJ_buttons.addWidget(self.pushButton_PROJ_explorer)

        self.verticalSpacer_PROJ_buttons = QSpacerItem(20, 440, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_frame_PROJ_buttons.addItem(self.verticalSpacer_PROJ_buttons)


        self.gridLayout_frame_PROJ.addWidget(self.frame_PROJ_buttons, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_PROJ)

        self.frame_FOLD = QFrame(self.widget_navigation)
        self.frame_FOLD.setObjectName(u"frame_FOLD")
        self.frame_FOLD.setMinimumSize(QSize(0, 0))
        self.frame_FOLD.setFrameShape(QFrame.StyledPanel)
        self.frame_FOLD.setFrameShadow(QFrame.Raised)
        self.gridLayout_frame_FOLD = QGridLayout(self.frame_FOLD)
        self.gridLayout_frame_FOLD.setObjectName(u"gridLayout_frame_FOLD")
        self.gridLayout_frame_FOLD.setHorizontalSpacing(10)
        self.gridLayout_frame_FOLD.setVerticalSpacing(0)
        self.gridLayout_frame_FOLD.setContentsMargins(0, 0, 0, 0)
        self.frame_FOLD_liste = QFrame(self.frame_FOLD)
        self.frame_FOLD_liste.setObjectName(u"frame_FOLD_liste")
        self.frame_FOLD_liste.setFrameShape(QFrame.StyledPanel)
        self.frame_FOLD_liste.setFrameShadow(QFrame.Raised)
        self.verticalLayout_frame_FOLD_liste = QVBoxLayout(self.frame_FOLD_liste)
        self.verticalLayout_frame_FOLD_liste.setSpacing(10)
        self.verticalLayout_frame_FOLD_liste.setObjectName(u"verticalLayout_frame_FOLD_liste")
        self.verticalLayout_frame_FOLD_liste.setContentsMargins(0, 10, 0, 10)
        self.label_FOLD_liste = QLabel(self.frame_FOLD_liste)
        self.label_FOLD_liste.setObjectName(u"label_FOLD_liste")
        self.label_FOLD_liste.setMinimumSize(QSize(0, 35))
        self.label_FOLD_liste.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_frame_FOLD_liste.addWidget(self.label_FOLD_liste)

        self.treeWidget_FOLD = QTreeWidget(self.frame_FOLD_liste)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setText(0, u"1");
        self.treeWidget_FOLD.setHeaderItem(__qtreewidgetitem2)
        self.treeWidget_FOLD.setObjectName(u"treeWidget_FOLD")
        self.treeWidget_FOLD.setColumnCount(1)
        self.treeWidget_FOLD.header().setVisible(True)

        self.verticalLayout_frame_FOLD_liste.addWidget(self.treeWidget_FOLD)


        self.gridLayout_frame_FOLD.addWidget(self.frame_FOLD_liste, 0, 0, 1, 1)

        self.frame_FOLD_buttons = QFrame(self.frame_FOLD)
        self.frame_FOLD_buttons.setObjectName(u"frame_FOLD_buttons")
        self.frame_FOLD_buttons.setMinimumSize(QSize(48, 0))
        self.frame_FOLD_buttons.setMaximumSize(QSize(48, 16777215))
        self.frame_FOLD_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_FOLD_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_frame_FOLD_buttons = QVBoxLayout(self.frame_FOLD_buttons)
        self.verticalLayout_frame_FOLD_buttons.setSpacing(0)
        self.verticalLayout_frame_FOLD_buttons.setObjectName(u"verticalLayout_frame_FOLD_buttons")
        self.verticalLayout_frame_FOLD_buttons.setContentsMargins(0, 0, 0, 0)
        self.pushButton_FOLD_explorer = QPushButton(self.frame_FOLD_buttons)
        self.pushButton_FOLD_explorer.setObjectName(u"pushButton_FOLD_explorer")
        self.pushButton_FOLD_explorer.setMinimumSize(QSize(48, 48))
        self.pushButton_FOLD_explorer.setMaximumSize(QSize(48, 48))
        self.pushButton_FOLD_explorer.setIcon(icon1)
        self.pushButton_FOLD_explorer.setIconSize(QSize(24, 24))

        self.verticalLayout_frame_FOLD_buttons.addWidget(self.pushButton_FOLD_explorer)

        self.verticalSpacer_FOLD_buttons = QSpacerItem(20, 440, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_frame_FOLD_buttons.addItem(self.verticalSpacer_FOLD_buttons)


        self.gridLayout_frame_FOLD.addWidget(self.frame_FOLD_buttons, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_FOLD)


        self.gridLayout_2.addWidget(self.widget_navigation, 0, 0, 1, 1)

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


        self.gridLayout_2.addWidget(self.widget_buttons, 0, 1, 2, 1)

        self.widget_W03 = QWidget(Form)
        self.widget_W03.setObjectName(u"widget_W03")
        self.gridLayout = QGridLayout(self.widget_W03)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_W03_F01 = QFrame(self.widget_W03)
        self.frame_W03_F01.setObjectName(u"frame_W03_F01")
        self.frame_W03_F01.setMinimumSize(QSize(250, 0))
        self.frame_W03_F01.setMaximumSize(QSize(250, 16777215))
        self.frame_W03_F01.setFrameShape(QFrame.StyledPanel)
        self.frame_W03_F01.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_W03_F01)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_SOFT = QFrame(self.frame_W03_F01)
        self.frame_SOFT.setObjectName(u"frame_SOFT")
        self.frame_SOFT.setMinimumSize(QSize(0, 0))
        self.frame_SOFT.setFrameShape(QFrame.StyledPanel)
        self.frame_SOFT.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_SOFT)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
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


        self.horizontalLayout.addWidget(self.frame_SOFT_liste)

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
        self.pushButton_SOFT_explorer = QPushButton(self.frame_SOFT_buttons)
        self.pushButton_SOFT_explorer.setObjectName(u"pushButton_SOFT_explorer")
        self.pushButton_SOFT_explorer.setMinimumSize(QSize(48, 48))
        self.pushButton_SOFT_explorer.setMaximumSize(QSize(48, 48))
        self.pushButton_SOFT_explorer.setIcon(icon1)
        self.pushButton_SOFT_explorer.setIconSize(QSize(24, 24))

        self.verticalLayout_frame_SOFT_buttons.addWidget(self.pushButton_SOFT_explorer)

        self.verticalSpacer_SOFT_buttons = QSpacerItem(20, 440, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_frame_SOFT_buttons.addItem(self.verticalSpacer_SOFT_buttons)


        self.horizontalLayout.addWidget(self.frame_SOFT_buttons)


        self.verticalLayout_3.addWidget(self.frame_SOFT)


        self.gridLayout.addWidget(self.frame_W03_F01, 0, 0, 2, 1)

        self.frame = QFrame(self.widget_W03)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 71))
        self.frame.setMaximumSize(QSize(16777215, 71))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_W03_proj = QLabel(self.frame)
        self.label_W03_proj.setObjectName(u"label_W03_proj")
        self.label_W03_proj.setGeometry(QRect(10, 10, 461, 50))
        self.label_W03_proj.setMinimumSize(QSize(0, 50))
        self.label_W03_proj.setMaximumSize(QSize(16777215, 50))

        self.gridLayout.addWidget(self.frame, 0, 1, 1, 2)

        self.frame_W03_F02 = QFrame(self.widget_W03)
        self.frame_W03_F02.setObjectName(u"frame_W03_F02")
        self.frame_W03_F02.setMinimumSize(QSize(72, 0))
        self.frame_W03_F02.setMaximumSize(QSize(72, 16777215))
        self.frame_W03_F02.setFrameShape(QFrame.StyledPanel)
        self.frame_W03_F02.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_W03_F02)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.pushButton_W03_ref = QPushButton(self.frame_W03_F02)
        self.pushButton_W03_ref.setObjectName(u"pushButton_W03_ref")
        self.pushButton_W03_ref.setMinimumSize(QSize(48, 48))
        self.pushButton_W03_ref.setMaximumSize(QSize(48, 48))

        self.verticalLayout_4.addWidget(self.pushButton_W03_ref)

        self.pushButton_W03_pur = QPushButton(self.frame_W03_F02)
        self.pushButton_W03_pur.setObjectName(u"pushButton_W03_pur")
        self.pushButton_W03_pur.setMinimumSize(QSize(48, 48))
        self.pushButton_W03_pur.setMaximumSize(QSize(48, 48))

        self.verticalLayout_4.addWidget(self.pushButton_W03_pur)

        self.verticalSpacer_3 = QSpacerItem(20, 786, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.gridLayout.addWidget(self.frame_W03_F02, 0, 3, 2, 1)

        self.frame_2 = QFrame(self.widget_W03)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(500, 0))
        self.frame_2.setMaximumSize(QSize(500, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.treeWidget_W03_workfiles = QTreeWidget(self.frame_2)
        __qtreewidgetitem4 = QTreeWidgetItem()
        __qtreewidgetitem4.setText(0, u"1");
        self.treeWidget_W03_workfiles.setHeaderItem(__qtreewidgetitem4)
        self.treeWidget_W03_workfiles.setObjectName(u"treeWidget_W03_workfiles")
        self.treeWidget_W03_workfiles.setColumnCount(1)
        self.treeWidget_W03_workfiles.header().setVisible(True)

        self.verticalLayout_5.addWidget(self.treeWidget_W03_workfiles)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 100))
        self.label.setMaximumSize(QSize(16777215, 100))
        self.label.setPixmap(QPixmap(u"../../../../Images/adam-wesierski-trainstation-breakdown-artstation-v003.jpg"))
        self.label.setScaledContents(False)

        self.verticalLayout_5.addWidget(self.label)


        self.gridLayout.addWidget(self.frame_2, 1, 1, 1, 1)

        self.frame_3 = QFrame(self.widget_W03)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.widget_W03, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_TYPE_explorer.setText("")
        self.label_TYPE_liste.setText(QCoreApplication.translate("Form", u"Type :", None))
        self.label_PROJ_liste.setText(QCoreApplication.translate("Form", u"Proj :", None))
        self.pushButton_PROJ_explorer.setText("")
        self.label_FOLD_liste.setText(QCoreApplication.translate("Form", u"Sous repertoire :", None))
        self.pushButton_FOLD_explorer.setText("")
        self.pushButton_job.setText("")
        self.pushButton_exit.setText("")
        self.label_SOFT_liste.setText(QCoreApplication.translate("Form", u"Soft :", None))
        self.pushButton_SOFT_explorer.setText("")
        self.label_W03_proj.setText(QCoreApplication.translate("Form", u"Arrete de mentir, c'est moi !!!!!!!!!!!!", None))
        self.pushButton_W03_ref.setText(QCoreApplication.translate("Form", u"Ref", None))
        self.pushButton_W03_pur.setText(QCoreApplication.translate("Form", u"Pur", None))
        self.label.setText("")
    # retranslateUi

