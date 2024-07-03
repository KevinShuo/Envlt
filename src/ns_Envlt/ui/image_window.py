# -*- coding: utf-8 -*-
# @Time : 2024/7/2 15:43
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : image_window.py
# @Project : Envlt
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class ImageWindow(QWidget):
    def __init__(self, image_data):
        super().__init__()
        self.setWindowTitle('Image Viewer')
        self.setGeometry(100, 100, 800, 600)  # 设置窗口初始大小

        # 保存原始图片数据
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(QByteArray(image_data))


        # 创建布局
        main_layout = QVBoxLayout(self)

        # 创建滚动区域
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        # 创建标签并设置图像
        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.label.setAlignment(Qt.AlignCenter)
        self.scroll_area.setWidget(self.label)

        # 添加滚动区域到布局
        main_layout.addWidget(self.scroll_area)

        # 创建缩放控件布局
        scale_layout = QHBoxLayout()

        # 创建还原比例按钮
        self.reset_button = QPushButton("Reset", self)
        self.reset_button.clicked.connect(self.reset_scale)
        scale_layout.addWidget(self.reset_button)

        # 创建滑块
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(10)
        self.slider.setMaximum(200)
        self.slider.setValue(100)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.valueChanged.connect(self.scale_image)
        scale_layout.addWidget(self.slider)

        # 创建比例显示标签
        self.scale_label = QLabel("100%", self)
        scale_layout.addWidget(self.scale_label)

        # 添加缩放控件布局到主布局
        main_layout.addLayout(scale_layout)

        self.setLayout(main_layout)

    def scale_image(self, value):
        scale_factor = value / 100.0
        scaled_pixmap = self.pixmap.scaled(self.pixmap.size() * scale_factor, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(scaled_pixmap)
        self.scale_label.setText(f"{value}%")

    def reset_scale(self):
        self.slider.setValue(100)
