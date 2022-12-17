;---------------------------------------------------------------------------------------------------
;
; $BeginLicense$
;
; (C) 2022 by Camiel Bouchier (camiel@bouchier.be)
;
; This file is part of cb_outlook.
; All rights reserved.
; You are granted a non-exclusive and non-transferable license to use this
; software for personal or internal business purposes.
;
; THIS SOFTWARE IS PROVIDED "AS IS" AND
; ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
; WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
; DISCLAIMED. IN NO EVENT SHALL Camiel Bouchier BE LIABLE FOR ANY
; DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
; (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
; ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
; (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
; SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
;
; $EndLicense$
;
;---------------------------------------------------------------------------------------------------

!define program_name  "cb_outlook"
!define reg_key       "Software\${program_name}"
!define start_menu    "$SMPROGRAMS\${program_name}"
!define uninstall     "uninstall.exe"
!define uninstall_key "Software\Microsoft\Windows\CurrentVersion\Uninstall\${program_name}"

XPStyle on

Name       "${program_name}"
Caption    "${program_name}"
OutFile    "../${program_name}_installer.exe"
InstallDir "$PROGRAMFILES64\${program_name}"

;---------------------------------------------------------------------------------------------------

Page license
Page directory
Page instfiles

;---------------------------------------------------------------------------------------------------

; First is default
LoadLanguageFile "${NSISDIR}\Contrib\Language files\English.nlf"

LicenseLangString license_data ${LANG_ENGLISH} "..\license.txt"
LangString license_text ${LANG_ENGLISH} "License"
LangString dir_text ${LANG_ENGLISH} "The installer will install ${program_name}"
LangString uninstall_text ${LANG_ENGLISH} "The installer will uninstall ${program_name}"

LicenseData   "$(license_data)"
LicenseText   "$(license_text)"
DirText       "$(dir_text)"
UninstallText "$(uninstall_text)"

;---------------------------------------------------------------------------------------------------

UninstPage uninstConfirm
UninstPage instfiles

;---------------------------------------------------------------------------------------------------

Section
  WriteRegStr HKLM "${reg_key}"       "Install_Dir" "   $INSTDIR"
  WriteRegStr HKLM "${uninstall_key}" "DisplayName"     "${program_name} (remove only)"
  WriteRegStr HKLM "${uninstall_key}" "UninstallString" '"$INSTDIR\${uninstall}"'

  SetOutPath $INSTDIR
  File /r "..\dist_windows\cb_outlook\*.*"
  File /r /x ".*" "..\dist_windows\cb_outlook\plugins"
  File /r /x ".*" "..\dist_windows\cb_outlook\PySide2"
  File /r /x ".*" "..\dist_windows\cb_outlook\pytz"
  File /r /x ".*" "..\dist_windows\cb_outlook\pywin32_system32"
  File /r /x ".*" "..\dist_windows\cb_outlook\shiboken2"
  File /r /x ".*" "..\dist_windows\cb_outlook\win32com"

  WriteUninstaller "${uninstall}"

SectionEnd

;---------------------------------------------------------------------------------------------------

Section

  SetOutPath $INSTDIR
  CreateDirectory "${start_menu}"
  CreateShortCut  "${start_menu}\${program_name}.lnk" "$INSTDIR\${program_name}.exe"

SectionEnd

;---------------------------------------------------------------------------------------------------

Section "Uninstall"

  DeleteRegKey HKLM "${uninstall_key}"
  DeleteRegKey HKLM "${reg_key}"

  Delete "${start_menu}\*.*"
  Delete "${start_menu}"
  RMDir /r $INSTDIR

SectionEnd

;---------------------------------------------------------------------------------------------------
;
; vim: syntax=nsis ts=2 sw=2 sts=2 sr et columns=100 lines=45
