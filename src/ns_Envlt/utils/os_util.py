# -*- coding: utf-8 -*-
# @Time : 2024/6/24 12:54
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : os_util.py
# @Project : Envlt
import traceback
import hashlib
import os
import shutil
import json
from typing import *
from importlib import reload
from ns_Envlt.temp_pkg import temp

reload(temp)


class UIResource:
    def __init__(self):
        """
            UI资源类
        """
        pass

    def get_icon_path(self, icon_name: str) -> str:
        """
            get icon path
        Args:
            icon_name: icon name

        Returns: icon absolute

        """
        icon_path = os.path.join(self.resource_path, icon_name).replace('\\', '/')
        if not os.path.exists(icon_path):
            raise OSError("Icon path is not exists")
        return icon_path

    def upload_img(self, src_img_path: str) -> Union[str, bool]:
        """
            上传图片到服务器

        Args:
            src_img_path:本地图片路径

        Returns:服务器图片路径

        """
        if not os.path.exists(src_img_path):
            raise OSError("Src image path is not exists")
        # 获取原始图像的md5
        with open(src_img_path, "rb") as src_file:
            md5_src = hashlib.md5(src_file.read())
        image_path, image_name = os.path.split(src_img_path)
        n, p = os.path.splitext(image_name)
        target_name = f"{md5_src.hexdigest()}{p}"
        target_path = str(os.path.join(self.img_project_path, target_name).replace('\\', '/'))
        # 如果 服务器存在相同的图片，则比较俩个图片的md5，如果不相同重新拷贝
        if os.path.exists(target_path):
            return target_path
        else:
            try:
                shutil.copy2(src_img_path, target_path)
                return target_path
            except Exception as e:
                print(traceback.format_exc())
                return False

    @property
    def resource_path(self):
        """
            resource path
        Returns:

        """
        resource_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ui/resources").replace('\\', '/')
        if not os.path.exists(resource_path):
            raise OSError("Resource path is not exists")
        return resource_path

    @property
    def img_project_path(self):
        img_project_path = os.path.join(self.resource_path, "img_project")
        if not os.path.exists(img_project_path):
            raise OSError("img project is not exists")
        return img_project_path


class QFileDialogUtil:
    def __init__(self):
        """
        Qt FileDialog 工具类
        """
        self.temp = temp.EnvltTemp("Envlt")

    def write_last_choose_path(self, path: str):
        """
            记录QFileDialog最后选择的路径
        """
        path_dict = json.dumps({"path": os.path.dirname(path)})
        self.temp.create_config_file("file_dialog_last_choose.json", path_dict)

    def get_last_choose_path(self):
        """
            获取最后一次选择的路径
        :return:
        """
        data = self.temp.read_config_file("file_dialog_last_choose.json")
        if not data:
            return
        return data["path"]
