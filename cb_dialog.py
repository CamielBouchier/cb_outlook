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

from PySide2.QtWidgets import QDialog

from ui_cb_dialog import Ui_cb_dialog

#---------------------------------------------------------------------------------------------------

class cb_dialog(QDialog):

    def __init__(self,parent, title, message, icon) :

        super(cb_dialog, self).__init__(parent)

        # Setup from GUI builder.
        self.ui = Ui_cb_dialog()
        self.ui.setupUi(self)

        self.setWindowTitle(title)
        self.setWindowIcon(icon)
        self.ui.textbrowser_text.setText(message)
        self.ui.textbrowser_text.setOpenExternalLinks(True)

#---------------------------------------------------------------------------------------------------

# vim: syntax=python ts=4 sw=4 sts=4 sr et columns=100 lines=45
