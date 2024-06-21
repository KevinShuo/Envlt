# -*- coding: utf-8 -*-
# @Time : 2024/6/21 14:08
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : mainWindow.py
# @Project : Envlt
from enum import Enum
from ns_Envlt.ui import Envlt
from maya.OpenMayaUI import MQtUtil_mainWindow
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from shiboken2 import wrapInstance


class PageType(Enum):
    About = 0,
    Project = 1,


class mainWindow(QWidget):
    def __init__(self):
        """
            Envlt mainWindow
        """
        super().__init__()
        self.envlt = Envlt.Ui_mainWindows()
        self.envlt.setupUi(self)
        self.setParent(wrapInstance(int(MQtUtil_mainWindow()), QWidget))
        self.setWindowFlags(Qt.Window)
        self.init_window()
        self.init_slot()
        self.show()

    def init_window(self):
        self.envlt.stackedWidget.setCurrentIndex(0)

    def init_slot(self):
        self.envlt.about_button.clicked.connect(lambda: self.switch_page(PageType.About))
        self.envlt.project.clicked.connect(lambda: self.switch_page(PageType.Project))

    def switch_page(self, page: PageType):
        if page == PageType.About:
            self.envlt.stackedWidget.setCurrentIndex(0)
        elif page == PageType.Project:
            self.envlt.stackedWidget.setCurrentIndex(1)
