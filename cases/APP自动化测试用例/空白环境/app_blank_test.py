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

class tc006002():

    name = 'vcode登录2'

    def teststeps(self):
        login()
        wd = GSTORE['wd']
        sleep(2)
        banji = wd.find_element(AppiumBy.ID, 'no-class-warning')
        INFO(f'{banji.text}')
        CHECK_POINT('检查提示', banji.text == '该学校还没有班级，点击刷新')
        wd.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="tabnav-teachers"]/android.widget.TextView').click()
        laoshi = wd.find_element(AppiumBy.ID, 'no-teacher-warning')
        INFO(f'{laoshi.text}')
        CHECK_POINT('检查提示', laoshi.text == '该学校还没有老师，点击刷新')

class tc006101():

    name = '添加班级1'

    def teststeps(self):
        login()
        wd = GSTORE['wd']
        sleep(2)
        wd.find_element(AppiumBy.ID, 'IconAddClass').click()
        wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                     '.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android'
                                     '.view.ViewGroup[2]/android.widget.EditText').send_keys('app自动化创建班级')
        wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                        '/android.view.ViewGroup[3]/android.widget.EditText').send_keys('1')
        wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                        '/android.view.ViewGroup[4]/android.widget.EditText').send_keys('100')
        wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                        '/android.view.ViewGroup[5]/android.widget.TextView').click()

        INFO(f'{banji.text}')
        CHECK_POINT('检查提示', banji.text == '该学校还没有班级，点击刷新')
        wd.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="tabnav-teachers"]/android.widget.TextView').click()
        laoshi = wd.find_element(AppiumBy.ID, 'no-teacher-warning')
        INFO(f'{laoshi.text}')
        CHECK_POINT('检查提示', laoshi.text == '该学校还没有老师，点击刷新')



