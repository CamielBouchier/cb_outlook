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

# Want to be asap sure we are running Python 3.6
import sys
assert sys.version_info >= (3,6)

import logging
logger = logging.getLogger(__name__)

import datetime
import glob
import io
import json
import os
import pytz
import pywintypes
import re
import time
import traceback
import win32api
import win32com.client

from PySide2.QtCore     import QCoreApplication
from PySide2.QtCore     import QPoint
from PySide2.QtCore     import QSettings
from PySide2.QtCore     import QSize
from PySide2.QtCore     import QStandardPaths
from PySide2.QtCore     import Qt
from PySide2.QtCore     import QTimer
from PySide2.QtGui      import QIcon
from PySide2.QtWidgets  import QApplication

from cb_mainwindow import cb_mainwindow
from cb_dialog     import cb_dialog

#---------------------------------------------------------------------------------------------------

program_name    = "cb_outlook"
program_version = "1.0.0"
company_name    = "cb_soft"
domain_name     = "camiel.bouchier.be"

QCoreApplication.setApplicationName(program_name)
QCoreApplication.setOrganizationName(company_name)
QCoreApplication.setOrganizationDomain(domain_name)

home_location = QStandardPaths.writableLocation(QStandardPaths.HomeLocation)
data_location = f"{home_location}/{program_name}"

try:
    os.makedirs(data_location)
except FileExistsError:
    pass

log_filename = f"{data_location}/{program_name}.log"
usersettings_filename = f"{data_location}/{program_name}.ini"

#---------------------------------------------------------------------------------------------------

def get_datetime_format_string():

    '''
    This function tries to figure out what is the datetime representation to be used
    when interacting with win32/outlook.  A confusing date (3 april 2002 17:56) is converted
    using the win32api (with its localizations) and the output is parsed to find out what
    should be the datetime format to be used in strftime()
    '''

    dt_test = datetime.datetime(2002, 4, 3, 17, 56, tzinfo=pytz.UTC)

    d = win32api.GetDateFormat(0, 0, dt_test)
    if "03" in d:
        d = d.replace("03", "%d")
    if "3" in d:
        d = d.replace("3", "%d")    # -d does not work on all platforms.
    if "04" in d:
        d = d.replace("04", "%m")
    if "4" in d:
        d = d.replace("4", "%-m")
    if "2002" in d:
        d = d.replace("2002", "%Y")
    if "02" in d:
        d = d.replace("02", "%y")
    if "2" in d:
        d = d.replace("2", "%-y")

    t = win32api.GetTimeFormat(0, 0, dt_test)
    assert "56" in t
    t = t.replace("56", "%M")
    if "17" in t:
        t = t.replace("17", "%H")
    if "5" in t:
        t = t.replace("5", "%H")
        assert "PM" in t
        t = t.replace("PM", "%p")
    # Outlook does not want seconds. Don't convert them!
    assert ":00" in t
    t = t.replace(":00", "")

    rv = f"{d} {t}"

    return rv

#---------------------------------------------------------------------------------------------------

def myself():

    '''
    This to return the name of a function from within that function.
    It only survives the most straightforward cases, so don't stretch anywhere.
    '''

    return sys._getframe().f_back.f_code.co_name

#---------------------------------------------------------------------------------------------------

