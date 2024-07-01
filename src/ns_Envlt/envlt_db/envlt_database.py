# -*- coding: utf-8 -*-
# @Time : 2024/6/24 14:30
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : envlt_database.py
# @Project : Envlt
from importlib import reload
import os
import sqlite3
from typing import *
from ns_Envlt.error import database_error
from ns_Envlt.data import database_data

reload(database_error)
reload(database_data)



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

    def create_new_scene(self, project_data: database_data.ProjectDbData):
        """
            创建一个新的场景

        Args:
            project_data:项目数据

        Returns:

        """
        command = f"""INSERT INTO project_data (name, image, description, create_date, modify_date, create_user, enable)
values (?, ?, ?, ?, ?, ?, ?)"""
        c = self.conn.cursor()
        rt_data = self.get_global_scene_data(scene_name=project_data.scene_name)
        if rt_data:
            raise database_error.SceneExistsError("场景已存在")
        c.execute(command, (
            project_data.scene_name, project_data.image_path, project_data.description, project_data.create_date,
            project_data.modify_date, project_data.create_user, project_data.enable))
        self.conn.commit()

    def create_new_asset_table(self, scene_name: str):
        """
            创建一个新的场景资产表

        :param scene_name: 场景名字
        :return:
        """
        command = f"""create table {scene_name}_libs
(
    id          integer not null
        constraint test_lib_pk
            primary key autoincrement,
    name        TEXT    not null,
    path        TEXT    not null,
    asset_type  TEXT,
    tab_type    TEXT    not null,
    image       TEXT    not null,
    description TEXT,
    labels      TEXT,
    enable      TEXT    not null
);
"""
        index_command = f"""create index {scene_name}_libs_name_index
    on {scene_name}_libs (name);"""
        c = self.conn.cursor()
        c.execute(command)
        c.execute(index_command)
        self.conn.commit()

    def get_all_scene_name(self) -> Optional[List[str]]:
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

    def get_global_scene_data(self, scene_name: Union[str, List[str]]) -> Optional[
        Union[database_data.ProjectDbData, List[database_data.ProjectDbData], Tuple[
            List[database_data.ProjectDbData], List[database_data.NoExistsData]]]]:
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
            data = database_data.ProjectDbData(name, image, description, create_date, modify_date, create_user, enable)
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
                    has_not_list.append(database_data.NoExistsData(name))
                    continue
                _id, name, image, description, create_date, modify_date, create_user, enable = data
                data = database_data.ProjectDbData(name, image, description, create_date, modify_date, create_user,
                                                   enable)
                rt_data.append(data)
            return rt_data, has_not_list
        else:
            raise AttributeError("不支持此数据查询")

    def get_asset_libs_data(self, scene_name: str) -> Optional[List[database_data.AssetDbData]]:
        """
            获取场景里的所有资产数据

        :param scene_name: 要获取场景的场景名
        :return:
        """
        # 获取场景里资产所有数据
        assets = []
        if "project_data" in scene_name:
            command_get_asset_lib = f"""SELECT * FROM {scene_name}"""
            c = self.conn.cursor()
            c.execute(command_get_asset_lib)
            datas = c.fetchall()
            if not datas:
                return
            for data in datas:
                _id, name, image, description, creat_date, modify_date, creat_user, enable = data
                asset_data = database_data.ProjectDbData(name, image, description, creat_date, modify_date, creat_user,
                                                         enable)
                assets.append(asset_data)
        else:
            command_get_asset_lib = f"""SELECT * FROM {scene_name}_libs"""
            c = self.conn.cursor()
            c.execute(command_get_asset_lib)
            datas = c.fetchall()
            if not datas:
                return
            for data in datas:
                _id, name, path, asset_type, tab_type, image, description, labels, enable = data
                asset_data = database_data.AssetDbData(_id, name, path, asset_type, tab_type, image, description,
                                                       labels,
                                                       enable)
                assets.append(asset_data)
        return assets

    def insert_data_to_table(self, origin_data: List[database_data.AssetDbData], scene_name: str):
        """
        往表中插入数据
        :param origin_data:从表中获取的数据，类型为list
        :param scene_name:总表中的场景名称
        :return:
        """
        table_name = scene_name + "_libs"
        command = f"""INSERT INTO {table_name} (name, path, asset_type, tab_type, image, description, labels, enable)
        values (?, ?, ?, ?, ?, ?, ?,?)"""
        # print(command)
        for asset in origin_data:
            data = (
                asset.name,
                asset.path,
                asset.asset_type,
                asset.tab_type,
                asset.image,
                asset.description,
                asset.labels,
                asset.enable
            )
            c = self.conn.cursor()
            c.execute(command, data)
        self.conn.commit()

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
