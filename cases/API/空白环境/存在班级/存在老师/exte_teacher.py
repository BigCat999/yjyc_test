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
        ad_res = web_API.Api_teacher().add_teacher(classlist = classlist, subjectid = 2)
        ad_id = ad_res.json()['id']
        te_res = web_API.Api_teacher().ls_tescher()
        INFO(f'返回结果{te_res.json()}')
        for idlist in te_res.json()['retlist']:
            if idlist['id'] == ad_id:
                CHECK_POINT('存在添加的老师', True)
            else:
                CHECK_POINT('不存在添加的老师', False)

class tc001003():

    name = '添加老师3'

    def teststeps(self):
        classlist = []
        cscl_id = GSTORE['cscl_id']
        dict = {"id":cscl_id}
        classlist.append(dict)
        STEP(1, '添加老师')
        classlist = json.dumps(classlist)
        ad_res = web_API.Api_teacher().add_teacher(classlist = classlist, username = '初始老师')
        INFO(f'返回结果{ad_res.json()}')
        ad_id = ad_res.json()['id']
        te_res = web_API.Api_teacher().ls_tescher()
        CHECK_POINT('登录名 ??? 已经存在', te_res.json()['retlist'])

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

    def setup(self):
        STEP(1,'创建班级class2')
        res = web_API.Api_class().add_class(name='初始班级')
        '添加初始化班级全局变量'
        cscl_tc001051 = res.json()['id']
        INFO(f'old初始班级id:{cscl_tc001051}')
        GSTORE['cscl_tc001051'] = cscl_tc001051

    def teststeps(self):
        classlist = []
        cscl_id = GSTORE['cscl_id']
        cscl_tc001051 = GSTORE['cscl_tc001051']
        dict_class = {"id":cscl_id}
        dict_class2 = {"id":cscl_tc001051}
        classlist.append(dict_class)
        classlist.append(dict_class2)
        STEP(1, '修改老师')
        classlist = json.dumps(classlist)
        te_res = web_API.Api_teacher().moy_teacher(teacherid = 999999, classlist = classlist)
        INFO(f'返回结果{te_res.json()}')
        CHECK_POINT('id 为`999999`的老师不存在', te_res.json()['reason'])

class tc001081():

    name = '删除老师1'

    def teststeps(self):
        STEP(1, '删除老师')
        te_res = web_API.Api_teacher().del_teacher(teacherid = 9999999)
        INFO(f'返回结果{te_res.json()}')
        CHECK_POINT('id 为`9999999`的老师不存在', te_res.json()['reason'])

class tc001082():

    name = '删除老师2'

    def setup(self):
        STEP(1,'创建班级class2')
        res = web_API.Api_class().add_class(name='初始班级')
        '添加初始化班级全局变量'
        cscl_tc001082 = res.json()['id']
        INFO(f'old初始班级id:{cscl_tc001082}')
        GSTORE['cscl_tc001051'] = cscl_tc001082

    def teststeps(self):
        STEP(2, '删除老师')
        teacherid = GSTORE['cscl_tc001051']
        te_res = web_API.Api_teacher().del_teacher(teacherid = teacherid)
        INFO(f'返回结果{te_res.json()}')
        CHECK_POINT('删除老师是否成功', 0 == te_res.json()['retcode'])
        te_res = web_API.Api_teacher().ls_tescher()
        for idlist in te_res.json()['retlist']:
            if idlist['id'] == teacherid:
                CHECK_POINT('删除成功', True)
            else:
                CHECK_POINT('删除失败', False)


