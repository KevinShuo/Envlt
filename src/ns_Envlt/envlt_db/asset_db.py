from typing import *
from ..data import database_data
from .base_db import EnvltBaseDB


class EnvltAssetDB(EnvltBaseDB):
    def __init__(self):
        super().__init__()

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
