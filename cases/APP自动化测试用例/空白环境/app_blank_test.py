from appium import webdriver
from hytest import *
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey
from time import time, sleep
from lib.app_public import *
from lib.config import *

class tc006001():

    name = 'vcode登录1'

    def teststeps(self):
        login(configs.url, '123321')
        wd = GSTORE['wd']
        sleep(2)
        tishi = wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout'
                                                '/android '
                                                '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                                '.FrameLayout '
                                                '/android.widget.ScrollView/android.widget.LinearLayout/android.widget'
                                                '.TextView')
        INFO(f'{tishi.text}')
        CHECK_POINT('检查提示', tishi.text == '登录失败 : vcode format error:1')


