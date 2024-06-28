import unittest
from ns_Envlt.envlt_log import log_factory


class MyTestCase(unittest.TestCase):
    a = log_factory.LogFactory("unit_test2", True)

    def test_write_log(self):
        self.a.write_log(log_level=log_factory.LogLevel.INFO, content="my_test")

    def test_list_all_logs(self):
        all_path = self.a.list_all_logs_path(False)
        print(f"All :{all_path}")
        limit_path = self.a.list_logs_path(False, 1)
        print(f"Limit: {limit_path}")

    def test_read_line_content(self):
        limit_path = self.a.list_all_logs_path(False)
        f = log_factory.LogFileFactory(self.a)
        print(f.read_line_content())


if __name__ == '__main__':
    unittest.main()
