from lib import web_API
from hytest import *
from time import time, sleep
import json

class tc001009():

    name = '添加老师2'

    def teststeps(self):
        classlist = []
        cscl_id = GSTORE['cscl_id']
        dict = {"id":cscl_id}
        classlist.append(dict)
        STEP(1, '添加老师')
        classlist = json.dumps(classlist)
        ad_res = web_API.Api_teacher().add_teacher(classlist = classlist, username = 'tc001009', subjectid = 11)
        INFO(f'接口返回{ad_res.json()}')
        ad_id = ad_res.json()['id']
        te_res = web_API.Api_teacher().ls_tescher()
        INFO(f'返回结果{te_res.json()}')
        for idlist in te_res.json()['retlist']:
            INFO(idlist['id'])
            if idlist['id'] == ad_id:
                check = True
                break
            else:
                check = False
        CHECK_POINT('是否添加成功', check)




class tc001003():

    name = '添加老师3'

    def teststeps(self):
        classlist = []
        cscl_id = GSTORE['cscl_id']
        dict = {"id":cscl_id}
        classlist.append(dict)
        STEP(1, '添加老师')
        classlist = json.dumps(classlist)
        ad_res = web_API.Api_teacher().add_teacher(classlist = classlist, username = '初始老师', subjectid = 12)
        INFO(f'返回结果{ad_res.json()}')
        reason = ad_res.json()['reason']
        CHECK_POINT('登录名 初始老师 已经存在', ad_res.json()['reason'])

class tc001051():

    name = '修改老师1'

    def teststeps(self):
        classlist = []
        cscl_id = GSTORE['cscl_id']
        dict = {"id":cscl_id}
        classlist.append(dict)
        STEP(1, '修改老师')
        classlist = json.dumps(classlist)
        te_res = web_API.Api_teacher().moy_teacher(teacherid = 999999, classlist = classlist)
        INFO(f'返回结果{te_res.json()}')
        CHECK_POINT(' id 为`999999`的老师不存在', te_res.json()['reason'])


class tc001002():

    name = '修改老师2'
    addcl_id = None

    def setup(self):
        STEP(1,'创建班级class2')
        res = web_API.Api_class().add_class()
        INFO(f'接口返回{res.json()}')
        self.addcl_id = res.json()['id']

    def teststeps(self):
        classlist = []
        cscl_id = GSTORE['cscl_id']
        cste_id = GSTORE['cste_id']
        dict_class = {"id":cscl_id}
        dict_class2 = {"id":self.addcl_id}
        classlist.append(dict_class)
        classlist.append(dict_class2)
        STEP(1, '修改老师')
        classlist = json.dumps(classlist)
        te_res = web_API.Api_teacher().moy_teacher(teacherid = cste_id, classlist = classlist, subjectid = 13)
        INFO(f'返回结果{te_res.json()}')
        CHECK_POINT('检查返回结果', te_res.json()['retcode'] == 0)

class tc001081():

    name = '删除老师1'

    def teststeps(self):
        STEP(1, '删除老师')
        te_res = web_API.Api_teacher().del_teacher(teacherid = 9999999)
        INFO(f'返回结果{te_res.json()}')
        CHECK_POINT('id 为`9999999`的老师不存在', te_res.json()['reason'])

class tc001082():

    name = '删除老师2'
    dete_id = None

    def setup(self):
        classlist = []
        cscl_id = GSTORE['cscl_id']
        dict = {"id":cscl_id}
        classlist.append(dict)
        STEP(1, '添加老师')
        classlist = json.dumps(classlist)
        ad_res = web_API.Api_teacher().add_teacher(classlist = classlist, username = 'tc001082', subjectid = 5)
        INFO(f'返回结果{ad_res.json()}')
        self.dete_id = ad_res.json()['id']

    def teststeps(self):
        STEP(2, '删除老师')
        te_res = web_API.Api_teacher().del_teacher(teacherid = self.dete_id)
        INFO(f'返回结果{te_res.json()}')
        CHECK_POINT('删除老师是否成功', 0 == te_res.json()['retcode'])
        te_res = web_API.Api_teacher().ls_tescher()
        for idlist in te_res.json()['retlist']:
            if idlist['id'] == self.dete_id:
                CHECK_POINT('删除失败', False)
            else:
                CHECK_POINT('删除成功', True)


