from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
from PySide2.QtGui import QPainter, QColor
from PySide2.QtCore import Qt

class NotificationWidget(QWidget):
    instances = []

    def __init__(self, title, message):
        super().__init__()

        self.title = title
        self.message = message

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 设置固定大小
        self.setFixedSize(350, 120)

        layout = QVBoxLayout()

        lbl_title = QLabel(self.title)
        lbl_title.setStyleSheet("font-weight: bold; font-size: 14px; color: black;")

        lbl_message = QTextEdit(self.message)
        lbl_message.setReadOnly(True)
        lbl_message.setStyleSheet("font-size: 13px; background-color: rgba(0, 0, 0, 0); border: none; color: black;")

        btn_close = QPushButton("Confirm")
        btn_close.setStyleSheet("""
            QPushButton {
                background-color: #2d3341;
                color: #cddced;
                border: 1px solid #555;
                padding: 5px 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #3e4454;
            }
            QPushButton:pressed {
                background-color: #4c5265;
            }
        """)
        btn_close.clicked.connect(self.close)

        layout.addWidget(lbl_title)
        layout.addWidget(lbl_message)
        layout.addWidget(btn_close)

        self.setLayout(layout)

        # 将新通知添加到静态列表中
        NotificationWidget.instances.append(self)

        # 更新所有窗口位置
        self.update_positions()

        # 显示通知窗口
        self.show()

    def update_positions(self):
        # 计算通知窗口的位置
        total_height = 0
        screen_geometry = QApplication.primaryScreen().availableGeometry()

        for index, widget in enumerate(reversed(NotificationWidget.instances)):
            total_height += widget.height() + 10  # 添加一些间隔
            x = screen_geometry.width() - widget.width() - 20
            y = screen_geometry.height() - total_height - 20
            widget.move(x, y)

    def closeEvent(self, event):
        # 从静态列表中移除已关闭的通知窗口
        NotificationWidget.instances.remove(self)
        self.update_positions()  # 更新其他通知窗口的位置
        event.accept()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制一个带圆角的矩形作为背景
        rect = self.rect()
        rect.adjust(0, 0, -1, -1)
        painter.setBrush(QColor(255, 255, 255, 220))  # 设置背景颜色
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(rect, 10, 10)
