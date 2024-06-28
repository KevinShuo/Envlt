# -*- coding: utf-8 -*-
# @Time : 2024/6/21 14:08
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : mainWindow.py
# @Project : Envlt
import datetime
import getpass
import os
from enum import Enum
from ns_Envlt.ui import Envlt, envlt_messagebox,project_ui
from ns_Envlt.data import database_data
from ns_Envlt.envlt_db import envlt_database
from ns_Envlt.utils import os_util
from ns_Envlt.error import database_error
from maya.OpenMayaUI import MQtUtil_mainWindow
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import Qt
from shiboken2 import wrapInstance
from importlib import reload



reload(project_ui)

reload(os_util)
reload(Envlt)
reload(envlt_database)
reload(envlt_messagebox)


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

        # time
        self.now_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.envlt = Envlt.Ui_mainWindows()
        self.envlt.setupUi(self)
        self.setParent(wrapInstance(int(MQtUtil_mainWindow()), QWidget))
        self.setWindowFlags(Qt.Window)
        self.init_window()
        self.init_slot()
        self.show()

    def init_window(self):
        """
            创建窗口时候要执行的方法1
        """
        self.envlt.stackedWidget.setCurrentIndex(0)
        # init project database
        self.envlt_project_database = envlt_database.EnvltProjectDatabase()

        self.dialog = envlt_messagebox.EnvltDialog()

        # test
        self.project_ui = project_ui.ProjectUI()
        self.envlt.stackedWidget.addWidget(self.project_ui)



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
            # self.envlt.stackedWidget.setCurrentIndex(1)

            # test
            self.envlt.stackedWidget.setCurrentWidget(self.project_ui)

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

        self.widgetAction_choose_image_2 = QWidgetAction(self.create_scene_ui.lineEdit_image_2)
        self.widgetAction_choose_image_2.setIcon(QIcon(select_image_icon))
        self.create_scene_ui.lineEdit_image_2.addAction(self.widgetAction_choose_image_2, QLineEdit.TrailingPosition)
        # get scene name
        all_name = self.envlt_project_database.get_all_scene_name()
        if all_name:
            self.create_scene_ui.comboBox_choose_project.addItems(all_name)

    def init_create_scene_slot(self):
        """
            初始化创建场景的信号

        Returns:

        """
        self.create_scene_ui.radioButton_create.toggled.connect(self.switch_new_exists_page)
        self.create_scene_ui.pushButton_create.clicked.connect(self.create_scene)
        self.widgetAction_choose_image.triggered.connect(self.choose_image)
        self.widgetAction_choose_image_2.triggered.connect(self.choose_image)

    def create_scene(self):
        """
            创建一个新的场景
                1. 创建一个新的场景(空的)
                2. 根据已有场景 拷贝已有的场景到新的场景里
        :return:
        """
        if self.create_scene_ui.radioButton_create.isChecked():
            self._create_new_scene()
        else:
            try:
                self._clone_scene()
            except database_error.SceneAssetNoDataError as e:
                self.dialog.error("禁止拷贝空场景", str(e))

    def _create_new_scene(self):
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
            self.dialog.warning("信息不全", "请填写场景名称")
            return
        # scene name
        scene_name = self.create_scene_ui.lineEdit_name.text()
        # image path
        image = self.create_scene_ui.lineEdit_image.text()
        image_server_path = None
        if image and os.path.exists(image):
            img_scene = os_util.UIResource()
            image_server_path = img_scene.upload_img(image)
            if not image_server_path:
                self.dialog.error("上传图片失败", "上传图片到服务器失败,请联系TD")
                raise AttributeError("上传图片失败")
        elif not os.path.exists(image):
            self.dialog.error("图片路径不存在", "图片路径不存在")
            raise OSError("图片路径不存在")
        else:
            pass
        # description
        description = self.create_scene_ui.textEdit_description.toPlainText()

        # user
        user = getpass.getuser()

        scene_data = database_data.ProjectDbData(scene_name, image_server_path, description, self.now_time,
                                                 self.now_time, user,
                                                 enable=True)
        try:
            self.envlt_project_database.create_new_scene(scene_data)
            self.envlt_project_database.create_new_asset_table(scene_name)
            self.dialog.information("创建成功", f"创建{scene_name}场景 成功")
            del self.envlt_project_database
        except database_error.SceneExistsError as e:
            self.dialog.error("错误", "场景已存在")

    def _clone_scene(self):
        """
            克隆一个场景
        :return:
        """
        select_scene = self.create_scene_ui.comboBox_choose_project.currentText()
        name_after_clone = self.create_scene_ui.lineEdit_name_2.text()
        image_after_clone = self.create_scene_ui.lineEdit_image_2.text()
        description_after_clone = self.create_scene_ui.textEdit_description_2.toPlainText()
        user = getpass.getuser()
        # 获取原表的数据
        db = self.envlt_project_database.get_asset_libs_data(select_scene)
        if not db:
            raise database_error.SceneAssetNoDataError("原始场景里没有数据,禁止克隆空的场景。")
        # 在总表里插入一行新的场景数据
        clone_scene_data = database_data.ProjectDbData(name_after_clone, image_after_clone, description_after_clone,
                                                       self.now_time,
                                                       self.now_time, user, enable=True)
        try:
            self.envlt_project_database.create_new_scene(clone_scene_data)
            self.envlt_project_database.create_new_asset_table(name_after_clone)
            self.envlt_project_database.insert_data_to_table(db, name_after_clone)
            self.dialog.information("创建成功", f"创建{name_after_clone}场景 成功")
            del self.envlt_project_database
        except database_error.SceneExistsError as e:
            self.dialog.error("错误", "场景已存在")


    def choose_image(self):

        file_dialog_util = os_util.QFileDialogUtil()
        last_path = file_dialog_util.get_last_choose_path()
        # file_path, _ = QFileDialog.getOpenFileName(self, "请选择一个图片", "c:/" if not last_path else last_path)
        file_types = "Images (*.png *.xpm *.jpg *.jpeg *.bmp *.gif)"
        file_path, _ = QFileDialog.getOpenFileName(self, "请选择一个图片", "c:/" if not last_path else last_path,
                                                   file_types)

        if not file_path:
            return
        # 获取并判断触发槽函数对象
        sender = self.sender()
        if sender == self.widgetAction_choose_image:
            self.create_scene_ui.lineEdit_image.setText(file_path)
        elif sender == self.widgetAction_choose_image_2:
            self.create_scene_ui.lineEdit_image_2.setText(file_path)
        file_dialog_util.write_last_choose_path(file_path)

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
