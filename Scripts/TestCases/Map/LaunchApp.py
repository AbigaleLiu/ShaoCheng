from appium import webdriver
import unittest
from Scripts.Mobile import Desired_caps


class LaunchApp(unittest.TestCase):
    def setUp(self):
        self.desired_caps = Desired_caps.Desired_caps().desired_caps()  # 获取设备参数
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=self.desired_caps)

    def test_launch(self):
        self.driver.start_activity(self.desired_caps["appPackage"], self.desired_caps["appActivity"])
        self.failUnless(self.driver.find_element_by_id("com.example.lsx.wcgg:id/tv_start"))


if __name__ == '__main__':
    unittest.main()