class cb_outlook(QApplication):

    def __init__(self, argv) :

        logger.debug(f"{myself()}: {argv} {type(argv)}")

        super().__init__(argv)

        # I strongly prefer ini files above register values for readibility and debug.
        self.usersettings  = QSettings(usersettings_filename, QSettings.IniFormat)
        logger.debug("usersettings in '{self.usersettings.fileName()}'")

        self.icon = QIcon(program_name + ".ico")
        self.cb_launch_mainwindow()

        self.mainwindow.show()

        # Our timer for hourly runs.

        self.hour_timer = QTimer()
        self.hour_timer.setInterval(1000*60*60)
        self.hour_timer.setSingleShot(False)
        self.hour_timer.timeout.connect(self.cb_on_hour_timer)
        self.cb_on_hour_timer()
        self.hour_timer.start()

    #-----------------------------------------------------------------------------------------------

    def cb_launch_mainwindow(self) :

        logger.debug(f"{myself()}")

        self.mainwindow = cb_mainwindow(program_name, self.icon)
        desktop_rect = QApplication.desktop().screenGeometry(self.mainwindow)
        default_pos  = QPoint(desktop_rect.width()/10, desktop_rect.height()/10)
        default_size = QSize(480,600)
        self.mainwindow.resize(self.usersettings.value("mainwindow_size", default_size))
        self.mainwindow.move(self.usersettings.value("mainwindow_pos", default_pos))

        str_now = datetime.datetime.now().replace(microsecond=0)
        self.cb_log(f"{str_now}: starting {program_name}")
        self.cb_log(f"usersettings: {self.usersettings.fileName()}")
        self.cb_log(f"logging: {log_filename}")

    #-----------------------------------------------------------------------------------------------

    def cb_on_start_of_day_changed(self, start_of_day):

        logger.debug(f"{myself()}: {start_of_day} {type(start_of_day)}")
        self.usersettings.setValue("start_of_day" , start_of_day)

        self.start_slot = start_of_day.hour() * 2
        if start_of_day.minute() > 0:
            self.start_slot += 1
        if start_of_day.minute() > 30:
            self.start_slot += 1

        logger.debug(f"{myself()}: self.start_slot = {self.start_slot}")

    #-----------------------------------------------------------------------------------------------

    def cb_on_end_of_day_changed(self, end_of_day):

        logger.debug(f"{myself()}: {end_of_day} {type(end_of_day)}")
        self.usersettings.setValue("end_of_day" , end_of_day)

        self.end_slot = end_of_day.hour() * 2
        if end_of_day.minute() > 0:
            self.end_slot += 1
        if end_of_day.minute() > 30:
            self.end_slot += 1

        logger.debug(f"{myself()}: self.end_slot = {self.end_slot}")

    #-----------------------------------------------------------------------------------------------

    def cb_on_free_slots_changed(self, free_slots):

        logger.debug(f"{myself()}: {free_slots} {type(free_slots)}")
        self.usersettings.setValue("free_slots" , free_slots)
        self.max_nr_occupied_slots = self.end_slot - self.start_slot - free_slots
        logger.debug(f"{myself()}: self.max_nr_occupied_slots = {self.max_nr_occupied_slots}")

    #-----------------------------------------------------------------------------------------------

    def cb_on_lookahead_days_changed(self, lookahead_days):

        logger.debug(f"{myself()}: {lookahead_days} {type(lookahead_days)}")
        self.usersettings.setValue("lookahead_days" , lookahead_days)
        self.lookahead_days = lookahead_days

    #-----------------------------------------------------------------------------------------------

    def cb_on_focus_string_changed(self, focus_string):

        logger.debug(f"{myself()} {focus_string} {type(focus_string)}")
        self.usersettings.setValue("focus_string" , focus_string)
        self.focus_string = focus_string

    #-----------------------------------------------------------------------------------------------

    def cb_on_each_hour_changed(self, each_hour):

        logger.debug(f"{myself()}: {each_hour} {type(each_hour)}")
        self.usersettings.setValue("each_hour" , each_hour)
        self.each_hour = each_hour

    #-----------------------------------------------------------------------------------------------

    def cb_on_start_date_changed(self, start_date):

        logger.debug(f"{myself()}: {start_date} {type(start_date)}")
        self.start_date = start_date

    #-----------------------------------------------------------------------------------------------

    def cb_on_end_date_changed(self, end_date):

        logger.debug(f"{myself()}: {end_date} {type(end_date)}")
        self.end_date = end_date

    #-----------------------------------------------------------------------------------------------

    def cb_on_message_changed(self, message):

        logger.debug(f"{myself()}: {message} {type(message)}")
        self.message = message

    #-----------------------------------------------------------------------------------------------

    def fix_day(self, year, month, day):

        '''
        this is the crux of the code, it fixes the agenda of a particular day to
        stuff it with reserved slots or to remove them (when meetings were cancelled e.g.)
        '''

        # 0: free, 1: really occupied, 2: blocked by this program
        day_occupation_half_hours = [0] * 48

        dt_begin = datetime.datetime(year, month, day)
        dt_end   = dt_begin + datetime.timedelta(days=1)

        f = get_datetime_format_string()

        str_begin = dt_begin.strftime(f)
        str_end   = dt_end.strftime(f)

        restriction = f"[Start] >= '{str_begin}' AND [End] < '{str_end}'"

        outlook = win32com.client.Dispatch('Outlook.Application').GetNamespace('MAPI')

        calendar = outlook.getDefaultFolder(9).Items
        calendar.IncludeRecurrences = True
        calendar.Sort('[Start]')

        calendar = calendar.Restrict(restriction)

        for app in calendar:

            dt_start = datetime.datetime(year, month, day, app.Start.hour, app.Start.minute)
            start_as_half_hour_slot = int( (dt_start - dt_begin).total_seconds()/(60*30) )
            duration_half_hours = int( (app.Duration+29)/30 )

            r = range(start_as_half_hour_slot, start_as_half_hour_slot + duration_half_hours)
            for slot in r:
                if app.Subject != self.focus_string:
                    day_occupation_half_hours[slot] = 1
                else:
                    day_occupation_half_hours[slot] = 2


        my_day_occupation_half_hours = day_occupation_half_hours[self.start_slot:self.end_slot]
        nr_occupied_slots = my_day_occupation_half_hours.count(1)

        if nr_occupied_slots > self.max_nr_occupied_slots:

            self.cb_log(f"{year}-{month}-{day} is overbooked. Start blocking")

            # Start blocking half an hour slots for this day.
            for slot in range(len(day_occupation_half_hours)):

                # Outside hours?
                if slot<self.start_slot or slot>=self.end_slot: continue
                # Already occupied?
                if day_occupation_half_hours[slot]: continue

                # Create half hour slot of focus
                hours = int(slot/2)
                minutes = (slot % 2) * 30
                dt_start = datetime.datetime(year, month, day, hours, minutes)
                self.cb_log(f"blocking {dt_start} to focus")
                olap = win32com.client.Dispatch('Outlook.Application')
                app = olap.CreateItem(1)
                app.Start = dt_start.strftime(f)
                app.Duration = 30
                app.Subject = self.focus_string
                app.Save()

        else:

            self.cb_log(f"{year}-{month}-{day} is not overbooked.")

            # Remove our blocking slots

            to_remove = []
            for app in calendar:
                if app.Subject == self.focus_string: to_remove.append(app)
            for app in to_remove:
                self.cb_log(f"unblocking {app.Start}")
                app.Delete()

        # To know the attributes one can work with
        # for x in dir(calendar[0]):
        #    print(f"{x} {getattr(calendar[0], x)}" )

    #-----------------------------------------------------------------------------------------------

    def cb_on_block_now(self):

        logger.debug(f"{myself()}")

        str_now = datetime.datetime.now().replace(microsecond=0)
        self.cb_log(f"{str_now}: checking and updating calendar")
        dt_start = datetime.datetime.now()
        for i in range(self.lookahead_days):
            dt_to_handle = dt_start + datetime.timedelta(days=i)
            year = dt_to_handle.year
            month = dt_to_handle.month
            day = dt_to_handle.day
            logger.debug(f"handling {year}-{month}-{day}")
            self.fix_day(year, month, day)

        str_now = datetime.datetime.now().replace(microsecond=0)
        self.cb_log(f"{str_now}: checked and updated calendar")

        # So as of now each hour (if that would be enabled)
        self.hour_timer.start()

    #-----------------------------------------------------------------------------------------------

    def cb_on_hour_timer(self):

        logger.debug(f"{myself()}")
        if self.each_hour:
            self.cb_on_block_now()

    #-----------------------------------------------------------------------------------------------

    def cb_on_empty_now(self):

        logger.debug(f"{myself()}")

        str_now = datetime.datetime.now().replace(microsecond=0)
        self.cb_log(f"{str_now}: emptying calendar")

        d = self.start_date
        dt_begin = datetime.datetime(d.year(), d.month(), d.day())

        d = self.end_date
        dt_end = datetime.datetime(d.year(), d.month(), d.day())

        f = get_datetime_format_string()

        str_begin = dt_begin.strftime(f)
        str_end   = dt_end.strftime(f)

        restriction = f"[Start] >= '{str_begin}' AND [End] < '{str_end}'"

        outlook = win32com.client.Dispatch('Outlook.Application').GetNamespace('MAPI')

        calendar = outlook.getDefaultFolder(9).Items
        calendar.IncludeRecurrences = True
        calendar.Sort('[Start]')

        calendar = calendar.Restrict(restriction)

        apps_to_handle = [app for app in calendar]
        for app in apps_to_handle:

            # 4: declined
            new_app = app.Respond(4, True, True)
            if not new_app:
                self.cb_log(f"canceling {app.Start}: {app.Subject}")
                # 5: cancelled
                app.MeetingStatus = 5
                app.Body = self.message
                app.Save()
                app.Send()
            else:
                self.cb_log(f"declining {app.Start}: {app.Subject}")
                new_app.Body = self.message
                new_app.Send()

        str_now = datetime.datetime.now().replace(microsecond=0)
        self.cb_log(f"{str_now}: emptied calendar")

    #-----------------------------------------------------------------------------------------------

    def cb_log(self, text):

        '''
        this is logging as it goes to the user (in the therefore foreseen read-only textedit
        '''

        logger.debug(f"{myself()}: {text}")
        self.mainwindow.ui.textedit_log.appendPlainText(text)
        # Ensure immediate GUI update
        self.processEvents()

    #-----------------------------------------------------------------------------------------------

    def cb_on_help(self):

        logger.debug(f"{myself()}")
        with open("help.txt", "r", encoding="utf-8") as f:
            help = f.read().format(**{
                "program_name": program_name,
                "program_version": program_version})
        dialog = cb_dialog(self.mainwindow, "Help", help, self.icon)
        dialog.exec_()

    #-----------------------------------------------------------------------------------------------

    def cb_on_license(self):

        logger.debug(f"{myself()}")
        with open("license.txt", "r", encoding="utf-8") as f:
            license = f.read()
        dialog = cb_dialog(self.mainwindow, "License", license, self.icon)
        dialog.exec_()


    #-----------------------------------------------------------------------------------------------

    def cb_on_quit(self):

        logger.debug(f"{myself()}")

        self.usersettings.setValue("mainwindow_pos" , self.mainwindow.pos())
        self.usersettings.setValue("mainwindow_size" , self.mainwindow.size())
        self.usersettings.sync()
        QApplication.quit()

