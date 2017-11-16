import os
import subprocess
from Scripts.GUI.TransportFile import *
from Scripts.Public.Path import *


class Desired_caps:
    """
    自动获取启动appium所需的desired_caps
    """
    def desired_caps(self):
        try:
            version_Popen = subprocess.Popen("adb shell getprop ro.build.version.release",
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
            version_adb = version_Popen.communicate()
            if version_adb[1] == b'':
                platform_version = version_adb[0].decode().split("\r\r")[0]
                device_name = subprocess.Popen("adb shell getprop ro.serialno",
                                               stdout=subprocess.PIPE).communicate()[0].decode().split("\r\r")[0]
                app = Path().apk_path()
                badging = subprocess.Popen("aapt dump badging " + app,
                                                stdout=subprocess.PIPE).communicate()[0].decode()
                package_name = badging.split("'")[1]
                app_activity = badging.split("launchable-activity: name=")[1].split("\'")[1]
                desired_caps = {
                    'platformName': 'Android',
                    'platformVersion': platform_version,
                    'deviceName': device_name,
                    'appPackage': package_name,
                    'appActivity': app_activity
                }
                return desired_caps
            else:
                print(version_adb[1].decode().split("\r\n")[0])
        except Exception as e:
            print(e)


if __name__ == '__main__':
    _r = Desired_caps()
    print(_r.desired_caps())