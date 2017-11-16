import unittest
import HTMLTestRunner
from Scripts.Public.Path import *
from Scripts.Public.TimeTemp import *
from Scripts.TestSuites.TestSuites import *


class Html:
    def file_name(self):
        dir = Path().report_dir()
        file_name = dir + "\\" + TimeTemp().time_temp() + ".html"
        return file_name

    def html(self):
        file = open(self.file_name(), "wb")
        suites = TestSuites().test_suites()
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=file,
            title='本周测试报告',
            # description='This demonstrates the report output by HTMLTestRunner.'
        )

        runner.run(suites)
        file.close()


if __name__ == '__main__':
    Html().html()
