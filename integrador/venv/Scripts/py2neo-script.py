#!C:\Users\karli\PycharmProjects\IASEexamen\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'py2neo==4.3.0','console_scripts','py2neo'
__requires__ = 'py2neo==4.3.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('py2neo==4.3.0', 'console_scripts', 'py2neo')()
    )
