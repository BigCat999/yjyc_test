from lib import web_API
from hytest import *
from time import time, sleep
import json

class tc000002():

    name = '添加班级2'

    def teststeps(self):
        STEP(1, '添加班级')
        ac_res = web_API.Api_class().add_class(name = '测试002')
        INFO(f'接口返回{ac_res.json()}')
        new_id = ac_res.json()['id']
        retcode = ac_res.json()['retcode']
        INFO(f'接口返回{retcode}')
        CHECK_POINT('检查返回值', retcode == 0)
        ls_res = web_API.Api_class().ls_class()
        cl_list = ls_res.json()['retlist']
        number = len(cl_list)
        id = cl_list[number - 1]['id']
        INFO(f'接口返回{id}')
        CHECK_POINT('检查返回结果', id == new_id)

class tc000003():

    name = '添加班级3'

    def teststeps(self):
        STEP(1, '添加相同名称的班级')
        ac_res = web_API.Api_class().add_class(name = '初始班级')
        INFO(f'接口返回{ac_res.json()}')
        reason = ac_res.json()['reason']
        INFO(f'接口返回{reason}')
        CHECK_POINT('检查返回结果', reason == 'duplicated class name')

class tc000051():

    name = '修改班级1'

    def teststeps(self):
        STEP(1, '修改班级名字')
        new_name = '修改名称' + str(time())
        cl_id = GSTORE['cscl_id']
        res_moy = web_API.Api_class().moy_class(calssid = cl_id, name = new_name)
        STEP(2,'查询班级名称')
        res_cl2 = web_API.Api_class().ls_class()
        for i in res_cl2.json()['retlist']:
            if i['id'] == cl_id:
                cl_name = str(i['name'])
        CHECK_POINT('检查返回结果', cl_name == new_name)

class tc000052():

    name = '修改班级2'

    def teststeps(self):
        STEP(1, '创建班级')
        res = web_API.Api_class().add_class(name = tc000052)
        adcl_id = res.json()['id']
        INFO(f'添加班级id:{adcl_id}')
        res_ls = web_API.Api_class().ls_class()
        cscl_id = GSTORE['cscl_id']
        INFO(f'班级列表:{res_ls.json()}')
        INFO(f"班级列表:{res_ls.json()['retlist']}")
        for id in res_ls.json()['retlist']:
            if id['id'] == cscl_id:
                new_name = id['name']
        INFO(f'班级列表:{new_name}')
        res_moy = web_API.Api_class().moy_class(calssid = f'{adcl_id}', name = new_name)
        INFO(f'修改返回结果:{res_moy.json()}')
        reason = res_moy.json()['reason']
        CHECK_POINT('检查返回结果', reason == 'duplicated class name')

class tc000053():

    name = '修改班级3'

    def teststeps(self):
        STEP(1, '修改不存在的班级')
        res_moy= web_API.Api_class().moy_class(calssid = '99999999')
        INFO(f'修改返回结果:{res_moy.json()}')
        reason = res_moy.json()['reason']
        CHECK_POINT('检查返回结果', reason == 'id 为`99999999`的班级不存在')

class tc000081():

    name = '删除班级1'

    def teststeps(self):
        STEP(1, '删除不存在的班级')
        res_de= web_API.Api_class().del_class(calssid = '9999999')
        INFO(f'修改返回结果:{res_de.json()}')
        reason = res_de.json()['reason']
        CHECK_POINT('检查返回结果', reason == 'id 为`9999999`的班级不存在')

class tc000082():

    name = '删除班级2'
    ad_id = ''

    def setup(self):
        STEP(1, '创建班级')
        res_ad = web_API.Api_class().add_class()
        self.ad_id = res_ad.json()['id']

    def teststeps(self):
        STEP(2, '删除班级')
        res_de= web_API.Api_class().del_class(calssid = self.ad_id)
        INFO(f'修改返回结果:{res_de.json()}')
        retcode = res_de.json()['retcode']
        CHECK_POINT('检查返回结果', retcode == 0)
