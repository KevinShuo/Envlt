# -*- coding: utf-8 -*-
import dataclasses
from importlib import reload
from typing import *

from ns_Envlt.data import database_data
from ns_Envlt.error import database_error
from . import base_db

reload(database_error)
reload(database_data)
reload(base_db)


class EnvltProjectDatabase(base_db.EnvltBaseDB):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(EnvltProjectDatabase, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
            单例模式，控制场景总表数据
        """
        super().__init__()
        self.db_master_column = ("name", "image", "description", "create_date", "modify_date", "create_user", "enable")

    def create_new_scene(self, project_data: database_data.ProjectDbData):
        """
            创建一个新的场景

        Args:
            project_data:项目数据

        Returns:

        """

        rt_data = self.get_global_scene_data(scene_name=project_data.scene_name)
        if rt_data:
            raise database_error.SceneExistsError("场景已存在")
        insert_data = dataclasses.astuple(project_data)[1:]
        self.insert_table(table_name="project_data", table_column=self.db_master_column, value=insert_data)

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
            data = database_data.ProjectDbData(*data)
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
                data = database_data.ProjectDbData(*data)
                rt_data.append(data)
            return rt_data, has_not_list
        else:
            raise AttributeError("不支持此数据查询")

    def delete_data_from_project_data(self, scene_name: str):
        """
        从总表中删除场景的索引信息
        :param scene_name: 场景名
        :return:
        """
        command = f"""DELETE FROM project_data WHERE name = ?"""
        c = self.conn.cursor()
        c.execute(command, (scene_name,))
        self.conn.commit()
