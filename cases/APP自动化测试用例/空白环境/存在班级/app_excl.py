from appium import webdriver
from hytest import *
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey
from time import time, sleep
from lib.app_public import *
from lib.config import *
from lib import web_API

class tc006201():
    name = '添加老师1'

    def teststeps(self):
        login()
        wd = GSTORE['wd']
        cscl_id = GSTORE['cscl_id']
        sleep(2)
        wd.find_element(AppiumBy.XPATH,
                        '//android.view.ViewGroup[@content-desc="tabnav-teachers"]/android.widget.TextView').click()

        wd.find_element(AppiumBy.ACCESSIBILITY_ID, 'IconAddTeacher').click()
        wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                        '/android.view.ViewGroup[2]/android.widget.EditText').send_keys('app自动化创建老师')
        wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                        '/android.view.ViewGroup[3]/android.widget.EditText').send_keys('applaoshi')
        wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                        '/android.view.ViewGroup[4]/android.widget.EditText').send_keys('1')
        wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                        '/android.view.ViewGroup[5]/android.widget.EditText').send_keys(cscl_id)
        wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                        '/android.widget.FrameLayout/android.widget.FrameLayout/android.view'
                                        '.ViewGroup/android.view.ViewGroup[6]/android.widget.EditText').send_keys('13123234545')
        wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                        '/android.view.ViewGroup[7]/android.widget.EditText').send_keys('98987123@qq.com')
        wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                        '/android.view.ViewGroup[8]/android.widget.EditText').send_keys('152311343456787')
        wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                        '/android.view.ViewGroup[9]/android.widget.TextView').click()
        add_te = wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                        '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                        '/android.widget.ScrollView/android.widget.LinearLayout/android.widget'
                                        '.TextView')

        INFO(f'{add_te.text}')
        CHECK_POINT('检查提示', '添加成功' in add_te.text)
        wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                        '.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView'
                                        '/android.widget.LinearLayout/android.widget.Button').click()
        wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                        '/android.view.ViewGroup[10]/android.widget.TextView').click()
        wd.find_element(AppiumBy.XPATH,
                        '//android.view.ViewGroup[@content-desc="tabnav-teachers"]/android.widget.TextView').click()
        te_name = wd.find_element(AppiumBy.XPATH, '//android.widget.ScrollView['
                                                '@content-desc="detail-teacher-list"]/android.view.ViewGroup/android'
                                                '.view.ViewGroup/android.widget.TextView[2]')
        INFO(f'返回值：{te_name.text}')
        CHECK_POINT('检查提示', te_name.text.strip() == 'app自动化创建老师')
        res = web_API.Api_teacher().ls_tescher()
        te_list = res.json()['retlist']
        INFO(f'返回值：{te_list[0]["realname"]}')
        CHECK_POINT('检查提示', te_list[0]['realname'] == 'app自动化创建老师')
