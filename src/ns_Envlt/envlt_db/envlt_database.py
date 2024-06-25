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


class SceneExistsError(Exception):
    """
        场景已存在错误
    """
    pass


class EnvltProjectDatabase:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(EnvltProjectDatabase, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
            单例模式，控制场景总表数据
        """
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
        rt_data = self.get_scene_data(scene_name=project_data.scene_name)
        if rt_data:
            raise SceneExistsError("场景已存在")
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

    def get_scene_data(self, scene_name: Union[str, List[str]]) -> Optional[
        Union[ProjectDbData, List[ProjectDbData], Tuple[List[ProjectDbData], List[NoExistsData]]]]:
        """
            从服务器中获取场景数据 （支持多数查询，和单个查询）

            1.单数查询
                    - 如果场景不存在返回空
                    - 如果场景存在返回该场景数据(ProjectDbData)
            2. 多数查询
                    -返回一个元组(存在数据，未存在数据)
        :param scene_name: 场景名字，支持单个/多数查询
        :return: 1.单数查询
                    - 如果场景不存在返回空
                    - 如果场景存在返回该场景数据(ProjectDbData)
                2. 多数查询
                    -返回一个元组(存在数据，未存在数据)
        """
        command = "SELECT * from project_data where name=?"
        c = self.conn.cursor()
        # 单个查询
        if isinstance(scene_name, str):
            c.execute(command, (scene_name,))
            data = c.fetchone()
            if not data:
                return
            _id, name, image, description, create_date, modify_date, create_user, enable = data
            data = ProjectDbData(name, image, description, create_date, modify_date, create_user, enable)
            return data
        # 多数查询
        elif isinstance(scene_name, list):
            has_not_list = []
            rt_data = []
            for name in scene_name:
                command = "SELECT * from project_data where name=?"
                c = self.conn.cursor()
                c.execute(command, (name,))
                data = c.fetchone()
                if not data:
                    has_not_list.append(NoExistsData(name))
                    continue
                _id, name, image, description, create_date, modify_date, create_user, enable = data
                data = ProjectDbData(name, image, description, create_date, modify_date, create_user, enable)
                rt_data.append(data)
            return rt_data, has_not_list
        else:
            raise AttributeError("不支持此数据查询")

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

    def close_db(self):
        """
         关闭数据库连接

        :return:
        """
        self.conn.close()

    def __del__(self):
        self.conn.close()
