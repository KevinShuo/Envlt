import sqlite3
import os


class EnvltBaseDB:
    def __init__(self):
        self.conn = sqlite3.connect(self.db_path)

    def drop_table(self, scene_name: str):
        """
        删除场景表格
        :param scene_name:场景名
        :return:
        """
        table_name = scene_name + "_libs"
        command = f"""DROP TABLE IF EXISTS {table_name}"""
        c = self.conn.cursor()
        c.execute(command)
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