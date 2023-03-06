import random
from random import randint
import requests
import json
from lib.config import configs
import time

class Api_class:

    url = configs.url
    vcode = configs.vcode
    session = requests.Session()

    def printResponse(self,response):
        # print('==========='+str(response.content))
        print('\n\n-------- HTTP response * begin -------')
        print(response.status_code)

        for k, v in response.headers.items():
            print(f'{k}: {v}')
        if response.status_code == 200:
            print('')
            print(json.loads(response.content.decode('utf8')))
            print('-------- HTTP response * end -------\n\n')
        else:
            print('接口未请求成功')

        '''列出班级'''
    def ls_class(self, gradeid = 1 ):

        response = self.session.get(f'{self.url}/api/3school/school_classes?vcode={self.vcode}&action=list_classes_by_schoolgrade&gradeid={gradeid}',
                                   )
        self.printResponse(response)
        return response

        '''添加班级'''
    def add_class(self, name = '班级'+ str(random.randint(0000000, 99999999))):

        # headers = {
        #     'Content-Type': 'application/x-www-form-urlencoded'
        # }
        data = {
            "vcode": f"{self.vcode}",
            "action": "add",
            "grade": "1",
            "name": f"{name}",
            "studentlimit": "100"
        }
        response = self.session.post(f'{self.url}/api/3school/school_classes',
                                     data=data)
        self.printResponse(response)
        return response

        '''修改班级'''
    def moy_class(self, calssid, name = '修改', studentlimit = 100):
        data = {
            "vcode": f"{self.vcode}",
            "action": "modify",
            "name": f"{name}",
            "studentlimit": f"{studentlimit}"
        }
        response = self.session.put(f'{self.url}/api/3school/school_classes/{calssid}',
                                data=data)
        self.printResponse(response)
        return response

        '''删除班级'''
    def del_class(self, calssid=20600):
        data = {
            "vcode": f"{self.vcode}"
        }

        response = self.session.delete(f'{self.url}/api/3school/school_classes/{calssid}',
                                     data=data)
        self.printResponse(response)
        return response


class Api_teacher:

    url = configs.url
    vcode = configs.vcode
    session = requests.Session()

    def printResponse(self, response):
        print('===========' + str(response.content))
        print('\n\n-------- HTTP response * begin -------')
        print(response.status_code)

        for k, v in response.headers.items():
            print(f'{k}: {v}')
        if response.status_code == 200:
            print('')
            print(json.loads(response.content.decode('utf8')))
            print('-------- HTTP response * end -------\n\n')
        else:
            print('接口未请求成功')

        '''列出老师'''
    def ls_tescher(self, subjectid = ''):

        response = self.session.get(
            f'{self.url}/api/3school/teachers?vcode={self.vcode}&action=search_with_pagenation&subjectid={subjectid}',
            )
        self.printResponse(response)
        return response

        '''添加老师'''
    def add_teacher(self, username = '登录'+ str(int(time.time())), classlist = '[{"id":20524}]', subjectid = 12):
        phonenumber = '132' + str(random.randint(00000000, 99999999))
        data = {
            "vcode": f"{self.vcode}",
            "action": "add",
            "username": f"{username}",
            "realname": "测试老师",
            "subjectid": f"{subjectid}",
            "classlist": classlist,
            "phonenumber": phonenumber,
            "email": "ceshi@16553.com",
            "idcardnumber": "111111155"

        }
        response = self.session.post(f'{self.url}/api/3school/teachers',
                                    data=data)
        self.printResponse(response)
        return response

        '''修改老师'''
    def moy_teacher(self, teacherid=5214, classlist = '[{"id":20247}]', subjectid = 1):

        data = {
            "vcode": f"{self.vcode}",
            "action": "modify",
            "username": "ceshi",
            "realname": "测试老师9",
            "subjectid": subjectid,
            "classlist": classlist,
            "phonenumber": "13212123434",
            "email": "ceshi@163.com",
            "idcardnumber": "11111111"

        }
        response = self.session.put(f'{self.url}/api/3school/teachers/{teacherid}',
                                     data=data)
        self.printResponse(response)
        return response

        '''删除老师'''
    def del_teacher(self, teacherid=5214):

        data = {
            "vcode": f"{self.vcode}"
        }

        response = self.session.delete(f'{self.url}/api/3school/teachers/{teacherid}',
                                       data=data)
        self.printResponse(response)
        return response
'''学生操作'''
class Api_students:

    url = configs.url
    vcode = configs.vcode
    session = requests.Session()

    def printResponse(self, response):
        print('===========' + str(response.content))
        print('\n\n-------- HTTP response * begin -------')
        print(response.status_code)

        for k, v in response.headers.items():
            print(f'{k}: {v}')
        if response.status_code == 200:
            print('')
            print(json.loads(response.content.decode('utf8')))
            print('-------- HTTP response * end -------\n\n')
        else:
            print('接口未请求成功')

        '''列出学生'''
    def ls_students(self):

        response = self.session.get(
            f'{self.url}/api/3school/students?vcode={self.vcode}&action=search_with_pagenation',
            )
        self.printResponse(response)
        return response

        '''添加学生'''
    def add_students(self, username = '测试学生', classid = 20247, gradeid = 1, realname = '测试学生'):

        phonenumber = '132' + ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 8))
        data = {
            "vcode": f"{self.vcode}",
            "action": "add",
            "username": username,
            "realname": realname,
            "gradeid": gradeid,
            "classid": classid,
            "phonenumber": phonenumber

        }

        response = self.session.post(f'{self.url}/api/3school/students',
                                    data=data)
        self.printResponse(response)
        return response

        '''修改学生'''
    def moy_students(self, studentid=2122):

        data = {
            "vcode": f"{self.vcode}",
            "action": "modify",
            "realname": "5测试学生",
            "phonenumber": "15512123434"

        }
        response = self.session.put(f'{self.url}/api/3school/students/{studentid}',
                                     data=data)
        self.printResponse(response)
        return response

        '''删除学生'''
    def del_students(self, studentid=2122):

        data = {
            "vcode": f"{self.vcode}"
        }

        response = self.session.delete(f'{self.url}/api/3school/students/{studentid}',
                                       data=data)
        self.printResponse(response)
        return response

# list = [0,1,2,3,4,5,6,7,8,9]
# print(type(list))
# a1 = "-"
# seq = ["a", "b", "c"]
# print (a1.join( seq ))
# a = ''.join(random.sample(['0','1','2','3','4','5','6','7','8','9'], 8))
# print('132'+ a)
# print(''.join(a))
# print('132'+str(random.sample([0,1,2,3,4,5,6,7,8,9], 8)))
# print(a)
