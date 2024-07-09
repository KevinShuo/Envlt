# -*- coding: utf-8 -*-
# @Time : 2024/6/21 14:08
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : mainWindow.py
# @Project : Envlt

import datetime
import getpass
import io
import os
from enum import Enum
from importlib import reload

from PIL import Image
from PySide2.QtCore import Qt, Signal
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from maya.OpenMayaUI import MQtUtil_mainWindow
from shiboken2 import wrapInstance

from ns_Envlt.config.json_config_factory import JsonConfigFactory
from ns_Envlt.data import database_data
from ns_Envlt.envlt_db import master_db, asset_db
from ns_Envlt.envlt_log import log_factory
from ns_Envlt.error import database_error
from ns_Envlt.ui import Envlt, envlt_messagebox, project_ui, scene_lib
from ns_Envlt.utils import os_util

reload(project_ui)
reload(scene_lib)
reload(os_util)
reload(Envlt)
reload(master_db)
reload(envlt_messagebox)
reload(log_factory)
reload(asset_db)


class PageType(Enum):
    """
        页面枚举
    """
    About = 0,
    Project = 1,


class mainWindow(QWidget):
    project_refresh = Signal()

    def __init__(self):
        """
            Envlt mainWindow
        """
        super().__init__()
        self.project_refresh.connect(self.refresh_project_page)
        # time
        self.now_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.envlt = Envlt.Ui_mainWindows()
        self.envlt.setupUi(self)
        self.setParent(wrapInstance(int(MQtUtil_mainWindow()), QWidget))
        self.setWindowFlags(Qt.Window)
        self.init_window()
        self.init_slot()
        self.log = log_factory.LogFactory("Envlt", True)
        # self.create_scene_lib_ui()
        self.show()

    def init_window(self):
        """
            创建窗口时候要执行的方法1
        """
        self.envlt.stackedWidget.setCurrentIndex(0)
        # init project database
        self.db_project = master_db.EnvltProjectDatabase()
        self.db_assets = asset_db.EnvltAssetDB()
        self.dialog = envlt_messagebox.EnvltDialog()

        # 构建Project页面

        self.project_ui = project_ui.ProjectUI()

        self.envlt.stackedWidget.addWidget(self.project_ui)
        # init check user
        self.user = getpass.getuser()
        blacklist_path = os.path.join(os.path.dirname(__file__), "../../config/blacklist.json")
        json_factory = JsonConfigFactory(blacklist_path)
        blacklist = json_factory.parser()["black_list"]
        if self.user in blacklist:
            self.dialog.warning("当前用户是封禁用户", "禁止用当前用户登录")
            self.close()
            raise AttributeError("封禁用户")

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
            self.refresh_project_page()
            self.envlt.stackedWidget.setCurrentWidget(self.project_ui)

    def refresh_project_page(self):
        """
        用于对Project页面场景操作后的自动刷新界面
        :return:
        """
        self.db_project = master_db.EnvltProjectDatabase()
        all_db = self.db_assets.get_asset_libs_data("project_data")
        self.project_ui.add_frames(all_db)
        self.project_ui.update_layout(force_update=True)

        del self.db_project

    def create_new_scene_ui(self):
        """
            Build new scene ui
        Returns:

        """
        self.db_project = master_db.EnvltProjectDatabase()

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
        all_name = self.db_project.get_all_scene_name()
        if all_name:
            self.create_scene_ui.comboBox_choose_project.addItems(all_name)

        self.init_create_scene_check_label()

    def init_create_scene_check_label(self):
        """
            创建新水平布局并插入原有布局实现重复场景名称检定提示

        :return:
        """
        # 创建场景名输入检定
        self.name_layout = QHBoxLayout()
        self.create_scene_ui.lineEdit_name.setStyleSheet("border: 1px solid #ccc; padding-right: 80px;")
        self.name_layout.addWidget(self.create_scene_ui.lineEdit_name)

        self.duplicate_label = QLabel("名称重复", self.create_scene_ui.lineEdit_name)
        self.duplicate_label.setStyleSheet("color: gray; font-size: 12px; opacity: 0.6;")
        self.duplicate_label.setVisible(False)
        self.name_layout.addWidget(self.duplicate_label)

        self.create_scene_ui.formLayout.setLayout(0, QFormLayout.FieldRole, self.name_layout)

        # 克隆场景名输入检定
        self.name_layout_2 = QHBoxLayout()
        self.create_scene_ui.lineEdit_name_2.setStyleSheet("border: 1px solid #ccc; padding-right: 80px;")
        self.name_layout_2.addWidget(self.create_scene_ui.lineEdit_name_2)

        self.duplicate_label_2 = QLabel("名称重复", self.create_scene_ui.lineEdit_name_2)
        self.duplicate_label_2.setStyleSheet("color: gray; font-size: 12px; opacity: 0.6;")
        self.duplicate_label_2.setVisible(False)
        self.name_layout_2.addWidget(self.duplicate_label_2)

        self.create_scene_ui.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.name_layout_2)

    def init_create_scene_slot(self):
        """
            初始化创建场景的信号

        Returns:

        """
        self.create_scene_ui.radioButton_create.toggled.connect(self.switch_new_exists_page)
        self.create_scene_ui.pushButton_create.clicked.connect(self.create_scene)
        self.create_scene_ui.lineEdit_name.textEdited.connect(self.check_scene_exists)
        self.create_scene_ui.lineEdit_name_2.textEdited.connect(self.check_scene_exists)
        self.widgetAction_choose_image.triggered.connect(self.choose_image)
        self.widgetAction_choose_image_2.triggered.connect(self.choose_image)

    def check_scene_exists(self, text: str):
        """
            实时检查场景是否存在数据库中，如果存在则给与提示并禁用创建按钮
        :param text:当前name文本框里的文本
        :return:
        """
        self.db_project = master_db.EnvltProjectDatabase()
        sender = self.sender()
        all_scene_name = self.db_project.get_all_scene_name()
        if all_scene_name:
            if sender == self.create_scene_ui.lineEdit_name:
                if text in all_scene_name:
                    self.create_scene_ui.lineEdit_name.setStyleSheet("border: 1px solid red;")
                    self.duplicate_label.setText("名称重复")
                    self.duplicate_label.setVisible(True)
                    self.create_scene_ui.pushButton_create.setEnabled(False)
                    self.create_scene_ui.pushButton_create.setStyleSheet("background-color: gray;")
                else:
                    self.create_scene_ui.lineEdit_name.setStyleSheet("")
                    self.duplicate_label.setVisible(False)
                    self.create_scene_ui.pushButton_create.setEnabled(True)
                    self.create_scene_ui.pushButton_create.setStyleSheet("")
            elif sender == self.create_scene_ui.lineEdit_name_2:
                if text in all_scene_name:
                    self.create_scene_ui.lineEdit_name_2.setStyleSheet("border: 1px solid red;")
                    self.duplicate_label_2.setText("名称重复")
                    self.duplicate_label_2.setVisible(True)
                    self.create_scene_ui.pushButton_create.setEnabled(False)
                    self.create_scene_ui.pushButton_create.setStyleSheet("background-color: gray;")
                else:
                    self.create_scene_ui.lineEdit_name_2.setStyleSheet("")
                    self.duplicate_label_2.setVisible(False)
                    self.create_scene_ui.pushButton_create.setEnabled(True)
                    self.create_scene_ui.pushButton_create.setStyleSheet("")
        else:
            pass

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
                self.log.write_log(self.log.critical, "禁止拷贝空场景")
                self.dialog.error("禁止拷贝空场景", str(e))

        self.project_refresh.emit()

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
        image_path = self.create_scene_ui.lineEdit_image.text()
        image_server_path = None
        if image_path and os.path.exists(image_path):
            """遗弃上传image的功能，改为读取图片二进制"""
            # img_scene = os_util.UIResource()
            # image_server_path = img_scene.upload_img(image)
            # if not image_server_path:
            #     self.dialog.error("上传图片失败", "上传图片到服务器失败,请联系TD")
            #     raise AttributeError("上传图片失败")
            """===================================="""
            with open(image_path, "rb") as image_file:
                original_image_data = image_file.read()

            with Image.open(image_path) as img:
                img.thumbnail((240, 180))  # Set the size of the thumbnail
                thumbnail_io = io.BytesIO()
                img.save(thumbnail_io, format=img.format)
                thumbnail_data = thumbnail_io.getvalue()

            image_data_dict = {
                "original": original_image_data,
                "small": thumbnail_data
            }
        elif not os.path.exists(image_path):
            self.dialog.error("图片路径不存在", "图片路径不存在")
            raise OSError("图片路径不存在")
        else:
            pass
        # description
        description = self.create_scene_ui.textEdit_description.toPlainText()

        # user
        scene_data = database_data.ProjectDbData(None, scene_name, str(image_data_dict), description, self.now_time,
                                                 self.now_time, self.user,
                                                 enable=True)
        try:
            self.db_project.create_new_scene(scene_data)
            self.db_assets.create_new_asset_table(scene_name)
            self.dialog.information("创建成功", f"创建{scene_name}场景 成功")
            del self.db_project
        except database_error.SceneExistsError as e:
            self.log.write_log(self.log.critical, "场景已经存在")
            self.dialog.error("错误", "场景已存在")

        self.project_refresh.emit()

    def _clone_scene(self):
        """
            克隆一个场景
        :return:
        """
        select_scene = self.create_scene_ui.comboBox_choose_project.currentText()
        name_after_clone = self.create_scene_ui.lineEdit_name_2.text()
        image_after_clone = self.create_scene_ui.lineEdit_image_2.text()
        description_after_clone = self.create_scene_ui.textEdit_description_2.toPlainText()
        # 获取原表的数据
        db = self.db_assets.get_asset_libs_data(select_scene)
        if not db:
            raise database_error.SceneAssetNoDataError("原始场景里没有数据,禁止克隆空的场景。")
        # 在总表里插入一行新的场景数据
        if image_after_clone and os.path.exists(image_after_clone):
            with open(image_after_clone, "rb") as image_file:
                original_image_data = image_file.read()

            with Image.open(image_after_clone) as img:
                img.thumbnail((240, 180))  # Set the size of the thumbnail
                thumbnail_io = io.BytesIO()
                img.save(thumbnail_io, format=img.format)
                thumbnail_data = thumbnail_io.getvalue()

            image_data_dict = {
                "original": original_image_data,
                "small": thumbnail_data
            }
        clone_scene_data = database_data.ProjectDbData(None, name_after_clone, str(image_data_dict),
                                                       description_after_clone,
                                                       self.now_time,
                                                       self.now_time, self.user, enable=True)
        try:
            self.db_project.create_new_scene(clone_scene_data)
            self.db_assets.create_new_asset_table(name_after_clone)
            self.db_assets.insert_data_to_table(db, name_after_clone)
            self.dialog.information("创建成功", f"创建{name_after_clone}场景 成功")
            del self.db_project
        except database_error.SceneExistsError as e:
            self.log.write_log(self.log.critical, "场景已存在")
            self.dialog.error("错误", "场景已存在")

        self.project_refresh.emit()

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

    # def create_scene_lib_ui(self):
    #     from ns_Envlt.ui import scene_lib
    #     reload(scene_lib)
    #     self.widget_scene_lib = QWidget(self)
    #     self.widget_scene_lib.setWindowFlags(Qt.Window)
    #     _scene_lib = scene_lib.Ui_Form()
    #     _scene_lib.setupUi(self.widget_scene_lib)
    #     self.widget_scene_lib.show()
