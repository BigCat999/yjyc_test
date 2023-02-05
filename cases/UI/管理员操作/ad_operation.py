from hytest import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

import lib.ui_public
from lib import ui_public

def suite_setup():
    INFO('suite_setup')
    STEP(1, '打开浏览器')
    sleep(1)
    public.open_browser()
    STEP(2, '登录')
    public.login()

def suite_teardown():
    INFO('suite_teardown')
    sleep(1)
    wd = GSTORE['wd']
    wd.quit()

class UI_0101:

    name = '登录'

    def teststeps(self):
        # STEP(1, '打开浏览器')
        # public.open_browser()
        wd = GSTORE['wd']
        # STEP(2, '登录')
        # public.login()
        STEP(3, '登录')
        sleep(2)
        title = wd.title
        INFO(f'title = {title}')
        elements = wd.find_elements(By.XPATH, '//ul[@class="sidebar-menu tree"]//li//span')
        element_text = [i.text for i in elements]
        INFO(f'菜单列表{element_text}')
        CHECK_POINT('检查前三个菜单', element_text[:3] == ['客户','药品', '订单'])

class UI_0102:

    name = '添加用户'

    def teststeps(self):
        wd = GSTORE['wd']
        STEP(3, '创建用户')
        wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-md').click()
        wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div .form-control').send_keys('南京中医院')
        wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div:nth-child(2) .form-control').send_keys('15311149787')
        wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div:nth-child(3) .form-control').send_keys('南京')
        wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-xs').click()
        sleep(2)
        elements = wd.find_elements(By.CSS_SELECTOR, '.content.container-fluid div:nth-child(3) div[class="search-result-item-field"] span:nth-child(2)')
        elements_text = [ i.text for i in elements]
        INFO(f'创建信息 {elements_text}')
        CHECK_POINT('检查是否创建成功', elements_text == ['南京中医院', '15311149787', '南京'])
        STEP(4, '删除用户')
        wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[3]/div[4]/div/label[2]').click()
        sleep(1)
        wd.switch_to.alert.accept()


class UI_0103:

    name = '编辑用户'

    def teststeps(self):
        wd = GSTORE['wd']
        sleep(2)
        STEP(3, '创建用户')
        wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-md').click()
        wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div .form-control').send_keys('南京中医院')
        wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div:nth-child(2) .form-control').send_keys('15311149787')
        wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div:nth-child(3) .form-control').send_keys('南京')
        wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-xs').click()
        sleep(2)
        wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[3]/div[4]/div/label[1]').click()
        wd.find_element(By.CSS_SELECTOR, '.content.container-fluid div:nth-child(3) div input').clear()
        wd.find_element(By.CSS_SELECTOR, '.content.container-fluid div:nth-child(3) div input').send_keys('南京省中医院')
        wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[3]/div[2]/div/label[1]').click()
        sleep(2)
        elements = wd.find_elements(By.CSS_SELECTOR, '.content.container-fluid div:nth-child(3) div[class="search-result-item-field"] span:nth-child(2)')
        elements_text = [ i.text for i in elements]
        INFO(f'编辑信息 {elements_text}')
        CHECK_POINT('检查是否编辑成功', elements_text == ['南京省中医院', '15311149787', '南京'])
        STEP(4, '删除用户')
        wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[3]/div[4]/div/label[2]').click()
        sleep(1)
        wd.switch_to.alert.accept()

class UI_0105:

    name = '添加药品'


    def teststeps(self):
        wd = GSTORE['wd']
        sleep(2)
        STEP(3, '添加药品')
        wd.find_element(By.CSS_SELECTOR, '.fa.fa-plus').click()
        wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-md').click()
        wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div .form-control').send_keys('诺氟沙星')
        wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div:nth-child(2) .form-control').send_keys('SKD098')
        wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div:nth-child(3) .form-control').send_keys('治疗肠胃炎')
        wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-xs').click()
        sleep(2)
        elements = wd.find_elements(By.CSS_SELECTOR, '.content.container-fluid div:nth-child(3) div[class="search-result-item-field"] span:nth-child(2)')
        elements_text = [ i.text for i in elements]
        INFO(f'创建信息 {elements_text}')
        CHECK_POINT('检查是否创建成功', elements_text == ['诺氟沙星', 'SKD098', '治疗肠胃炎'])
        STEP(4, '删除药品')
        wd.find_element(By.XPATH, '//*[@id="root"]/div/section[2]/div[3]/div[4]/div/label[2]').click()
        sleep(1)
        wd.switch_to.alert.accept()

