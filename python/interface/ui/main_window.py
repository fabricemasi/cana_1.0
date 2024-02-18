# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1548, 1546)
        Form.setMinimumSize(QSize(930, 0))
        font = QFont()
        font.setFamilies([u"Inter"])
        Form.setFont(font)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"QWidget{\n"
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
"}")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_toolbox = QFrame(Form)
        self.frame_toolbox.setObjectName(u"frame_toolbox")
        self.frame_toolbox.setMinimumSize(QSize(900, 50))
        self.frame_toolbox.setFrameShape(QFrame.StyledPanel)
        self.frame_toolbox.setFrameShadow(QFrame.Raised)
        self.frame_toolbox_layout = QHBoxLayout(self.frame_toolbox)
        self.frame_toolbox_layout.setSpacing(10)
        self.frame_toolbox_layout.setObjectName(u"frame_toolbox_layout")
        self.frame_toolbox_layout.setContentsMargins(10, 0, 10, 0)
        self.bdm_label_01 = QLabel(self.frame_toolbox)
        self.bdm_label_01.setObjectName(u"bdm_label_01")

        self.frame_toolbox_layout.addWidget(self.bdm_label_01)

        self.bdm_comboBox_type = QComboBox(self.frame_toolbox)
        self.bdm_comboBox_type.setObjectName(u"bdm_comboBox_type")
        self.bdm_comboBox_type.setMinimumSize(QSize(200, 32))

        self.frame_toolbox_layout.addWidget(self.bdm_comboBox_type)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.frame_toolbox_layout.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.frame_toolbox, 0, 0, 1, 3)

        self.frame_proj = QFrame(Form)
        self.frame_proj.setObjectName(u"frame_proj")
        self.frame_proj.setMinimumSize(QSize(552, 0))
        self.frame_proj.setMaximumSize(QSize(552, 16777215))
        self.frame_proj.setFrameShape(QFrame.StyledPanel)
        self.frame_proj.setFrameShadow(QFrame.Raised)
        self.frame_proj_layout = QVBoxLayout(self.frame_proj)
        self.frame_proj_layout.setObjectName(u"frame_proj_layout")
        self.listWidget_proj = QListWidget(self.frame_proj)
        self.listWidget_proj.setObjectName(u"listWidget_proj")

        self.frame_proj_layout.addWidget(self.listWidget_proj)


        self.gridLayout.addWidget(self.frame_proj, 1, 0, 1, 1)

        self.frame_fold = QFrame(Form)
        self.frame_fold.setObjectName(u"frame_fold")
        self.frame_fold.setMinimumSize(QSize(552, 0))
        self.frame_fold.setMaximumSize(QSize(552, 16777215))
        self.frame_fold.setFrameShape(QFrame.StyledPanel)
        self.frame_fold.setFrameShadow(QFrame.Raised)
        self.frame_fold_layout = QVBoxLayout(self.frame_fold)
        self.frame_fold_layout.setObjectName(u"frame_fold_layout")
        self.image_proj = QLabel(self.frame_fold)
        self.image_proj.setObjectName(u"image_proj")
        self.image_proj.setMaximumSize(QSize(16777215, 400))

        self.frame_fold_layout.addWidget(self.image_proj)

        self.frame = QFrame(self.frame_fold)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 138))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.fold_label_01 = QLabel(self.frame)
        self.fold_label_01.setObjectName(u"fold_label_01")
        self.fold_label_01.setGeometry(QRect(110, 10, 411, 41))
        self.fold_pushButton_retour = QPushButton(self.frame)
        self.fold_pushButton_retour.setObjectName(u"fold_pushButton_retour")
        self.fold_pushButton_retour.setGeometry(QRect(10, 10, 89, 41))

        self.frame_fold_layout.addWidget(self.frame)

        self.listWidget_fold = QListWidget(self.frame_fold)
        self.listWidget_fold.setObjectName(u"listWidget_fold")

        self.frame_fold_layout.addWidget(self.listWidget_fold)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.frame_fold_layout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.frame_fold, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(200, 200, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.bdm_label_01.setText(QCoreApplication.translate("Form", u"Type :", None))
        self.image_proj.setText(QCoreApplication.translate("Form", u"image_proj", None))
        self.fold_label_01.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.fold_pushButton_retour.setText(QCoreApplication.translate("Form", u"Retour", None))
    # retranslateUi

