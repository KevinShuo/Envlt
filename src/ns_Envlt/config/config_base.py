# -*- coding: utf-8 -*-
# @Time : 2024/7/1 17:27
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : config_base.py
# @Project : Envlt
import os


class ConfigBase:
    def __init__(self, config_path: str):
        """
            配置项基类

        :param config_path:配置文件路径
        """
        self._config_path = config_path

    def read_config_content(self) -> str:
        """
            读取配置文件内容(没有进行序列化(serializer))

        :return:配置文件内容
        """
        with open(self.config_path, "r+", encoding="utf-8") as config_file:
            config_content = config_file.read()
        return config_content

    @property
    def config_path(self):
        if not os.path.exists(self._config_path):
            raise FileNotFoundError("Config path is not exists")
        return self._config_path

    @config_path.setter
    def config_path(self, value: str):
        if not os.path.exists(value):
            raise FileNotFoundError("Config path is not exists")
        self._config_path = value