class UI_0106:

    name = '页面跳转'

    def teststeps(self):
        wd = GSTORE['wd']
        wd.maximize_window()
        sleep(2)
        STEP(3, '跳转到教学网站')
        wd.find_element(By.CSS_SELECTOR, '.pull-right.hidden-xs').click()
        wh = wd.current_window_handle # 获取当前的窗口句柄
        windows = wd.window_handles  # 获取打开的多个窗口句柄
        wd.switch_to.window(windows[-1])  # 切换到当前最新打开的窗口
        sleep(2)
        elements = wd.find_elements(By.CSS_SELECTOR, '.navbar-nav.d-md-inline-flex li span')
        elements_txt = [ i.text for i in elements]
        INFO(f'创建信息 {elements_txt}')
        CHECK_POINT('检查是否创建成功', elements_txt == ['Python基础', 'Python进阶', 'Qt图形界面','Django', '自动化测试', '性能测试','HTML/CSS', 'JS语言', 'JS Web'])
        wd.switch_to.window(wh)
        wd.find_element(By.CSS_SELECTOR, '.hidden-xs').click()
        wd.find_element(By.CSS_SELECTOR, '.user-footer div:nth-child(2) a').click()
        sleep(2)
        url = wd.current_url
        INFO(f'页面url：{url}')
        CHECK_POINT('检查是否返回登录页', url =='http://127.0.0.1:8087/mgr/sign.html')

class UI_0107:

    name = '添加订单'
    y_name = ['青霉素盒装1', '青霉素盒装2', '青霉素盒装3']
    bianhao = ['YP-32342341', 'YP-32342342', 'YP-32342343']
    miaoshu = ['青霉素注射液，每支15ml，20支装', '青霉素注射液，每支15ml，30支装', '青霉素注射液，每支15ml，40支装']

    k_name = ['南京中医院1', '南京中医院2', '南京中医院3']
    phone = ['2551867851', '2551867852', '2551867853']
    dizhi = ['江苏省-南京市-秦淮区-汉中路-501', '江苏省-南京市-秦淮区-汉中路-502', '江苏省-南京市-秦淮区-汉中路-503']

    def setup(self):
        INFO('suite_setup')
        STEP(1, '打开浏览器')
        sleep(1)
        public.open_browser()
        STEP(2, '登录')
        public.login()

    def teardown(self):
        INFO('suite_teardown')
        sleep(1)
        wd = GSTORE['wd']
        wd.quit()

    def teststeps(self):
        wd = GSTORE['wd']
        sleep(2)
        STEP(3, '添加药品')
        wd.find_element(By.CSS_SELECTOR, '.fa.fa-plus').click()
        wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-md').click()
        for i in range(3):
            wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div .form-control').send_keys(self.y_name[i])
            wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div:nth-child(2) .form-control').send_keys(self.bianhao[i])
            wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div:nth-child(3) .form-control').send_keys(self.miaoshu[i])
            wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-xs').click()
        sleep(2)
        wd.find_element(By.CSS_SELECTOR, '.fa.fa-user').click()
        wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-md').click()
        sleep(2)
        STEP(4, '添加客户')
        for i in range(3):
            wd.find_element(By.CSS_SELECTOR, '.fa.fa-user').click()
            wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-md').click()
            wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div .form-control').send_keys(self.k_name[i])
            wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div:nth-child(2) .form-control').send_keys(self.phone[i])
            wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div:nth-child(3) .form-control').send_keys(self.dizhi[i])
            wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-xs').click()
        STEP(5, '添加订单')
        wd.find_element(By.CSS_SELECTOR, '.fa.fa-paperclip').click()
        wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-md').click()
        wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div .form-control').send_keys('客户订单')
        #创建Select对象
        select_1 = Select(wd.find_element(By.CSS_SELECTOR, ".col-lg-8.col-md-8.col-sm-8 div:nth-child(2) .xxx"))
        # 选择小雷老师 和 小凯老师
        select_1.select_by_visible_text("南京中医院2")
        sleep(2)

        select_2 = Select(wd.find_element(By.CSS_SELECTOR, ".col-lg-8.col-md-8.col-sm-8 div:nth-child(3) .xxx"))
        select_2.select_by_visible_text("青霉素盒装1")
        sleep(2)

        wd.find_element(By.CSS_SELECTOR, 'div[style = "margin-top: 0.2em;"] input').send_keys('100')
        sleep(2)
        wd.find_element(By.CSS_SELECTOR, '.col-lg-12.col-md-12.col-sm-12 .btn.btn-green.btn-outlined.btn-xs').click()
        sleep(2)
        element = wd.find_element(By.CSS_SELECTOR,
                                    '.content.container-fluid div:nth-child(3) div[class="search-result-item-field"] span:nth-child(2)').text
        INFO(f'创建订单信息 {element}')
        CHECK_POINT('检查是否创建成功', element == '客户订单')

