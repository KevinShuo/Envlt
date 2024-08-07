# -*- coding: utf-8 -*-
# @Time : 2024/8/7 下午3:35
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : database.py
# @Project : Envlt
import sqlite3
from typing import *
from ns_Envlt.dataclass import scene_data

project_name = NewType("project_name", str)


class EnvltDatabase:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def create_project(self, project_name: str):
        """
            创建一个项目

        :param project_name:
        :return:
        """
        command = f"""create table {project_name}
(
    id          integer not null
        constraint {project_name}_pk
            primary key autoincrement
        constraint {project_name}_pk_2
            unique,
    name        TEXT    not null,
    description TEXT,
    image       TEXT,
    create_user TEXT,
    modify_user TEXT,
    create_date TEXT,
    modify_date TEXT,
    status      TEXT
);"""
        self.conn.execute(command)
        self.conn.commit()

    def list_projects(self) -> Tuple[project_name, ...]:
        command = f"""SELECT *
FROM sqlite_master
WHERE type = 'table'
  and name != 'sqlite_sequence'"""
        c = self.conn.cursor()
        c.execute(command)
        datas = c.fetchall()
        return tuple([project_name(i[1]) for i in datas])

    def get_project_scene(self, project_name: str) -> Optional[Tuple[scene_data.SceneData, ...]]:
        command = f"""SELECT * FROM {project_name}"""
        c = self.conn.cursor()
        c.execute(command)
        datas = c.fetchall()
        if not datas:
            return
        return tuple([scene_data.SceneData(*d) for d in datas])
