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
        # print('11121111111313'+res)
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
        CHECK_POINT('检查页面元素', el_list[:3] == ['白月学院00002', '测试老师', '初中数学'])

# tc005001().setup()





