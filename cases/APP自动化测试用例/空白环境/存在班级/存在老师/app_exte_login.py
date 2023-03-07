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
        banji = wd.find_element(AppiumBy.ID, 'no-class-warning')
        INFO(f'{banji.text}')
        CHECK_POINT('检查提示', banji.text == '该学校还没有班级，点击刷新')
        wd.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="tabnav-teachers"]/android.widget.TextView').click()
        laoshi = wd.find_element(AppiumBy.ID, 'no-teacher-warning')
        INFO(f'{laoshi.text}')
        CHECK_POINT('检查提示', laoshi.text == '该学校还没有老师，点击刷新')

class tc006002():

    name = 'vcode登录2'

    def teststeps(self):
        login()
        wd = GSTORE['wd']
        sleep(2)
        wd.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="tabnav-teachers"]/android.widget.TextView').click()
        banji = wd.find_element(AppiumBy.ID, 'no-class-warning')
        INFO(f'{banji.text}')
        CHECK_POINT('检查提示', banji.text == '该学校还没有班级，点击刷新')
        laoshi = wd.find_element(AppiumBy.ID, 'no-teacher-warning')
        INFO(f'{laoshi.text}')
        CHECK_POINT('检查提示', laoshi.text == '该学校还没有老师，点击刷新')

class tc006003():

    name = 'vcode登录3'

    def teststeps(self):
        login()
        wd = GSTORE['wd']
        sleep(2)
        wd.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="tabnav-teachers"]/android.widget.TextView').click()
        banji = wd.find_element(AppiumBy.ID, 'no-class-warning')
        INFO(f'{banji.text}')
        CHECK_POINT('检查提示', banji.text == '该学校还没有班级，点击刷新')
        laoshi = wd.find_element(AppiumBy.ID, 'no-teacher-warning')
        INFO(f'{laoshi.text}')
        CHECK_POINT('检查提示', laoshi.text == '该学校还没有老师，点击刷新')



