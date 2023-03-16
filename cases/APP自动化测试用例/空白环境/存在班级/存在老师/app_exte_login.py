from appium import webdriver
from hytest import *
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey
from time import time, sleep
from lib.app_public import *
from lib.config import *


class tc006003():
    name = 'vcode登录3'

    def teststeps(self):
        login()
        wd = GSTORE['wd']
        sleep(2)
        banji = wd.find_element(AppiumBy.XPATH, '//android.widget.ScrollView['
                                                '@content-desc="detail-class-list"]/android.view.ViewGroup/android.view'
                                                '.ViewGroup/android.widget.TextView[2]')
        INFO(f'返回值：{banji.text}')
        CHECK_POINT('检查提示', banji.text.strip() == '七年级 : 初始班级')
        wd.find_element(AppiumBy.XPATH,
                        '//android.view.ViewGroup[@content-desc="tabnav-teachers"]/android.widget.TextView').click()
        laoshi = wd.find_element(AppiumBy.XPATH, '//android.widget.ScrollView['
                                                 '@content-desc="detail-teacher-list"]/android.view.ViewGroup/android'
                                                 '.view.ViewGroup/android.widget.TextView[2]')
        INFO(f'{laoshi.text}')
        CHECK_POINT('检查提示', laoshi.text.strip() == '测试老师')
