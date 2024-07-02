# -*- coding: utf-8 -*-
# @Time : 2024/7/2 15:43
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : image_window.py
# @Project : Envlt
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


class ImageWindow(QDialog):
    def __init__(self, image_data):
        super().__init__()
        self.setWindowTitle('Image Viewer')

        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(image_data))

        label = QLabel(self)
        label.setPixmap(pixmap)

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