class UI_0108:

    name = '删除订单'
    y_name = ['青霉素盒装1', '青霉素盒装2', '青霉素盒装3']
    bianhao = ['YP-32342341', 'YP-32342342', 'YP-32342343']
    miaoshu = ['青霉素注射液，每支15ml，20支装', '青霉素注射液，每支15ml，30支装', '青霉素注射液，每支15ml，40支装']

    k_name = ['南京中医院1', '南京中医院2', '南京中医院3']
    phone = ['2551867851', '2551867852', '2551867853']
    dizhi = ['江苏省-南京市-秦淮区-汉中路-501', '江苏省-南京市-秦淮区-汉中路-502', '江苏省-南京市-秦淮区-汉中路-503']

    # 初始化方法,删除所有订单/药品/用户
    def setup(self):
        INFO('suite_setup')
        STEP(1, '打开浏览器')
        sleep(1)
        public.open_browser()
        STEP(2, '登录')
        public.login()
        wd = GSTORE['wd']
        wd.find_element(By.CSS_SELECTOR, '.fa.fa-paperclip').click()
        sleep(2)
        while True == True:
            sleep(1)
            try:
                element = wd.find_element(By.CSS_SELECTOR,
                                          '.search-result-item .search-result-item-actionbar [type = "button"]').click()
                wd.switch_to.alert.accept()
                sleep(2)
            except:
                break
        wd.find_element(By.CSS_SELECTOR, '.fa.fa-user').click()
        while True == True:
            sleep(1)
            try:
                element = wd.find_element(By.CSS_SELECTOR,
                                          '.search-result-item .search-result-item-actionbar [type = "button"]:nth-child(2)').click()
                wd.switch_to.alert.accept()
                sleep(2)
            except:
                break
        wd.find_element(By.CSS_SELECTOR, '.fa.fa-plus').click()
        while True == True:
            sleep(1)
            try:
                element = wd.find_element(By.CSS_SELECTOR,
                                          '.search-result-item .search-result-item-actionbar [type = "button"]:nth-child(2)').click()
                wd.switch_to.alert.accept()
                sleep(2)
            except:
                break

    def teststeps(self):

        wd = GSTORE['wd']
        sleep(2)
        STEP(3, '添加药品')
        wd.find_element(By.CSS_SELECTOR, '.fa.fa-plus').click()
        wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-md').click()
        for i in range(3):
            wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div .form-control').send_keys(self.y_name[i])
            wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div:nth-child(2) .form-control').send_keys(self.bianhao[i])
            wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div:nth-child(3) .form-control').send_keys(self.miaoshu[i])
            wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-xs').click()
        sleep(2)
        wd.find_element(By.CSS_SELECTOR, '.fa.fa-user').click()
        wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-md').click()
        sleep(2)
        STEP(4, '添加客户')
        for i in range(3):
            wd.find_element(By.CSS_SELECTOR, '.fa.fa-user').click()
            wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-md').click()
            wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div .form-control').send_keys(self.k_name[i])
            wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div:nth-child(2) .form-control').send_keys(self.phone[i])
            wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div:nth-child(3) .form-control').send_keys(self.dizhi[i])
            wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-xs').click()
        STEP(5, '添加订单')
        wd.find_element(By.CSS_SELECTOR, '.fa.fa-paperclip').click()
        wd.find_element(By.CSS_SELECTOR, '.btn.btn-green.btn-outlined.btn-md').click()
        wd.find_element(By.CSS_SELECTOR, '.col-lg-8 div .form-control').send_keys('客户订单')
        #创建Select对象
        select_1 = Select(wd.find_element(By.CSS_SELECTOR, ".col-lg-8.col-md-8.col-sm-8 div:nth-child(2) .xxx"))
        # 选择小雷老师 和 小凯老师
        select_1.select_by_visible_text("南京中医院2")
        sleep(2)

        select_2 = Select(wd.find_element(By.CSS_SELECTOR, ".col-lg-8.col-md-8.col-sm-8 div:nth-child(3) .xxx"))
        select_2.select_by_visible_text("青霉素盒装1")
        sleep(2)

        wd.find_element(By.CSS_SELECTOR, 'div[style = "margin-top: 0.2em;"] input').send_keys('100')
        sleep(2)
        wd.find_element(By.CSS_SELECTOR, '.col-lg-12.col-md-12.col-sm-12 .btn.btn-green.btn-outlined.btn-xs').click()
        sleep(2)
        element = wd.find_element(By.CSS_SELECTOR,
                                    '.content.container-fluid div:nth-child(3) div[class="search-result-item-field"] span:nth-child(2)').text
        INFO(f'创建订单信息 {element}')
        CHECK_POINT('检查是否创建成功', element == '客户订单')










