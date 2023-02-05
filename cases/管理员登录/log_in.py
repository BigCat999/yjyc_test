from hytest import *
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
from lib import ui_public


class UI_010X:

    tags = ['登录功能']
    ddt_cases = [
        {
            'name': '登录 - UI-0001',
            'para': [ '', '888888', '请输入用户名']
        },
        {
            'name': '登录 - UI-0002',
            'para': ['byhy', '', '请输入密码']
        },
        {
            'name': '登录 - UI-0003',
            'para': ['byh', '888888', '登录失败 : 用户名或者密码错误']
        },
        {
            'name': '登录 - UI-0004',
            'para': ['byhy', '8888888', '登录失败 : 用户名或者密码错误']
        },
        {
            'name': '登录 - UI-0005',
            'para': ['byhy', '8888888', '登录失败 : 用户名或者密码错误']
        }
    ]

    def teststeps(self):
        STEP(1, '打开浏览器')
        public.open_browser()
        wd = GSTORE['wd']
        username, password, info = self.para
        STEP(2, '登录')
        wd.get('http://127.0.0.1:8087/mgr/sign.html')
        wd.find_element(By.CSS_SELECTOR, '#username').send_keys(username)
        wd.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        wd.find_element(By.CSS_SELECTOR, 'button[type = "submit"]').click()
        sleep(2)
        notify = wd.switch_to.alert.text
        CHECK_POINT('弹出提示', notify == info )
        wd.quit()

        # STEP(3, '查看菜单')
        # CHECK_POINT('检查菜单是否正确', True)
