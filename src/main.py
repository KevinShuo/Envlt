# -*- coding: utf-8 -*-
import sys
import traceback

sys.path.append(r"L:\TD\01_TD\py_package")
sys.path.append(r"C:\dev\maya\Envlt\src")
from importlib import reload
from ns_Envlt.ui import mainWindow
from ns_Envlt.envlt_log import log_factory
from PySide2.QtWidgets import QMessageBox

reload(mainWindow)
reload(log_factory)


def run():
    w = mainWindow.mainWindow()


if __name__ == '__main__':
    log = log_factory.LogFactory("Envlt", True)
    try:
        run()
    except:
        error_content = traceback.format_exc()
        log.write_log(log.error, error_content)
        QMessageBox.critical(None, "发生致命错误", error_content)
