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
        el_text = wd.find_elements(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]/span')
        sleep(3)
        el_list = [i.text for i in el_text]
        INFO(f'列表{el_list}')
        for st_name in el_list:
            INFO(f'名字{st_name}')
            if st_name == '初始学生':
                check = True
                break
            else:
                check = False
        CHECK_POINT('检查学生姓名', check)

class tc005101():

    name = '老师发布作业1'

    def setup(self):
        STEP(1, '创建试题')
        wd = GSTORE['wd']
        login('初始老师', '888888', '/teacher/login/login.html')
        sleep(3)
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[3]/a').click()
        sleep(3)
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[3]/ul/a[3]/li/span').click()
        sleep(3)
        wd.find_element(By.XPATH, '//*[@id="nav_item_add"]/a').click()
        sleep(3)
        wd.find_element(By.XPATH, '//*[@id="dropdown_textbookversions"]/li[1]/a').click()
        sleep(3)
        wd.find_element(By.XPATH, '//*[@id="btn_group_grades_1"]/label[1]').click()
        sleep(3)
        wd.find_element(By.XPATH, '//*[@id="btn_group_textbookvols_1"]/label[1]').click()
        sleep(3)
        iframe = wd.find_element(By.XPATH, '//*[@id="tbody_question_body"]/tr[2]/td[2]/div/div[2]/iframe')
        wd.switch_to.frame(iframe)
        wd.find_element(By.XPATH, '/html/body').send_keys('测试题目')
        sleep(3)
        wd.switch_to.parent_frame()
        wd.find_element(By.XPATH, '//*[@id="question_answers"]/label[4]/strong').click()
        sleep(3)
        wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
        sleep(3)
        wd.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div/div/button[1]').click()
        sleep(3)
        for i in range(2):
            iframe = wd.find_element(By.XPATH, '//*[@id="tbody_question_body"]/tr[2]/td[2]/div/div[2]/iframe')
            wd.switch_to.frame(iframe)
            wd.find_element(By.XPATH, '/html/body').send_keys('测试题目')
            sleep(3)
            wd.switch_to.parent_frame()
            wd.find_element(By.XPATH, '//*[@id="question_answers"]/label[4]/strong').click()
            sleep(3)
            wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
            sleep(3)
            wd.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div/div/button[1]').click()
        exit()

        # wd.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div/div/button[3]').click()

    def teststeps(self):
        wd = GSTORE['wd']
        STEP(2,'登录账号')
        login('初始老师', '888888', '/teacher/login/login.html')
        sleep(2)
        wd.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[2]/a').click()
        sleep(2)
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[2]/li/span').click()
        sleep(2)
        wd.find_element(By.XPATH, '//*[@id="exam_name_text"]').send_keys('测试作业')
        sleep(2)
        wd.find_element(By.XPATH, '//*[@id="btn_pick_question"]').click()
        sleep(2)
        elements = wd.find_elements(By.XPATH, '//*[@id="serach_result_table"]/div/div[3]/div/label[2]')
        sleep(2)
        for el in elements[:3]:
            el.click()
        sleep(2)
        wd.find_element(By.XPATH, '//*[@id="cart_footer"]/div[4]/div[2]').click()
        sleep(2)
        wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()




