#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

$BeginLicense$

(C) 2022 by Camiel Bouchier (camiel@bouchier.be)

This file is part of cb_outlook.
All rights reserved.
You are granted a non-exclusive and non-transferable license to use this
software for personal or internal business purposes.

THIS SOFTWARE IS PROVIDED "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL Camiel Bouchier BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

$EndLicense$

"""

#---------------------------------------------------------------------------------------------------

import datetime
import os

from PySide2.QtCore     import QDate
from PySide2.QtCore     import Qt
from PySide2.QtCore     import QTime
from PySide2.QtWidgets  import QApplication
from PySide2.QtWidgets  import QMainWindow

from ui_cb_mainwindow   import Ui_cb_mainwindow

#---------------------------------------------------------------------------------------------------

class cb_mainwindow(QMainWindow):

    def __init__(self,title,icon) :

        super().__init__(None)

        self.app = QApplication.instance()

        # Setup from gui builder.
        self.ui = Ui_cb_mainwindow()
        self.ui.setupUi(self)
        self.setWindowTitle(title)
        self.setWindowIcon(icon)

        # Menu connects.
        self.ui.action_quit.triggered.connect(self.app.cb_on_quit)
        self.ui.action_license.triggered.connect(self.app.cb_on_license)
        self.ui.action_help.triggered.connect(self.app.cb_on_help)

        # initializing gui elements from the usersettings case those are available
        # (and sensible default if not)

        start_of_day = self.app.usersettings.value("start_of_day", QTime(8, 30))
        end_of_day = self.app.usersettings.value("end_of_day", QTime(17, 30))
        free_slots = int(self.app.usersettings.value("free_slots", 6))
        lookahead_days = int(self.app.usersettings.value("lookahead_days", 7))
        focus_string = self.app.usersettings.value("focus_string", "cb_outlook: focus")
        each_hour = int(self.app.usersettings.value("each_hour", Qt.Unchecked))

        self.ui.time_edit_start_of_day.setTime(start_of_day)
        self.ui.time_edit_end_of_day.setTime(end_of_day)
        self.ui.spinbox_free_slots.setValue(free_slots)
        self.ui.spinbox_lookahead_days.setValue(lookahead_days)
        self.ui.line_edit_focus_string.setText(focus_string)
        self.ui.checkbox_each_hour.setCheckState(Qt.CheckState(each_hour))

        now_date = QDate(datetime.datetime.now())
        reason = "This is the reason"

        self.ui.date_edit_start_date.setDate(now_date)
        self.ui.date_edit_end_date.setDate(now_date)
        self.ui.text_edit_message.setText(reason)

        # Call the associated cb_on function (just to make sure all got initialized,
        # even if *no* change)
        self.app.cb_on_start_of_day_changed(start_of_day)
        self.app.cb_on_end_of_day_changed(end_of_day)
        self.app.cb_on_free_slots_changed(free_slots)
        self.app.cb_on_lookahead_days_changed(lookahead_days)
        self.app.cb_on_focus_string_changed(focus_string)
        self.app.cb_on_each_hour_changed(each_hour)

        self.app.cb_on_start_date_changed(now_date)
        self.app.cb_on_end_date_changed(now_date)
        self.app.cb_on_message_changed(reason)

        # signal connections for future changes

        self.ui.time_edit_start_of_day.timeChanged.connect(self.app.cb_on_start_of_day_changed)
        self.ui.time_edit_end_of_day.timeChanged.connect(self.app.cb_on_end_of_day_changed)
        self.ui.spinbox_free_slots.valueChanged.connect(self.app.cb_on_free_slots_changed)
        self.ui.spinbox_lookahead_days.valueChanged.connect(self.app.cb_on_lookahead_days_changed)
        self.ui.line_edit_focus_string.textChanged.connect(self.app.cb_on_focus_string_changed)
        self.ui.checkbox_each_hour.stateChanged.connect(self.app.cb_on_each_hour_changed)
        self.ui.pushbutton_block_now.clicked.connect(self.app.cb_on_block_now)

        self.ui.date_edit_start_date.dateChanged.connect(self.app.cb_on_start_date_changed)
        self.ui.date_edit_end_date.dateChanged.connect(self.app.cb_on_end_date_changed)
        self.ui.text_edit_message.textChanged.connect(self.app.cb_on_message_changed)
        self.ui.pushbutton_empty_now.clicked.connect(self.app.cb_on_empty_now)

    #-----------------------------------------------------------------------------------------------

    def closeEvent(self,event):

        self.app.cb_on_quit()

#---------------------------------------------------------------------------------------------------

# vim: syntax=python ts=4 sw=4 sts=4 sr et columns=100 lines=45
