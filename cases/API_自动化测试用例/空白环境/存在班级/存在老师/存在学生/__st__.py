from lib import web_API
from hytest import *
import json

def suite_setup():
    classid = GSTORE['cscl_id']
    STEP(1, '添加学生')
    ad_res = web_API.Api_students().add_students(classid=classid, username='初始学生', realname='初始学生')
    INFO(f'返回结果{ad_res.json()}')
    st_id = ad_res.json()['id']
    GSTORE['st_id'] = st_id

