# -*- coding: utf-8 -*-
# @Time : 2024/6/26 15:22
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : database_data.py
# @Project : Envlt
from importlib import reload
import dataclasses
from typing import *
from ns_Envlt.data import asset_type

reload(asset_type)


@dataclasses.dataclass
class ProjectDbData:
    """
        全局场景数据
    """
    scene_name: str
    image_path: Optional[str]
    description: Optional[str]
    create_date: str
    modify_date: str
    create_user: str
    enable: bool

    def __str__(self):
        return (
            f"======== ProjectDbData ========\n"
            f"scene_name: {self.scene_name}\n"
            f"image_path: {self.image_path}\n"
            f"description: {self.description}\n"
            f"create_date: {self.create_date}\n"
            f"modify_date: {self.modify_date}\n"
            f"create_user: {self.create_user}\n"
            f"enable: {self.enable}\n"
            f"=================================="
        )

    def __eq__(self, other):
        if isinstance(other, ProjectDbData):
            return (self.scene_name == other.scene_name and
                    self.image_path == other.image_path and
                    self.description == other.description and
                    self.create_date == other.create_date and
                    self.modify_date == other.modify_date and
                    self.create_user == other.create_user and
                    self.enable == other.enable)
        return False

    def __hash__(self):
        return hash(
            (self.scene_name, self.image_path, self.description, self.create_date, self.modify_date, self.create_user,
             self.enable))


@dataclasses.dataclass
class AssetDbData:
    _id: str
    name: str
    path: Union[str, dict]
    asset_type: asset_type.AssetType
    tab_type: str
    image: str
    description: str
    labels: List[str]
    enable: bool

    def __str__(self):
        labels_str = ', '.join(self.labels)  # 将标签列表转换为字符串
        path_str = self.path if isinstance(self.path, str) else str(self.path)

        return (
            f"======== AssetDbData ========\n"
            f"_id: {self._id}\n"
            f"name: {self.name}\n"
            f"path: {path_str}\n"
            f"asset_type: {self.asset_type}\n"
            f"tab_type: {self.tab_type}\n"
            f"image: {self.image}\n"
            f"description: {self.description}\n"
            f"labels: {labels_str}\n"
            f"enable: {self.enable}\n"
            f"=================================="
        )

    def __eq__(self, other):
        if isinstance(other, AssetDbData):
            return (self._id == other._id and
                    self.name == other.name and
                    self.path == other.path and
                    self.asset_type == other.asset_type and
                    self.tab_type == other.tab_type and
                    self.image == other.image and
                    self.description == other.description and
                    self.labels == other.labels and
                    self.enable == other.enable)
        return False

    def __hash__(self):
        return hash(
            (self._id, self.name, self.path, self.asset_type, self.tab_type, self.image, self.description,
             tuple(self.labels), self.enable))


@dataclasses.dataclass
class NoExistsData:
    name: str

    def __str__(self):
        return f"{self.name} is not exists"

    def __eq__(self, other):
        if isinstance(other, NoExistsData):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)
