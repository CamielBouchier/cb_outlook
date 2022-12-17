# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cb_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_cb_dialog(object):
    def setupUi(self, cb_dialog):
        if not cb_dialog.objectName():
            cb_dialog.setObjectName(u"cb_dialog")
        cb_dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(cb_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.textbrowser_text = QTextBrowser(cb_dialog)
        self.textbrowser_text.setObjectName(u"textbrowser_text")

        self.verticalLayout.addWidget(self.textbrowser_text)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonBox = QDialogButtonBox(cb_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)

        self.horizontalSpacer = QSpacerItem(9, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(cb_dialog)
        self.buttonBox.accepted.connect(cb_dialog.accept)
        self.buttonBox.rejected.connect(cb_dialog.reject)

        QMetaObject.connectSlotsByName(cb_dialog)
    # setupUi

    def retranslateUi(self, cb_dialog):
        cb_dialog.setWindowTitle(QCoreApplication.translate("cb_dialog", u"Dialog", None))
    # retranslateUi

