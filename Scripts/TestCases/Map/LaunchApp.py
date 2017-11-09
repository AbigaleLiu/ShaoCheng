from appium import webdriver
from Scripts.Mobile import Desired_caps
from appium import webdriver

from Scripts.Mobile import Desired_caps


class LaunchApp():
    def launch_app(self):
        desired_caps = Desired_caps.Desired_caps.desired_caps()  # 获取设备参数
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.start_activity("com.example.lsx.wcgg", ".foo")

    def tearDown(self):
        self.driver.quit()

    def test_add_listings(self):
        self.driver.implicitly_wait(150)