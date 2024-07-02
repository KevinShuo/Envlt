import dataclasses
from importlib import reload
from typing import *
from ..data import database_data
from . import base_db

reload(base_db)


class EnvltAssetDB(base_db.EnvltBaseDB):
    def __init__(self):
        super().__init__()
        self.db_asset_column = ("name", "path", "asset_type", "tab_type", "image", "description", "labels", "enable")

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

    def get_asset_libs_data(self, scene_name: str) -> Optional[List[database_data.AssetDbData]]:
        """
            获取场景里的所有资产数据

        :param scene_name: 要获取场景的场景名
        :return:
        """
        # 获取场景里资产所有数据
        assets = []

        if scene_name == "project_data":
            assets = self.get_all_data_from_table(table_name="project_data",
                                                  insert_dataclass=database_data.ProjectDbData)
        else:
            table_lib_name = f"{scene_name}_libs"
            assets = self.get_all_data_from_table(table_name=table_lib_name,
                                                  insert_dataclass=database_data.AssetDbData)
        return assets

    def insert_data_to_table(self, origin_data: List[database_data.AssetDbData], scene_name: str):
        """
        往表中插入数据

        :param origin_data:从表中获取的数据，类型为list
        :param scene_name:总表中的场景名称
        :return:
        """
        table_name = scene_name + "_libs"
        for asset in origin_data:
            data = dataclasses.astuple(asset)[1:]
            self.insert_table(table_name, table_column=self.db_asset_column, value=data)
