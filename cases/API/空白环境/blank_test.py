from lib import web_API
from hytest import *
from time import sleep

class tc000001():

    name = '添加班级1'

    def teststeps(self):
        STEP(1, '添加班级')
        ac_res = web_API.Api_class().add_class(name = '测试001')
        new_id = ac_res.json()['id']
        retcode = ac_res.json()['retcode']
        INFO(f'接口返回{retcode}')
        CHECK_POINT('检查返回值', retcode == 0)
        ls_res = web_API.Api_class().ls_class()
        cl_list = ls_res.json()['retlist']
        number = len(cl_list)
        id = cl_list[number - 1]['id']
        INFO(f'接口返回{id}')
        CHECK_POINT('检查返回值', id == new_id)

