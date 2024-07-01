# -*- coding: utf-8 -*-
# @Time : 2024/7/1 17:34
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : json_config_factory.py
# @Project : Envlt
import json
from .config_base import ConfigBase
from ns_Envlt.error import config_error
from typing import *


class JsonConfigFactory(ConfigBase):
    def __init__(self, config_path: str):
        super().__init__(config_path)

    def parser(self) -> Any:
        """
            解析json数据

        :return:json数据类型
        """
        config_content = self.read_config_content()
        try:
            json_data = json.loads(config_content)
            return json_data
        except:
            raise config_error.JsonContentError("获取json数据失败")

    @property
    def config_path(self):
        if not str(self._config_path).endswith("json"):
            raise config_error.FileFormatError("文件不是 JSON 格式")
        return super().config_path

    @config_path.setter
    def config_path(self, value: str):
        if not value.endswith("json"):
            raise config_error.FileFormatError("文件不是 JSON 格式")
        super(JsonConfigFactory, JsonConfigFactory).config_path.__set__(self, value)
