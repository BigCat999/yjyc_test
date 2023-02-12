from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from hytest import *
from lib.config import configs
from time import time, sleep
'''获取浏览器对象'''
def open_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(10)
    GSTORE['wd'] = wd

'''登录用户'''
def login(username, password, path):
    url = configs.url
    wd = GSTORE['wd']
    wd.get(f'{url}{path}')
    wd.find_element(By.CSS_SELECTOR, '#username').send_keys(username)
    wd.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
    wd.find_element(By.CSS_SELECTOR, 'button[id = "submit"]').click()

'''退出用户'''
def exit():
    wd = GSTORE['wd']
    wd.find_element(By.XPATH, '//*[@id="topbar"]/div/ul[2]/li/a/span[1]').click()
    wd.find_element(By.XPATH, '//*[@id="topbar"]/div/ul[2]/li/ul/li[4]/a/i').click()

'''创建试题'''
def cr_ques(number, username, password, path):
    STEP(1, '创建试题')
    wd = GSTORE['wd']
    login(username, password, path)
    sleep(1)
    wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[3]/a').click()
    sleep(1)
    wd.find_element(By.XPATH, '//*[@id="topbar"]/div/div/ul/li[3]/ul/a[3]/li/span').click()
    sleep(1)
    wd.find_element(By.XPATH, '//*[@id="nav_item_add"]/a').click()
    sleep(1)
    wd.find_element(By.XPATH, '//*[@id="dropdown_textbookversions"]/li[1]/a').click()
    sleep(1)
    wd.find_element(By.XPATH, '//*[@id="btn_group_grades_1"]/label[1]').click()
    sleep(1)
    wd.find_element(By.XPATH, '//*[@id="btn_group_textbookvols_1"]/label[1]').click()
    sleep(1)
    for i in range(int(number)):
        iframe = wd.find_element(By.XPATH, '//*[@id="tbody_question_body"]/tr[2]/td[2]/div/div[2]/iframe')
        wd.switch_to.frame(iframe)
        wd.find_element(By.XPATH, '/html/body').send_keys('测试题目')
        sleep(3)
        wd.switch_to.parent_frame()
        wd.find_element(By.XPATH, '//*[@id="question_answers"]/label[4]/strong').click()
        sleep(3)
        wd.find_element(By.XPATH, '//*[@id="btn_submit"]').click()
        sleep(3)
        wd.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[3]/div/div/button[1]').click()
    exit()



