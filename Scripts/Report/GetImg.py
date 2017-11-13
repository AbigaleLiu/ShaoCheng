import os
from appium import webdriver
from Scripts.Public.TimeTemp import *

class GetImg:
    def img_name(self):
        img_name = TimeTemp().time_temp() + ".jpg"
        return img_name
    def get_img(self):
        img_name = self.img_name()
