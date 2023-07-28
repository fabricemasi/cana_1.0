# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testFkahkk.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1418, 800)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(160, 210, 343, 491))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listView = QListView(self.frame)
        self.listView.setObjectName(u"listView")

        self.gridLayout.addWidget(self.listView, 0, 0, 1, 1)

        self.frame_btn = QFrame(self.frame)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setMaximumSize(QSize(61, 385))
        self.frame_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_btn)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.frame_btn)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 357, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.frame_btn, 0, 1, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 80))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 20, 89, 25))

        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

