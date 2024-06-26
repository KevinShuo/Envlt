# -*- coding: utf-8 -*-
# @Time : 2024/6/26 15:22
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : database_data.py
# @Project : Envlt
import dataclasses
from typing import *


@dataclasses.dataclass
class ProjectDbData:
    scene_name: str
    image_path: Optional[str]
    description: Optional[str]
    create_date: str
    modify_date: str
    create_user: str
    enable: bool

    def __str__(self):
        return f"""======== ProjectDbData ========\n
        scene_name: {self.scene_name}\n
        image_path: {self.image_path}\n
        description: {self.description}\n
        create_date: {self.create_date}\n
        modify_date: {self.modify_date}\n
        create_user: {self.create_user}\n
        enable: {self.enable}\n
=================================="""

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
