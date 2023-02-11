from lib import web_API
from hytest import *
import time

def suite_setup():
    STEP(1, '添加班级')
    res = web_API.Api_class().add_class(name = '初始班级')
    '添加初始化班级全局变量'
    cscl_id = res.json()['id']
    INFO(f'old初始班级id:{cscl_id}')
    GSTORE['cscl_id'] = cscl_id
    print(cscl_id)
