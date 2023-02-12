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

    def teststeps(self):
        wd = GSTORE['wd']
        STEP(1,'登录老师账号发布作业')
        login('初始老师', '888888', '/teacher/login/login.html')
        sleep(1)
        wd.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[2]/a').click()
        sleep(1)
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[2]/li/span').click()
        sleep(1)
        wd.find_element(By.XPATH, '//*[@id="exam_name_text"]').send_keys('测试作业')
        sleep(1)
        wd.find_element(By.XPATH, '//*[@id="btn_pick_question"]').click()
        wd.switch_to.frame('pick_questions_frame')
        # wd.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div[3]/div/div/button').click()
        sleep(1)
        elements = wd.find_elements(By.XPATH, '//*[@id="serach_result_table"]/div/div[3]/div/label[2]')
        sleep(1)
        for el in elements[:3]:
            el.click()
        sleep(1)
        wd.find_element(By.XPATH, '//*[@id="cart_footer"]/div[4]/div[2]').click()
        sleep(1)
        wd.switch_to.parent_frame()
        wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
        sleep(1)
        wd.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div/div/button[2]').click()
        sleep(1)
        a = wd.current_window_handle  # 获得当前窗口句柄
        INFO(f'窗口句柄{a}')
        windows = wd.window_handles  # 获取打开的多个窗口句柄
        INFO(f'窗口句柄{windows}')
        INFO(f'当前窗口句柄{windows[-1]}')
        wd.switch_to.window(windows[-1])  # 切换到当前最新打开的窗口
        wd.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div[3]/div/table/tbody/tr/td/div/label/span').click()
        sleep(2)
        wd.find_element(By.XPATH, '/html/body/div/div[2]/h3/button').click()
        sleep(2)
        wd.find_element(By.XPATH, '//*[@id="modal-dispatch"]/div[2]/div/div[3]/button[2]').click()
        sleep(2)
        # wd.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div/div/button').click()
        STEP(2,'登录学生账号完成作业')
        sleep(3)
        login('初始学生', '888888', '/student/login/login.html')
        sleep(3)
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div[2]/ul/li[1]/a/i').click()
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div[2]/ul/li[1]/ul/li[3]/a').click()
        wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div[2]/div/table/tbody/tr/td[7]/button').click()
        sleep(2)
        elements = wd.find_elements(By.XPATH, '//*[@id="exam_question_list_choice"]/div/div/div/div[2]/div/div/button[4]')
        for element in elements:
            element.click()
        sleep(2)
        wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div[1]/div[3]/button').click()
        sleep(2)
        wd.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[3]/div/div/button[2]').click()
        sleep(2)
        wd.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div/div[6]/div[1]/div[2]/div/img').click()
        sleep(2)
        stelements = wd.find_elements(By.XPATH, '//*[@id="exam_question_list_choice"]/div/div/div/img')
        stel_list = [el.get_attribute("ng-if") for el in stelements]
        INFO(f'{stel_list}')
        sleep(2)
        login('初始老师', '888888', '/teacher/login/login.html')
        wd.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div[2]/a/h2/i').click()
        wd.find_element(By.XPATH, '//*[@id="dynamicView"]/div[2]/div/table/tbody/tr/td[5]/a/i').click()
        wd.find_element(By.XPATH, '//*[@id="collapse_1"]/div/div[2]/div[2]/table/tbody/tr/td[4]/button').click()
        sleep(2)
        a = wd.current_window_handle  # 获得当前窗口句柄
        INFO(f'窗口句柄{a}')
        windows = wd.window_handles  # 获取打开的多个窗口句柄
        INFO(f'窗口句柄{windows}')
        INFO(f'当前窗口句柄{windows[-1]}')
        wd.switch_to.window(windows[-1])  # 切换到当前最新打开的窗口
        sleep(2)
        teelements = wd.find_elements(By.XPATH, '//*[@id="exam_question_list_choice"]/div/div/div/img')
        teel_list = [el.get_attribute("ng-if") for el in teelements]
        CHECK_POINT('对比作业完成情况', teel_list == stel_list)