#---------------------------------------------------------------------------------------------------

def cb_excepthook(exception_type, exception_value, traceback_object) :

    """
    Catch unhandled exceptions.
    """

    # Construct stack trace.
    traceback_info_file = io.StringIO()
    traceback.print_tb(traceback_object, None, traceback_info_file)
    traceback_info_file.seek(0)
    traceback_info = traceback_info_file.read()

    # Construct error message.
    error_message = f"{exception_type} :\n\n{exception_value}\n"
    stack_trace   = f"Stack trace :\n{traceback_info}"

    logger.critical(error_message)
    logger.debug(stack_trace)    # Auto stack trace of exception only works in exception block.

    sys.exit()

#---------------------------------------------------------------------------------------------------

def cb_install_logger() :

    """
    Install logger
    """

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_filename, mode='a', encoding="utf8")
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)10s - %(filename)32s:%(lineno)5s : %(message)s")
    file_handler.setFormatter(file_formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter("%(filename)32s:%(lineno)5s : %(message)s")
    console_handler.setFormatter(console_formatter)

    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    logger.debug(f"logging in '{log_filename}'")

#---------------------------------------------------------------------------------------------------

if __name__ == '__main__' :

    cb_install_logger()
    logger.debug(f"starting {program_name}")

    # Catch exceptions to give feedback to user.
    sys.excepthook = cb_excepthook

    the_app = cb_outlook(sys.argv)
    rv = the_app.exec_()

    logger.debug(f"done {program_name}: {rv}")

#---------------------------------------------------------------------------------------------------

# vim: syntax=python ts=4 sw=4 sts=4 sr et columns=100 lines=45
