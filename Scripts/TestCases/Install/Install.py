import subprocess
from appium import webdriver
from Scripts.Public.Path import *

class Install:
    def intall(self):
        apk = Path().apk_path()
        command = "adb install " + apk
        install_popen = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return install_popen


if __name__ == '__main__':
    Install().intall()