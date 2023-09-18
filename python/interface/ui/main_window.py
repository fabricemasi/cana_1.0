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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(714, 1276)
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
        self.widget_navigation = QWidget(Form)
        self.widget_navigation.setObjectName(u"widget_navigation")
        self.widget_navigation.setGeometry(QRect(10, 20, 671, 1241))
        self.treeWidget_navigation = QTreeWidget(self.widget_navigation)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget_navigation.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_navigation.setObjectName(u"treeWidget_navigation")
        self.treeWidget_navigation.setGeometry(QRect(20, 160, 631, 671))
        self.widget_fil_ariane = QWidget(self.widget_navigation)
        self.widget_fil_ariane.setObjectName(u"widget_fil_ariane")
        self.widget_fil_ariane.setGeometry(QRect(19, 80, 631, 37))
        self.horizontalLayout = QHBoxLayout(self.widget_fil_ariane)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_type = QPushButton(self.widget_fil_ariane)
        self.pushButton_type.setObjectName(u"pushButton_type")

        self.horizontalLayout.addWidget(self.pushButton_type)

        self.pushButton_proj = QPushButton(self.widget_fil_ariane)
        self.pushButton_proj.setObjectName(u"pushButton_proj")

        self.horizontalLayout.addWidget(self.pushButton_proj)

        self.pushButton_fold = QPushButton(self.widget_fil_ariane)
        self.pushButton_fold.setObjectName(u"pushButton_fold")

        self.horizontalLayout.addWidget(self.pushButton_fold)

        self.pushButton_soft = QPushButton(self.widget_fil_ariane)
        self.pushButton_soft.setObjectName(u"pushButton_soft")

        self.horizontalLayout.addWidget(self.pushButton_soft)

        self.label_type = QLabel(self.widget_navigation)
        self.label_type.setObjectName(u"label_type")
        self.label_type.setGeometry(QRect(30, 30, 77, 19))
        self.label_proj = QLabel(self.widget_navigation)
        self.label_proj.setObjectName(u"label_proj")
        self.label_proj.setGeometry(QRect(140, 30, 77, 19))
        self.label_fold = QLabel(self.widget_navigation)
        self.label_fold.setObjectName(u"label_fold")
        self.label_fold.setGeometry(QRect(280, 40, 77, 19))
        self.label_soft = QLabel(self.widget_navigation)
        self.label_soft.setObjectName(u"label_soft")
        self.label_soft.setGeometry(QRect(430, 30, 77, 19))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_type.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_proj.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_fold.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_soft.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label_type.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_proj.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_fold.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_soft.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

