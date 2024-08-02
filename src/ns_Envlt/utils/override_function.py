"""

该模块主要存放重写的方法

"""
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

"""
HoverableFrame为重写QFrame方法，可以触发对应的点击信号。

"""


class HoverableFrame(QFrame):
    clicked = Signal()  # 定义一个信号
    rightClicked = Signal()
    doubleClicked = Signal()

    def __init__(self, parent=None):
        super(HoverableFrame, self).__init__(parent)
        # Create a shadow effect
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(QColor(0, 0, 0, 160))
        self.setGraphicsEffect(shadow)
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Raised)
        self.setStyleSheet("""
            QFrame {
                border: 1px solid #414654;
                border-radius: 10px;
                background-color: #414654;
            }
            QWidget#card_frame:hover {
                border: 1px solid #e0e0e0;
            }
        """)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()  # 触发左键点击信号
        elif event.button() == Qt.RightButton:
            self.rightClicked.emit()  # 触发右键点击信号
        super(HoverableFrame, self).mousePressEvent(event)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.doubleClicked.emit()  # 触发左键双击信号
        super(HoverableFrame, self).mouseDoubleClickEvent(event)

    # def enterEvent(self, event):
    #     super(HoverableFrame, self).enterEvent(event)
    #
    # def leaveEvent(self, event):
    #     super(HoverableFrame, self).leaveEvent(event)
    #


"""
ConfirmDialog为重写的确认窗口
"""


class ConfirmDialog(QDialog):
    def __init__(self, message, parent=None):
        super(ConfirmDialog, self).__init__(parent)

        self.setWindowTitle("确认删除")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setFixedHeight(100)
        self.setFixedWidth(200)
        self.setStyleSheet("""
            QDialog {
                background-color: #2d3341;
                color: #cddced;
                border: 1px solid #555;
                border-radius: 10px;
            }
            QLabel {
                font-size: 12px;
                color: white;
            }
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

        self.init_ui(message)

    def init_ui(self, message):
        layout = QVBoxLayout(self)

        message_label = QLabel(message)
        layout.addWidget(message_label)

        button_layout = QHBoxLayout()

        self.yes_button = QPushButton("Yes")
        self.no_button = QPushButton("No")

        button_layout.addWidget(self.yes_button)
        button_layout.addWidget(self.no_button)

        layout.addLayout(button_layout)

        self.yes_button.clicked.connect(self.accept)
        self.no_button.clicked.connect(self.reject)


def create_rounded_pixmap(pixmap: QPixmap, radius: int) -> QPixmap:
    """
        creates a rounded QPixmap from a QPixmap

    :param pixmap: original QPixmap
    :param radius: radius of rounded QPixmap
    :return:
    """
    rounded_pixmap = QPixmap(pixmap)
    rounded_pixmap.fill(Qt.transparent)

    painter = QPainter(rounded_pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setRenderHint(QPainter.SmoothPixmapTransform)

    path = QPainterPath()
    path.addRoundedRect(QRectF(pixmap.rect()), radius, radius, Qt.RelativeSize)

    painter.setClipPath(path)
    painter.drawPixmap(0, 0, pixmap)
    painter.end()
    return rounded_pixmap
