# -*- coding: utf-8 -*-
# @Time : 2024/6/28 下午1:23
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : log_error.py
# @Project : Envlt

class LogFileNameError(Exception):
    """
        日志文件名错误
    """
    pass


class HasNotLogsPath(Exception):
    """
        日志农场没有获取任何的数据
    """
    pass


class LogFilePathIsNotExists(Exception):
    """
        日志文件不存在
    """
    pass
