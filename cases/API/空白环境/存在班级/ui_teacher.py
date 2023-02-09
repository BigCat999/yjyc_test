from hytest import *
from time import time, sleep
from lib.ui_public import *
from lib.web_API import *

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
        dict = {"id": cscl_id}
        classlist.append(dict)
        Api_teacher().add_teacher(username = 'tc005001', classlist = classlist)
        STEP(2,'登录账号')






