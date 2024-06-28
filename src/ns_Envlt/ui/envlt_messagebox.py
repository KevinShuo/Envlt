# -*- coding: utf-8 -*-
# @Time : 2024/6/25 16:20
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : envlt_messagebox.py
# @Project : Envlt
import os
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from importlib import reload
from . import envlt_dialog

reload(envlt_dialog)


class EnvltDialog(QDialog):
    def __init__(self):
        """
         envlt message dialog 类
        """
        super().__init__()
        self.env_dialog = envlt_dialog.Ui_Dialog()
        self.env_dialog.setupUi(self)
        self._init_slot()

    def information(self, title: str, content: str):
        """
            信息类

        :param title: 标题
        :param content:内容
        :return:
        """
        self.env_dialog.label.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), "resources/information .png")))
        self.env_dialog.label_title.setText(title)
        self.env_dialog.label_content.setText(content)
        self.exec_()

    def warning(self, title: str, content: str):
        """
            警告类

        :param title: 标题
        :param content: 内容
        :return:
        """
        self.env_dialog.label.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), "resources/warning.png")))
        self.env_dialog.label_title.setText(title)
        self.env_dialog.label_content.setText(content)
        self.exec_()

    def error(self, title: str, content: str):
        """
            错误类

        :param title: 标题
        :param content: 内容
        :return:
        """
        self.env_dialog.label.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), "resources/gaojing.png")))
        self.env_dialog.label_title.setText(f"Error: {title}" )
        self.env_dialog.label_content.setText(content)
        self.exec_()

    def _init_slot(self):
        """
            初始化信号

        :return:
        """
        self.env_dialog.pushButton_yes.clicked.connect(self.hide)
        self.env_dialog.pushButton_no.clicked.connect(self.hide)


from ns_Envlt.ui.resources import envlt_rc
