import os
from Scripts.Public.TimeTemp import *

class Path:
    def apk_path(self):
        """
        获取apk文件名（绝对路径）
        获取截图保存路径
        获取日志保存路径
        :return:
        """
        apk_name = "shaocheng-lianxiang-v1.0-t2017-11-08.apk"
        localpath = os.getcwd()
        app = localpath.split("\\Scripts")[0] + "\\Scripts\\apk\\" + apk_name
        return app

    def img_path(self):
        localpath = os.getcwd()
        img_path = localpath.split("\\Scripts")[0] + "\\Scripts\\Report\\IMGs\\" + TimeTemp().time_temp()
        return img_path

    def log_path(self):
        localpath = os.getcwd()
        log_path = localpath.split("\\Scripts")[0] + "\\Scripts\\Report\\Logs\\" + TimeTemp().time_temp()
        return log_path

    def report_dir(self):
        localpath = os.getcwd()
        report = localpath.split("\\Scripts")[0] + "\\Scripts\\Report"
        return report

if __name__ == '__main__':
    _path = Path()
    print(_path.apk_path())
    print(_path.img_path())
