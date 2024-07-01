# -*- coding: utf-8 -*-
# @Time : 2024/6/28 11:53
# @Author : Mr.wang
# @Email : 204062518@qq.com
# @File : log_factory.py
# @Project : Envlt

import os
import re
import getpass
from enum import Enum
from ns_Envlt.envlt_log import envlt_log
from importlib import reload
from ns_Envlt.error import log_error
from ns_Envlt.utils import os_util

reload(log_error)


class LogLevel(Enum):
    INFO = 0
    WARN = 1
    ERROR = 2
    SUCCESS = 3
    CRITICAL = 4
    DEBUG = 5


class LogFactory:
    """
     操作日志类
    """

    def __init__(self, log_name: str, user_dir: bool):
        """
            初始化一个日志农场

        :param log_name: 日志文件名
        """
        self._log_dir_path = None
        self._logs_path_list = []
        self.log_level = LogLevel
        if not check_log_file_name(log_name):
            raise log_error.LogFileNameError("日志文件名错误,请不要带后缀")
        if user_dir:
            self.log_user_dir_path = os.path.join(self.log_dir_path, getpass.getuser()).replace('\\', '/')
            if not os.path.exists(self.log_user_dir_path):
                os.makedirs(self.log_user_dir_path)
            self.env_log = envlt_log.EnvLog(self.log_user_dir_path, log_name)
        else:
            self.env_log = envlt_log.EnvLog(self.log_dir_path, log_name)

    def write_log(self, log_level: LogLevel, content: str):
        """
            写一行日志

        :param log_level:日志等级
        :param content: 日志内容
        :return:
        """
        self.env_log.write_log(log_level.name, content)

    def list_all_logs_path(self, user: bool):
        """
            获取当前插件下所有的日志文件路径
        :param user:是否开启用户目录
        :return: 日志文件路径
        """
        log_file_path = envlt_log.EnvLog.list_log(self.log_user_dir_path if user else self.log_dir_path)
        logs_path = os_util.correct_path(log_file_path)
        self.logs_path_list = logs_path
        return logs_path

    def list_logs_path(self, user: bool, limit: int = 1):
        """
            列举指定数量的日志文件路径
        :param user:是否开启用户目录
        :param limit: 日志数量
        :return:
        """
        log_file_path = envlt_log.EnvLog.list_log(self.log_user_dir_path if user else self.log_dir_path, limit)
        logs_path = os_util.correct_path(log_file_path)
        self.logs_path_list = logs_path
        return logs_path

    @property
    def log_dir_path(self):
        """
        日志目录路径
        :return:
        """
        self._log_dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                          "logs").replace('\\', '/')
        if not os.path.exists(self._log_dir_path):
            os.makedirs(self._log_dir_path)
        return self._log_dir_path

    @log_dir_path.setter
    def log_dir_path(self, value: str):
        self._log_dir_path = value

    @property
    def logs_path_list(self):
        return self._logs_path_list

    @logs_path_list.setter
    def logs_path_list(self, value: list):
        self._logs_path_list = value

    @property
    def info(self):
        return self.log_level.INFO

    @property
    def warn(self):
        return self.log_level.WARN

    @property
    def error(self):
        return self.log_level.ERROR

    @property
    def success(self):
        return self.log_level.SUCCESS

    @property
    def critical(self):
        return self.log_level.CRITICAL

    @property
    def debug(self):
        return self.log_level.DEBUG


class LogFileFactory:
    def __init__(self, log_factory: LogFactory):
        self.log_factory = log_factory
        if not self.log_factory.logs_path_list:
            raise log_error.HasNotLogsPath("日志农场没有获取任何数据")

    def read_line_content(self, read_line: int = 1000000):
        """
            读取指定行
        :param read_line:
        :return:
        """
        log_content_dict = []
        for log_path in self.log_factory.logs_path_list:
            if not os.path.exists(log_path):
                raise log_error.LogFilePathIsNotExists("日志文件不存在")
            log_file_name = os.path.split(log_path)[-1]
            with open(log_path, "r+", encoding="utf-8") as log_file:
                log_lines = log_file.readlines()[::-1]
                if len(log_lines) <= read_line:
                    log_content_dict.append({"name": log_file_name, "data": log_lines})
                else:
                    log_content_dict.append({"name": log_file_name, "data": log_lines[:read_line + 1]})
        return log_content_dict


def check_log_file_name(file_name: str) -> bool:
    """
        检查日志文件名是否符合规范

    :param file_name: 文件名
    :return:
    """
    if re.match(r".*?\.log", file_name):
        return False
    return True
