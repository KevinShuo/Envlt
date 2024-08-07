# -*- coding: utf-8 -*-
# @Time : 2024/8/7 下午4:21
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : scene_data.py
# @Project : Envlt
import dataclasses

from .image_data import ImageData


@dataclasses.dataclass
class SceneData:
    id: int
    name: str
    description: str
    image: ImageData
    create_user: str
    modify_user: str
    create_date: str
    modify_date: str
    status: str
