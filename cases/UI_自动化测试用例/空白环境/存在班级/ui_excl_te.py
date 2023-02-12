from hytest import *
from time import time, sleep
from lib.ui_public import *
from lib.web_API import *
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

def suite_setup():
    STEP(1, '获取浏览器对象')
    open_browser()

def suite_teardown():
    INFO('关闭浏览器')
    wd = GSTORE['wd']
    wd.quit()

class tc005001():

    name = '老师登录1'

    def setup(self):
        STEP(1,'创建老师')
        classlist = []
        cscl_id = GSTORE['cscl_id']
        dict = {"id":cscl_id}
        classlist.append(dict)
        STEP(1, '添加老师')
        classlist = json.dumps(classlist)
        res = Api_teacher().add_teacher(username = 'tc005001', classlist = classlist)
        INFO(f'返回结果{res.json()}')

    def teststeps(self):
        wd = GSTORE['wd']
        STEP(2,'登录账号')
        login('tc005001', '888888', '/teacher/login/login.html')
        sleep(2)
        el_texts = wd.find_elements(By.XPATH, '//table[@class="table table-striped table-hover"]//tbody//tr//td[2]/a')
        sleep(2)
        el_list = [i.text for i in el_texts]
        INFO(f'列表{el_list[:3]}')
        CHECK_POINT('检查页面元素', el_list[:3] == ['白月学院00002', '测试老师', '初中体育'])


class tc005081():

    name = '学生登录1'

    def setup(self):
        STEP(1,'创建学生')
        cscl_id = GSTORE['cscl_id']
        res = Api_students().add_students(username = 'tc005081', classid = cscl_id, realname = 'tc005081' )
        INFO(f'返回结果{res.json()}')
        print(res.json())

    def teardown (self):
        STEP(1,'删除创建学生')
        st_res = Api_students().ls_students()
        for idlist in st_res.json()['retlist']:
            Api_students().del_students(idlist['id'])

    def teststeps(self):
        wd = GSTORE['wd']
        STEP(2,'登录学生账号')
        login('tc005081', '888888', '/student/login/login.html')
        sleep(2)
        el_texts = wd.find_elements(By.XPATH, '//*[@id="div-home"]/div/div/div[1]/table/tbody/tr/td[2]/span')
        sleep(2)
        el_list = [i.text for i in el_texts]
        INFO(f'列表{el_list[:2]}')
        CHECK_POINT('检查页面元素', el_list[:2] == ['tc005081', '白月学院00002'])





