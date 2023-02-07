from lib import web_API
from hytest import *
from time import time, sleep
import json

class tc002001():

    name = '添加学生2'

    def teststeps(self):
        classid = GSTORE['cscl_id']
        STEP(1, '添加学生')
        ad_res = web_API.Api_students().add_students(classid = classid)
        ad_id = ad_res.json()['id']
        te_res = web_API.Api_students().ls_students()
        INFO(f'返回结果{te_res.json()}')
        for idlist in te_res.json()['retlist']:
            if idlist['id'] == ad_id:
                CHECK_POINT('添加成功', True)
            else:
                CHECK_POINT('添加失败', False)

class tc002081():

    name = '删除学生1'
    de_id = None

    def setup(self):
        classid = GSTORE['cscl_id']
        STEP(1, '添加学生')
        ad_res = web_API.Api_students().add_students(classid = classid)
        self.de_id = ad_res.json()['id']

    def teststeps(self):
        STEP(2, '删除学生')
        ad_res = web_API.Api_students().del_students(studentid = self.de_id )
        te_res = web_API.Api_students().ls_students()
        INFO(f'返回结果{te_res.json()}')
        for idlist in te_res.json()['retlist']:
            if idlist['id'] == self.de_id:
                CHECK_POINT('删除失败', True)
            else:
                CHECK_POINT('删除成功', False)