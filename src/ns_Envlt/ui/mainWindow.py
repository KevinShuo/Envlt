# -*- coding: utf-8 -*-
# @Time : 2024/6/21 14:08
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : mainWindow.py
# @Project : Envlt
import os
from enum import Enum
from ns_Envlt.ui import Envlt
from ns_Envlt.envlt_db import envlt_database
from ns_Envlt.utils import os_util
from maya.OpenMayaUI import MQtUtil_mainWindow
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import Qt
from shiboken2 import wrapInstance
from importlib import reload

reload(os_util)
reload(envlt_database)


class PageType(Enum):
    """
        页面枚举
    """
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
        """
            创建窗口时候要执行的方法
        """
        self.envlt.stackedWidget.setCurrentIndex(0)
        # init project database
        self.envlt_project_database = envlt_database.EnvltProjectDatabase()
        # db1 = envlt_database.ProjectDbData(scene_name="b1", image_path="aa.jpg", description="fff", create_date="129.0",
        #                                    modify_date="222", create_user="ws", enable=True)
        # self.envlt_project_database.create_new_scene(db1)

    def init_slot(self):
        """
            初始化信号
        Returns:

        """
        self.envlt.about_button.clicked.connect(lambda: self.switch_page(PageType.About))
        self.envlt.project.clicked.connect(lambda: self.switch_page(PageType.Project))
        self.envlt.new_button.clicked.connect(self.create_new_scene_ui)

    def switch_page(self, page: PageType):
        """
            切换页面
        Args:
            page: 页面属性

        Returns: None

        """
        if page == PageType.About:
            self.envlt.stackedWidget.setCurrentIndex(0)
        elif page == PageType.Project:
            self.envlt.stackedWidget.setCurrentIndex(1)

    def create_new_scene_ui(self):
        """
            Build new scene ui
        Returns:

        """
        from ns_Envlt.ui import create_new_scene
        reload(create_new_scene)
        self.create_scene_ui = create_new_scene.Ui_create_scene()
        create_scene_widget = QWidget(self)
        self.create_scene_ui.setupUi(create_scene_widget)
        create_scene_widget.setWindowFlags(Qt.Window)
        create_scene_widget.show()
        self.init_create_scene_ui()
        self.init_create_scene_slot()

    def init_create_scene_ui(self):
        # set image
        file_utils = os_util.UIResource()
        select_image = file_utils.get_icon_path("select_image.png")
        select_image_icon = QPixmap(select_image)
        select_image_icon.scaledToWidth(64)
        self.widgetAction_choose_image = QWidgetAction(self.create_scene_ui.lineEdit_image)
        self.widgetAction_choose_image.setIcon(QIcon(select_image_icon))
        self.create_scene_ui.lineEdit_image.addAction(self.widgetAction_choose_image, QLineEdit.TrailingPosition)
        # get scene name
        all_name = self.envlt_project_database.get_all_scene_name()
        self.create_scene_ui.comboBox_choose_project.addItems(all_name)

    def init_create_scene_slot(self):
        """
            初始化创建场景的信号

        Returns:

        """
        self.create_scene_ui.radioButton_create.toggled.connect(self.switch_new_exists_page)
        self.create_scene_ui.pushButton_create.clicked.connect(self.create_new_scene)
        self.widgetAction_choose_image.triggered.connect(self.choose_image)

    def create_new_scene(self):
        """
            创建一个新的场景
            步骤
             1.获取场景名字
             2.获取场景图片路径
                - 如果图片存在
                    - 比较md5数值 如果数值相同 则直接返回服务器的路径，如果数值不相同，拷贝一个新的文件到服务器，并且重命名
        Returns:

        """
        if not self.create_scene_ui.lineEdit_name.text():
            QMessageBox.critical(self, "error", "请填写插件名字")
            return
        scene_name = self.create_scene_ui.lineEdit_name.text()
        image = self.create_scene_ui.lineEdit_image.text()
        if image and os.path.exists(image):
            img_scene = os_util.UIResource()
            server_path = img_scene.upload_img(image)
            if not server_path:
                QMessageBox.critical(self, "error", "上传图片失败")
            print(server_path)
        elif not os.path.exists(image):
            QMessageBox.critical(self, "error", "图片路径不存在")
        elif not image:
            pass
        else:
            pass

        # scene_data = envlt_database.ProjectDbData()

    def choose_image(self):
        file_dialog_util = os_util.QFileDialogUtil()
        last_path = file_dialog_util.get_last_choose_path()
        file_path, _ = QFileDialog.getOpenFileName(self, "请选择一个图片", "c:/" if not last_path else last_path)
        if not file_path:
            return
        self.create_scene_ui.lineEdit_image.setText(file_path)
        file_dialog_util.wirte_last_choose_path(file_path)

    def switch_new_exists_page(self):
        """
            切换新建拷贝页面

        Returns:

        """
        if self.create_scene_ui.radioButton_create.isChecked():
            self.create_scene_ui.stackedWidget.setCurrentIndex(0)
        elif self.create_scene_ui.radioButton_clone.isChecked():
            self.create_scene_ui.stackedWidget.setCurrentIndex(1)
        else:
            raise AttributeError("Has not support this page")
