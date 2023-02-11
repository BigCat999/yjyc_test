from lib import web_API
from hytest import *
from time import time, sleep
import json

class tc002001():

    name = '添加学生2'

    def teststeps(self):
        classid = GSTORE['cscl_id']
        STEP(1, '添加学生')
        ad_res = web_API.Api_students().add_students(classid = classid, username='tc002001')
        INFO(f'返回结果{ad_res.json()}')
        ad_id = ad_res.json()['id']
        te_res = web_API.Api_students().ls_students()
        INFO(f'返回结果{te_res.json()}')
        for idlist in te_res.json()['retlist']:
            if idlist['id'] == ad_id:
                check = True
                break
            else:
                check = False
        CHECK_POINT('是否添加成功', check)

class tc002081():

    name = '删除学生1'
    de_id = None

    def setup(self):
        classid = GSTORE['cscl_id']
        STEP(1, '添加学生')
        ad_res = web_API.Api_students().add_students(classid = classid, username='tc002081')
        self.de_id = ad_res.json()['id']

    def teststeps(self):
        STEP(2, '删除学生')
        ad_res = web_API.Api_students().del_students(studentid = self.de_id )
        te_res = web_API.Api_students().ls_students()
        INFO(f'返回结果{te_res.json()}')
        for idlist in te_res.json()['retlist']:
            if idlist['id'] == self.de_id:
                check = False
                break
            else:
                check = True
        CHECK_POINT('是否删除成功', check)