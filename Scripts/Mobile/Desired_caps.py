import os
import subprocess
from Scripts.GUI.TransportFile import *


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
            if version_Popen.stderr == b'':
                return version_adb[1].decode().split("\r\n")[0]
            else:
                platform_version = version_adb[0].decode().split("\r\n")[0]
                device_name = subprocess.Popen("adb shell getprop ro.serialno",
                                               stdout=subprocess.PIPE).communicate()[0].decode().split("\r\n")[0]
                localpath = os.getcwd()
                # app = localpath.split("Mobile")[0] + "apk\\" + apk_name
                app = TransportFile().hit_me()
                package_name = subprocess.Popen("aapt dump badging "+app,
                                                stdout=subprocess.PIPE).communicate()[0].decode().split("'")[1]
                desired_caps = {
                        'platformName': 'Android',
                        'platformVersion': platform_version,
                        'deviceName': device_name,
                        'app': app,
                        'app-package': package_name,
                    }
                return desired_caps
        except Exception as e:
            return e


if __name__ == '__main__':
    _r = Desired_caps()
    print(_r.desired_caps("shaocheng-lianxiang-v1.0-t2017-11-08.apk"))