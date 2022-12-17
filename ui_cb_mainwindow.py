# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cb_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_cb_mainwindow(object):
    def setupUi(self, cb_mainwindow):
        if not cb_mainwindow.objectName():
            cb_mainwindow.setObjectName(u"cb_mainwindow")
        cb_mainwindow.resize(965, 927)
        self.action_help = QAction(cb_mainwindow)
        self.action_help.setObjectName(u"action_help")
        self.action_license = QAction(cb_mainwindow)
        self.action_license.setObjectName(u"action_license")
        self.action_quit = QAction(cb_mainwindow)
        self.action_quit.setObjectName(u"action_quit")
        self.centralwidget = QWidget(cb_mainwindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.time_edit_start_of_day = QTimeEdit(self.tab)
        self.time_edit_start_of_day.setObjectName(u"time_edit_start_of_day")

        self.gridLayout.addWidget(self.time_edit_start_of_day, 0, 0, 1, 1)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.time_edit_end_of_day = QTimeEdit(self.tab)
        self.time_edit_end_of_day.setObjectName(u"time_edit_end_of_day")

        self.gridLayout.addWidget(self.time_edit_end_of_day, 1, 0, 1, 1)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.spinbox_free_slots = QSpinBox(self.tab)
        self.spinbox_free_slots.setObjectName(u"spinbox_free_slots")

        self.gridLayout.addWidget(self.spinbox_free_slots, 2, 0, 1, 1)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.spinbox_lookahead_days = QSpinBox(self.tab)
        self.spinbox_lookahead_days.setObjectName(u"spinbox_lookahead_days")

        self.gridLayout.addWidget(self.spinbox_lookahead_days, 3, 0, 1, 1)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)

        self.line_edit_focus_string = QLineEdit(self.tab)
        self.line_edit_focus_string.setObjectName(u"line_edit_focus_string")

        self.gridLayout.addWidget(self.line_edit_focus_string, 4, 0, 1, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)

        self.checkbox_each_hour = QCheckBox(self.tab)
        self.checkbox_each_hour.setObjectName(u"checkbox_each_hour")
        self.checkbox_each_hour.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.checkbox_each_hour, 5, 0, 1, 1)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)

        self.pushbutton_block_now = QPushButton(self.tab)
        self.pushbutton_block_now.setObjectName(u"pushbutton_block_now")

        self.gridLayout.addWidget(self.pushbutton_block_now, 6, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 124, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.date_edit_start_date = QDateEdit(self.tab_2)
        self.date_edit_start_date.setObjectName(u"date_edit_start_date")

        self.gridLayout_2.addWidget(self.date_edit_start_date, 0, 0, 1, 1)

        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)

        self.date_edit_end_date = QDateEdit(self.tab_2)
        self.date_edit_end_date.setObjectName(u"date_edit_end_date")

        self.gridLayout_2.addWidget(self.date_edit_end_date, 1, 0, 1, 1)

        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 1, 1, 1)

        self.text_edit_message = QTextEdit(self.tab_2)
        self.text_edit_message.setObjectName(u"text_edit_message")

        self.gridLayout_2.addWidget(self.text_edit_message, 2, 0, 1, 1)

        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 1, 1, 1)

        self.pushbutton_empty_now = QPushButton(self.tab_2)
        self.pushbutton_empty_now.setObjectName(u"pushbutton_empty_now")

        self.gridLayout_2.addWidget(self.pushbutton_empty_now, 3, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 41, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.textedit_log = QPlainTextEdit(self.centralwidget)
        self.textedit_log.setObjectName(u"textedit_log")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(4)
        sizePolicy1.setHeightForWidth(self.textedit_log.sizePolicy().hasHeightForWidth())
        self.textedit_log.setSizePolicy(sizePolicy1)
        self.textedit_log.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textedit_log)

        cb_mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(cb_mainwindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 965, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        cb_mainwindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(cb_mainwindow)
        self.statusbar.setObjectName(u"statusbar")
        cb_mainwindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.action_quit)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.action_help)
        self.menuHelp.addAction(self.action_license)

        self.retranslateUi(cb_mainwindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(cb_mainwindow)
    # setupUi

    def retranslateUi(self, cb_mainwindow):
        cb_mainwindow.setWindowTitle(QCoreApplication.translate("cb_mainwindow", u"MainWindow", None))
        self.action_help.setText(QCoreApplication.translate("cb_mainwindow", u"Help", None))
        self.action_license.setText(QCoreApplication.translate("cb_mainwindow", u"License", None))
        self.action_quit.setText(QCoreApplication.translate("cb_mainwindow", u"Quit", None))
        self.label.setText(QCoreApplication.translate("cb_mainwindow", u"Start of day", None))
        self.label_2.setText(QCoreApplication.translate("cb_mainwindow", u"End of day", None))
        self.label_3.setText(QCoreApplication.translate("cb_mainwindow", u"Requested free slots of 30'", None))
        self.label_4.setText(QCoreApplication.translate("cb_mainwindow", u"Nr of days lookahead", None))
        self.line_edit_focus_string.setPlaceholderText(QCoreApplication.translate("cb_mainwindow", u"cb: focus time", None))
        self.label_5.setText(QCoreApplication.translate("cb_mainwindow", u"Focus string", None))
        self.checkbox_each_hour.setText("")
        self.label_6.setText(QCoreApplication.translate("cb_mainwindow", u"Run each hour", None))
        self.pushbutton_block_now.setText(QCoreApplication.translate("cb_mainwindow", u"Run now", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("cb_mainwindow", u"Block calendar", None))
        self.label_7.setText(QCoreApplication.translate("cb_mainwindow", u"Start date", None))
        self.label_8.setText(QCoreApplication.translate("cb_mainwindow", u"End date", None))
        self.label_9.setText(QCoreApplication.translate("cb_mainwindow", u"Message", None))
        self.pushbutton_empty_now.setText(QCoreApplication.translate("cb_mainwindow", u"Empty now", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("cb_mainwindow", u"Empty calendar", None))
        self.menuFile.setTitle(QCoreApplication.translate("cb_mainwindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("cb_mainwindow", u"Help", None))
    # retranslateUi

