from hytest import *
from time import time, sleep
from lib.ui_public import *
from lib.web_API import *
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def suite_setup():
    STEP(1, '获取浏览器对象')
    open_browser()

def suite_teardown():
    INFO('关闭浏览器')
    wd = GSTORE['wd']
    wd.quit()

class tc005002():

    name = '老师登录2'

    def teststeps(self):
        wd = GSTORE['wd']
        STEP(2,'登录账号')
        login('初始老师', '888888', '/teacher/login/login.html')
        sleep(2)
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[4]/a').click()
        sleep(2)
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[4]/ul/a[2]/li/span').click()
        sleep(3)
        wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/div/div[1]/a').click()
        sleep(3)
        el_text = wd.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]/span').text
        sleep(3)
        INFO(f'学生姓名{el_text}')
        sleep(2)
        CHECK_POINT('检查学生姓名', el_text == '初始学生')

        # el_list = [i.text for i in el_texts]
        # INFO(f'列表{el_list[:3]}')
        # CHECK_POINT('检查页面元素', el_list[:3] == ['白月学院00002', '测试老师', '初中数学'])

# tc005001().setup()





