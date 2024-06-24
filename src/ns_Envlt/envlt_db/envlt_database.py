# -*- coding: utf-8 -*-
# @Time : 2024/6/24 14:30
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : envlt_database.py
# @Project : Envlt
import dataclasses
from typing import *
import os
import sqlite3


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


class EnvltProjectDatabase:
    def __init__(self):
        self.conn = sqlite3.connect(self.db_path)

    def create_new_scene(self, project_data: ProjectDbData):
        """
            创建一个新的场景

        Args:
            project_data:项目数据

        Returns:

        """
        command = f"""INSERT INTO project_data (name, image, description, create_date, modify_date, create_user, enable)
values (?, ?, ?, ?, ?, ?, ?)"""
        c = self.conn.cursor()
        c.execute(command, (
            project_data.scene_name, project_data.image_path, project_data.description, project_data.create_date,
            project_data.modify_date, project_data.create_user, project_data.enable))
        self.conn.commit()

    def get_all_scene_name(self) -> List[str]:
        scene_name_list = []
        command = f"""SELECT name
from project_data"""
        c = self.conn.cursor()
        c.execute(command)
        datas = c.fetchall()
        if not datas:
            return
        for data in datas:
            scene_name_list.append(data[0])
        return sorted(scene_name_list)

    @property
    def db_path(self) -> str:
        """
          db 文件路径
        Returns:

        """
        db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                               "database/project_view_db.sqlite").replace('\\', '/')
        if not os.path.exists(db_path):
            raise OSError("Sqlite database is not exists")
        return db_path

    @db_path.setter
    def db_path(self, path: str):
        self.db_path = path
