from lib import web_API
from hytest import *
import json

def suite_setup():
    classlist = []
    cscl_id = GSTORE['cscl_id']
    dict = {"id": cscl_id}
    classlist.append(dict)
    STEP(1, '添加老师')
    classlist = json.dumps(classlist)
    ad_res = web_API.Api_teacher().add_teacher(classlist=classlist, username = '初始老师', subjectid = 1 )
    INFO(f'请求结果{ad_res.json()}')
    INFO(f"请求结果{ad_res.json()['id']}")
    GSTORE['cste_id'] = ad_res.json()['id']
