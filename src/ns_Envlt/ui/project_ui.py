"""
Project页面下的场景预览

当前展示信息有：预览图，场景名称

当前开发若要获取更多场景信息，单击项目可以在输出中查看到场景的具体资产信息

"""
import os
from importlib import reload

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ns_Envlt.envlt_db import master_db, asset_db
from ns_Envlt.utils import override_function
from . import image_window

reload(override_function)
reload(master_db)
reload(asset_db)
reload(image_window)


class ProjectUI(QWidget):
    def __init__(self):
        super(ProjectUI, self).__init__()

        self.db_projects = master_db.EnvltProjectDatabase()
        self.db_assets = asset_db.EnvltAssetDB()

        self.max_width = 200
        self.max_height = 150
        self.current_columns = -1

        init_db = self.db_assets.get_asset_libs_data("project_data")
        self.init_widget()
        self.init_layout()
        self.init_slot()
        self.add_frames(init_db)
        self.resizeEvent = self.on_resize

    def init_widget(self):
        self.search_label = QLabel("Search:")
        self.search_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #cddced;
            }
        """)

        self.search_lineEdit = QLineEdit()
        self.search_lineEdit.setStyleSheet("""
            QLineEdit {
                background-color: #2d3341;
                color: white;
                border: 1px solid #555;
                border-radius: 8px;
                padding: 5px;
            }
            QLineEdit:focus {
                border: 1px solid #cddced;
            }
        """)

    def init_layout(self):
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setStyleSheet("background-color: rgb(41, 46, 59);")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QGridLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)

        HLayout = QHBoxLayout()
        HLayout.addWidget(self.search_label)
        HLayout.addWidget(self.search_lineEdit)
        # 主布局
        main_layout = QVBoxLayout(self)
        main_layout.addLayout(HLayout)
        main_layout.addWidget(self.scroll_area)
        self.setLayout(main_layout)

    def init_slot(self):
        self.search_lineEdit.textChanged.connect(self.filter_frames)

    def filter_frames(self):
        search_text = self.search_lineEdit.text()
        all_db = self.db_assets.get_asset_libs_data("project_data")
        filtered_data = [d for d in all_db if search_text in d.scene_name]
        self.add_frames(filtered_data)

    def create_frame(self, image_data: str, scene_name: str):
        """

        批量创建project页面下的场景元素时所调用的函数，若要修改每个QFrame包含部件可以在这个函数中修改

        :param image_data: 预览图路径
        :param scene_name: 场景名称
        :return:
        """

        # 创建一个HoverableFrame
        card_frame = override_function.HoverableFrame()
        card_frame.setFrameShape(QFrame.Box)
        card_frame.setFrameShadow(QFrame.Raised)
        card_frame.setFixedSize(self.max_width, self.max_height)  # 设置固定大小
        card_frame.clicked.connect(self.on_frame_clicked)  # 连接点击信号到槽函数
        card_frame.rightClicked.connect(self.on_frame_right_clicked)

        # 设置布局
        layout = QVBoxLayout(card_frame)

        # 设置图片
        image = QLabel()
        pixmap = QPixmap()
        d = QByteArray(image_data)
        pixmap.loadFromData(d)
        scale_pixmap = pixmap.scaled(self.max_width, self.max_height, Qt.KeepAspectRatio)  # 缩小图片高度比例
        image.setPixmap(scale_pixmap)
        image.setAlignment(Qt.AlignCenter)
        layout.addWidget(image)

        # 设置标签
        label = QLabel(scene_name)
        label.setObjectName("frameLabel")  # 设置对象名称
        label.setStyleSheet("font-size: 14px; font-weight: bold; color: white; padding-top: 5px;")  # 设置文字样式
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        layout.setContentsMargins(5, 5, 5, 5)  # 设置内边距

        return card_frame

    def update_layout(self, force_update=False):
        # 计算每行可以放置的QFrame数量
        num_columns = max(1, self.width() // (self.max_width + 20))
        if num_columns == self.current_columns and not force_update:
            return

            # 更新当前列数
        self.current_columns = num_columns

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

    def on_resize(self, event):
        self.update_layout()
        QWidget.resizeEvent(self, event)

    def add_frames(self, project_data):
        self.frames = []
        if project_data:
            for i in project_data:
                frame = self.create_frame(eval(i.image_data), f"Scene: {i.scene_name} ")
                self.frames.append(frame)
            self.update_layout(force_update=True)  # 初始布局时强制更新
        else:
            pass


    def on_frame_clicked(self):
        """
        获取鼠标点击场景的具体信息

        :return:
        """
        sender = self.sender()
        label = sender.findChild(QLabel, "frameLabel")  # 根据对象名称查找QLabel
        if label:
            scene_name = label.text().split(":")[-1].strip()
            scene_db = self.db_assets.get_asset_libs_data(scene_name)
            print(scene_db)

    def on_frame_right_clicked(self):
        """
        触发右键信号，并触发对应操作
        :return:
        """

        sender = self.sender()
        label = sender.findChild(QLabel, "frameLabel")
        if label:
            scene_name = label.text().split(":")[-1].strip()
            self.show_context_menu(sender, scene_name)

    def show_context_menu(self, frame, scene_name):
        """
        显示右键上下文菜单
        :param frame: 当前右键场景的QFrame，用于更新页面
        :param scene_name: 场景名称,作为参数传进对应功能
        :return:
        """
        context_menu = QMenu(self)
        delete_action = context_menu.addAction("删除")
        # 添加更多的选项
        pic_view = context_menu.addAction("参考图")

        action = context_menu.exec_(QCursor.pos())
        if action == delete_action:
            self.confirm_delete_scene(frame, scene_name)
        elif action == pic_view:
            self.open_image(scene_name)

    def confirm_delete_scene(self, frame, scene_name):
        dialog = override_function.ConfirmDialog(f"确定要删除场景 '{scene_name}' 吗？", self)
        result = dialog.exec_()
        if result == QDialog.Accepted:
            self.delete_scene(frame, scene_name)

    def delete_scene(self, frame, scene_name):
        """
        删除场景
        :param frame: 当前右键场景的QFrame，用于更新页面
        :param scene_name: 场景名称,作为参数传进删除数据库信息函数
        :return:
        """
        # 在数据库中删除场景
        self.db_projects.delete_data_from_project_data(scene_name)
        self.db_assets.drop_table(scene_name)

        # 从布局中移除并删除 frame
        self.scroll_layout.removeWidget(frame)
        frame.setParent(None)
        self.frames.remove(frame)
        self.update_layout(force_update=True)

        print(f"{scene_name} deleted")

    def open_image(self, scene_name):
        all_db = self.db_assets.get_asset_libs_data("project_data")
        scene_data = next((d for d in all_db if d.scene_name == scene_name), None)
        if scene_data:
            a = image_window.ImageWindow(eval(scene_data.image_data))
            a.exec_()
        else:
            QMessageBox.warning(self, "Error", "Image not found or path is incorrect.")
