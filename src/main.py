# -*- coding: utf-8 -*-
import sys

sys.path.append(r"C:\dev\maya\Envlt\src")
from importlib import reload
from ns_Envlt.ui import mainWindow

reload(mainWindow)


def run():
    w = mainWindow.mainWindow()


if __name__ == '__main__':
    run()
