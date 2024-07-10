# -*- coding: utf-8 -*-
# @Time : 2024/7/10 下午4:45
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : test_rounded.py
# @Project : Envlt
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
from PyQt5.QtCore import Qt, QRectF


def create_rounded_pixmap(pixmap: QPixmap, radius: int) -> QPixmap:
    """
    Creates a rounded QPixmap from a QPixmap

    :param pixmap: original QPixmap
    :param radius: radius of rounded QPixmap
    :return: QPixmap with rounded corners
    """
    rounded_pixmap = QPixmap(pixmap)
    rounded_pixmap.fill(Qt.transparent)  # Ensure transparency

    painter = QPainter(rounded_pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setRenderHint(QPainter.SmoothPixmapTransform)

    path = QPainterPath()
    path.addRoundedRect(QRectF(pixmap.rect()), radius, radius)

    painter.setClipPath(path)
    painter.drawPixmap(0, 0, pixmap)
    painter.end()

    return rounded_pixmap


app = QApplication([])

label = QLabel()

original_pixmap = QPixmap(r"C:\dev\maya\Envlt\resources\scene_lib.png")  # Replace with your image path
rounded_pixmap = create_rounded_pixmap(original_pixmap, 130)  # Adjust the radius as needed

label.setPixmap(rounded_pixmap)
label.show()

app.exec_()
