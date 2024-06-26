# -*- coding: utf-8 -*-
# @Time : 2024/6/26 15:19
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : database_error.py
# @Project : Envlt

class SceneExistsError(Exception):
    """
        场景已存在错误
    """
    pass


class SceneNoExistsError(Exception):
    """
        场景已存在错误
    """
    pass
