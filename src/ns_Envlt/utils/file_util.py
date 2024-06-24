# -*- coding: utf-8 -*-
# @Time : 2024/6/24 12:54
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : file_util.py
# @Project : Envlt
import traceback
from typing import *
import hashlib
import os
import shutil


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
        image_path, image_name = os.path.split(src_img_path)
        target_path = str(os.path.join(self.img_project_path, image_name).replace('\\', '/'))
        # 如果 服务器存在相同的图片，则比较俩个图片的md5，如果不相同重新拷贝
        if os.path.exists(target_path):
            with open(src_img_path, "rb", encoding="utf-8") as src_file:
                md5_src = hashlib.md5(src_file.read())

            with open(target_path, "rb", encoding="utf-8") as target_file:
                md5_target = hashlib.md5(target_file.read())
            if md5_target == md5_src:
                return target_path
            else:
                try:
                    os.remove(target_file)
                    shutil.copy2(src_img_path, target_file)
                    return target_path
                except Exception as e:
                    print(traceback.format_exc())
                    return False
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
