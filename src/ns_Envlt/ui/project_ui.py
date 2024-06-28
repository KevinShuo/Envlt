from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ProjectUI(QWidget):
    def __init__(self):
        super(ProjectUI, self).__init__()
        self.max_width = 200
        self.max_height = 150
        self.current_columns = -1  # 用于跟踪当前列数

        self.init_widgets()
        self.init_layout()
        self.add_frames()
        self.resizeEvent = self.on_resize  # 绑定窗口调整事件

    def init_widgets(self):
        pass

    def init_layout(self):
        # 创建一个滚动区域
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setStyleSheet("background-color: rgb(41, 46, 59);")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QGridLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)

        # 主布局
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.scroll_area)
        self.setLayout(main_layout)

    def create_frame(self, image_path, text):
        # 创建一个HoverableFrame
        card_frame = HoverableFrame()
        card_frame.setFrameShape(QFrame.Box)
        card_frame.setFrameShadow(QFrame.Raised)
        card_frame.setFixedSize(self.max_width, self.max_height)  # 设置固定大小
        card_frame.clicked.connect(self.on_frame_clicked)  # 连接点击信号到槽函数

        # 设置布局
        layout = QVBoxLayout(card_frame)

        # 设置图片
        image = QLabel()
        pixmap = QPixmap(image_path)
        scale_pixmap = pixmap.scaled(self.max_width, self.max_height, Qt.KeepAspectRatio)
        image.setPixmap(scale_pixmap)
        layout.addWidget(image)

        # 设置标签
        label = QLabel(text)
        label.setObjectName("frameLabel")  # 设置对象名称
        label.setStyleSheet("font-size: 14px; font-weight: bold; color: #333; padding-top: 10px;")  # 设置文字样式
        layout.addWidget(label)

        layout.setContentsMargins(10, 10, 10, 10)  # 设置内边距

        return card_frame

    def on_frame_clicked(self):
        sender = self.sender()
        label = sender.findChild(QLabel, "frameLabel")  # 根据对象名称查找QLabel
        if label:
            print(label.text())

    def add_frames(self):
        self.frames = []
        for i in range(10):
            frame = self.create_frame(r"C:/Users/zhuyihan/Desktop/1111.png", f"资产名称: 13Hang_BaiET_{i}")
            self.frames.append(frame)
        self.update_layout(force_update=True)  # 初始布局时强制更新

    def update_layout(self, force_update=False):
        # 计算每行可以放置的QFrame数量
        num_columns = max(1, self.width() // (self.max_width + 20))
        if num_columns == self.current_columns and not force_update:
            return  # 如果列数没有变化且不是强制更新，就不进行调整

        # 更新当前列数
        self.current_columns = num_columns

        # 临时禁用更新
        self.setUpdatesEnabled(False)

        # 清除布局中的所有小部件
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget is not None:
                self.scroll_layout.removeWidget(widget)
                widget.setParent(None)

        # 根据窗口宽度计算每行可以放置的QFrame数量
        for index, frame in enumerate(self.frames):
            row = index // num_columns
            col = index % num_columns
            self.scroll_layout.addWidget(frame, row, col)

        # 重新启用更新
        self.setUpdatesEnabled(True)

    def on_resize(self, event):
        self.update_layout()
        super(ProjectUI, self).resizeEvent(event)


class HoverableFrame(QFrame):
    clicked = Signal()  # 定义一个信号

    def __init__(self, parent=None):
        super(HoverableFrame, self).__init__(parent)
        self.setStyleSheet("QFrame { border: 1px solid #ccc; border-radius: 5px; background-color: white; }")

    def mousePressEvent(self, event):
        self.clicked.emit()  # 触发点击信号
        super(HoverableFrame, self).mousePressEvent(event)

    def enterEvent(self, event):
        self.setStyleSheet("QFrame { border: 1px solid #999; border-radius: 5px; background-color: #f0f0f0; }")
        super(HoverableFrame, self).enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet("QFrame { border: 1px solid #ccc; border-radius: 5px; background-color: white; }")
        super(HoverableFrame, self).leaveEvent(event)
