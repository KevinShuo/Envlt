# -*- coding: utf-8 -*-
# @Time : 2024/8/7 下午1:07
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : envlt.py
# @Project : Envlt
from ns_Envlt import database, project, scene
from typing import *


class EnvltBase:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def new_project(self, project_name: str) -> project.Project:
        with database.EnvltDatabase(self.db_path) as db:
            db.create_project(project_name)
        return project.Project(project_name, self.db_path)

    def get_projects(self) -> Tuple[project.Project, ...]:
        with database.EnvltDatabase(self.db_path) as db:
            projects = tuple([project.Project(i, self.db_path) for i in db.list_projects()])
        return projects

    def get_project_scene(self, project_name: str) -> Optional[Tuple[scene.Scene, ...]]:
        with database.EnvltDatabase(self.db_path) as db:
            scene_datas = db.get_project_scene(project_name)
        return tuple([scene.Scene(name) for name in scene_datas if name])

    def delete_project(self, project_name):
        pass