class tc005102():

    name = '老师发布作业2'

    def teststeps(self):
        wd = GSTORE['wd']
        STEP(1,'登录老师账号发布作业')
        login('初始老师', '888888', '/teacher/login/login.html')
        sleep(1)
        wd.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[2]/a').click()
        sleep(1)
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[2]/li/span').click()
        sleep(1)
        # wd.find_element(By.XPATH, '//*[@id="exam_name_text"]').send_keys('')
        sleep(1)
        wd.find_element(By.XPATH, '//*[@id="btn_pick_question"]').click()
        wd.switch_to.frame('pick_questions_frame')
        # wd.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div[3]/div/div/button').click()
        sleep(1)
        elements = wd.find_elements(By.XPATH, '//*[@id="serach_result_table"]/div/div[3]/div/label[2]')
        sleep(1)
        for el in elements[:3]:
            el.click()
        sleep(1)
        wd.find_element(By.XPATH, '//*[@id="cart_footer"]/div[4]/div[2]').click()
        sleep(1)
        wd.switch_to.parent_frame()
        wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
        sleep(2)
        el_text = wd.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div').text
        INFO(f'{el_text}')
        CHECK_POINT('检查提示语', el_text == '请输入作业名称')

class tc005103():

    name = '老师发布作业3'

    def teststeps(self):
        wd = GSTORE['wd']
        STEP(1,'登录老师账号发布作业')
        login('初始老师', '888888', '/teacher/login/login.html')
        sleep(1)
        wd.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[2]/a').click()
        sleep(1)
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[2]/li/span').click()
        sleep(1)
        wd.find_element(By.XPATH, '//*[@id="exam_name_text"]').send_keys('a')
        sleep(1)
        wd.find_element(By.XPATH, '//*[@id="btn_pick_question"]').click()
        wd.switch_to.frame('pick_questions_frame')
        # wd.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div[3]/div/div/button').click()
        sleep(1)
        elements = wd.find_elements(By.XPATH, '//*[@id="serach_result_table"]/div/div[3]/div/label[2]')
        sleep(1)
        for el in elements[:3]:
            el.click()
        sleep(1)
        wd.find_element(By.XPATH, '//*[@id="cart_footer"]/div[4]/div[2]').click()
        sleep(1)
        wd.switch_to.parent_frame()
        wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
        sleep(2)
        wd.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div[1]/button').click()
        sleep(2)
        wd.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[2]/a').click()
        sleep(2)
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[3]/li/span').click()
        el_text = wd.find_element(By.XPATH, '//*[@id="serach_result_table"]/div[1]/div[1]').text
        INFO(f'{el_text}')
        CHECK_POINT('检查创建作业名称', el_text == 'a')

class tc005104():

    name = '老师发布作业4'

    def teststeps(self):
        wd = GSTORE['wd']
        STEP(1,'登录老师账号发布作业')
        login('初始老师', '888888', '/teacher/login/login.html')
        sleep(1)
        wd.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[2]/a').click()
        sleep(1)
        na = ''
        for i in range(90):
            na = na + '1'
        INFO(f'{na}')
        name = '测试*（）asdzz'+na
        INFO(f'{name}')
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[2]/li/span').click()
        sleep(1)
        wd.find_element(By.XPATH, '//*[@id="exam_name_text"]').send_keys(name)
        sleep(1)
        wd.find_element(By.XPATH, '//*[@id="btn_pick_question"]').click()
        wd.switch_to.frame('pick_questions_frame')
        # wd.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div[3]/div/div/button').click()
        sleep(1)
        elements = wd.find_elements(By.XPATH, '//*[@id="serach_result_table"]/div/div[3]/div/label[2]')
        sleep(1)
        for el in elements[:3]:
            el.click()
        sleep(1)
        wd.find_element(By.XPATH, '//*[@id="cart_footer"]/div[4]/div[2]').click()
        sleep(1)
        wd.switch_to.parent_frame()
        wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
        sleep(2)
        wd.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div[1]/button').click()
        sleep(2)
        wd.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[2]/a').click()
        sleep(2)
        wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[2]/ul/a[3]/li/span').click()
        el_text = wd.find_element(By.XPATH, '//*[@id="serach_result_table"]/div[1]/div[1]').text
        INFO(f'页面文本{el_text}')
        INFO(f'实际文本{name}')

        CHECK_POINT('检查创建作业名称', el_text == name)







