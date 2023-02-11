from lib import web_API
from hytest import *
from time import time, sleep
import json

class tc001001():

    name = '添加老师1'

    def teststeps(self):
        classlist = []
        cscl_id = GSTORE['cscl_id']
        dict = {"id":cscl_id}
        classlist.append(dict)
        STEP(1, '添加老师')
        classlist = json.dumps(classlist)
        ad_res = web_API.Api_teacher().add_teacher(classlist = classlist)
        INFO(f'返回结果{ad_res.json()}')
        ad_id = ad_res.json()['id']
        te_res = web_API.Api_teacher().ls_tescher()
        for idlist in te_res.json()['retlist']:
            if idlist['id'] == ad_id:
                CHECK_POINT('存在添加的老师', True)
            else:
                CHECK_POINT('不存在添加的老师', False)
