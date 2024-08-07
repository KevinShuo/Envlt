import unittest
from ns_Envlt.envlt import EnvltBase


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # with EnvltDatabase(r"C:\dev\maya\Envlt\database\envlt_db.sqlite") as db:
        #     # db.create_project("python")
        #     d = db.get_project_scene("python")
        #     print(d)
        env = EnvltBase(r"C:\dev\maya\Envlt\database\envlt_db.sqlite")
        a = env.get_project_scene("python")
        print(a)


if __name__ == '__main__':
    unittest.main()
