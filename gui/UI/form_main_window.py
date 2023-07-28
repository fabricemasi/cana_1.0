# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_main_windowIkbCvb.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QListView, QSizePolicy,
    QWidget)

class Ui_MainWindowForm(object):
    def setupUi(self, MainWindowForm):
        if not MainWindowForm.objectName():
            MainWindowForm.setObjectName(u"MainWindowForm")
        MainWindowForm.resize(549, 524)
        self.ui_listWidget1 = QListView(MainWindowForm)
        # self.ui_listWidget1.setObjectName(u"ui_listWidget1")
        self.ui_listWidget1.setGeometry(QRect(10, 10, 256, 501))
        self.ui_listWidget2 = QListView(MainWindowForm)
        # self.ui_listWidget2.setObjectName(u"ui_listWidget2")
        self.ui_listWidget2.setGeometry(QRect(280, 10, 256, 501))

        self.retranslateUi(MainWindowForm)

        QMetaObject.connectSlotsByName(MainWindowForm)
    # setupUi

    def retranslateUi(self, MainWindowForm):
        MainWindowForm.setWindowTitle(QCoreApplication.translate("MainWindowForm", u"Dialog", None))
    # retranslateUi

