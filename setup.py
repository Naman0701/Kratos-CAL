import cx_Freeze
import sys
import os
base =None


if sys.platform=='win32':
    base='Win32GUI'
os.environ['TCL_LIBRARY']=r'tcl8.6'
os.environ['TK_LIBRARY']=r'tk8.6'

executables=[cx_Freeze.Executable('Kratos Calculator.py',base=base,icon='krato.ico')]

cx_Freeze.setup(
    name='Kratos Calculator',
    options={'build_exe':{'packages':['tkinter','os'],'include_files':['krato.ico','tcl86t.dll','tk86t.dll','icon']}},
    version='0.26',
    description='Yara simple calci h. Malum bahut basic h, upar se bahut help leke banaya, future mein aur banata.',
    executables=executables

)
