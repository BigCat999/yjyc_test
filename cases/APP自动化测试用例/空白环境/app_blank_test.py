from appium import webdriver
from hytest import *
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey
from time import time, sleep
from lib.app_public import *
from lib.config import *
from lib import web_API

class tc006001():

    name = 'vcode登录1'

    def teststeps(self):
        login(configs.url, '123321')
        wd = GSTORE['wd']
        sleep(2)
        tishi = wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout'
                                                '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                                '.widget.FrameLayout/android.widget.ScrollView/android.widget'
                                                '.LinearLayout/android.widget.TextView')
        INFO(f'{tishi.text}')
        CHECK_POINT('检查提示', tishi.text == '登录失败 : vcode format error:1')

class tc006002():

    name = 'vcode登录2'

    def teststeps(self):
        login()
        wd = GSTORE['wd']
        sleep(2)
        banji = wd.find_element(AppiumBy.ACCESSIBILITY_ID, 'no-class-warning')
        INFO(f'{banji.text}')
        CHECK_POINT('检查提示', banji.text == '该学校还没有班级，点击刷新')
        wd.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="tabnav-teachers"]/android.widget.TextView').click()
        laoshi = wd.find_element(AppiumBy.ACCESSIBILITY_ID, 'no-teacher-warning')
        INFO(f'{laoshi.text}')
        CHECK_POINT('检查提示', laoshi.text == '该学校还没有老师，点击刷新')

class tc006101():

    name = '添加班级1'

    def teststeps(self):
        login()
        wd = GSTORE['wd']
        sleep(2)
        wd.find_element(AppiumBy.ACCESSIBILITY_ID, 'IconAddClass').click()
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
        addcl = wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout'
                                             '/android.widget.TextView')

        INFO(f'{addcl.text}')
        CHECK_POINT('检查提示', '添加成功' in addcl.text)
        wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                        '.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView'
                                        '/android.widget.LinearLayout/android.widget.Button').click()
        banji = wd.find_element(AppiumBy.XPATH, '//android.widget.ScrollView['
                                                '@content-desc="detail-class-list"]/android.view.ViewGroup/android.view'
                                                '.ViewGroup/android.widget.TextView[2]')
        INFO(f'返回值：{banji.text}')
        CHECK_POINT('检查提示', banji.text.strip() == '七年级 : app自动化创建班级')
        res = web_API.Api_class().ls_class()
        cl_list = res.json()['retlist']
        INFO(f'返回值：{cl_list[0]["name"]}')
        CHECK_POINT('检查提示', cl_list[0]['name'] == 'app自动化创建班级')



