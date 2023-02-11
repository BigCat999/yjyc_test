from lib import web_API
from hytest import *


def suite_setup():
    INFO('suite_setup')
    STEP(1, '清空所有学生/老师/班级')
    '''删除所有学生'''
    st_res = web_API.Api_students().ls_students()
    print(f'查询学生ls_students(){st_res.json()}')
    for idlist in st_res.json()['retlist']:
        print(idlist['id'])
        response =web_API.Api_students().del_students(idlist['id'])
    '''删除所有老师'''
    te_res = web_API.Api_teacher().ls_tescher()
    for idlist in te_res.json()['retlist']:
        print(idlist['id'])
        response =web_API.Api_teacher().del_teacher(idlist['id'])
    '''删除所有班级'''
    cl_res = web_API.Api_class().ls_class()
    for idlist in cl_res.json()['retlist']:
        print(idlist['id'])
        response =web_API.Api_class().del_class(idlist['id'])
