import sys

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

with open(r"C:\dev\maya\Envlt\src\ns_Envlt\ui\resources\img_project\4bf88be658fe4d482f3444981a592404.png",
          "rb") as image_file:
    data = QByteArray(image_file.read())
    print(data)
    # QPixmap()


class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        vbox_main = QVBoxLayout()
        label = QLabel()
        label.setPixmap(pixmap)
        vbox_main.addWidget(label)
        self.setLayout(vbox_main)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ImageWindow()
    sys.exit(app.exec_())
