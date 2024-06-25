# -*- coding: utf-8 -*-
# @Time : 2024/6/25 10:13
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : temp.py
# @Project : Envlt
import json
import os
import tempfile
import traceback


class EnvltTemp:
    def __init__(self, plugin_name: str):
        """
            操作temp文件类
            此类会在temp目录下创建一个新的plugin文件夹，里面存放临时文件
        Args:
            plugin_name:插件名字
        """
        self.plugin_name = plugin_name

    def create_config_file(self, file_name: str, content: str):
        """
            创建一个新的配置文件

        Args:
            file_name:配置文件名
            content:文件内容

        Returns:

        """

        config_path = os.path.join(self.config_dir_path, file_name).replace('\\', '/')
        with open(config_path, "w+", encoding="utf-8") as config_file:
            config_file.write(content)

    def read_config_file(self, file_name: str):
        """
            读取配置文件内容

        :param file_name: 配置文件名
        :return: 配置文件内容
        """
        p = os.path.join(self.config_dir_path, file_name).replace('\\', '/')
        if not os.path.exists(p):
            return
        with open(p, "r+", encoding="utf-8") as config_file:
            json_data = json.loads(config_file.read())
        return json_data

    @property
    def temp_plugin_path(self):
        """
        Temp 插件总路径

        Returns:

        """
        p = os.path.join(tempfile.gettempdir(), self.plugin_name).replace('\\', '/')
        if not os.path.exists(p):
            os.makedirs(p)
        return p

    @property
    def config_dir_path(self):
        """
            配置目录路径

        Returns:

        """
        p = os.path.join(self.temp_plugin_path, "config").replace('\\', '/')
        if not os.path.exists(p):
            os.makedirs(p)
        return p
