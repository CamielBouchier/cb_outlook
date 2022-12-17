#
# $BeginLicense$
#
# (C) 2022 by Camiel Bouchier (camiel@bouchier.be)
#
# This file is part of cb_outlook.
# All rights reserved.
# You are granted a non-exclusive and non-transferable license to use this
# software for personal or internal business purposes.
#
# THIS SOFTWARE IS PROVIDED "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Camiel Bouchier BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# $EndLicense$
#

a = Analysis(['cb_outlook.py'],
             #https://hackmd.io/@quency/B1QmM5-OD
             hiddenimports=['win32timezone'],
             hookspath=None,
             runtime_hooks=None)

a.datas +=  [('cb_outlook.ico'      , 'cb_outlook.ico'      , 'DATA')]
a.datas +=  [('cb_outlook_64px.png' , 'cb_outlook_64px.png' , 'DATA')]
a.datas +=  [('qt.conf'             , 'qt.conf'             , 'DATA')]
a.datas +=  [('help.txt'            , 'help.txt'            , 'DATA')]
a.datas +=  [('license.txt'         , 'license.txt'         , 'DATA')]

a.datas +=  [('plugins\\imageformats\\qico.dll' , 'plugins\\imageformats\\qico.dll', 'DATA')]


pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='cb_outlook.exe',
          debug=False,
          strip=None,
          upx=True,
          icon='cb_outlook.ico',
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='cb_outlook')

# vim: syntax=python ts=4 sw=4 sts=4 sr et columns=100
