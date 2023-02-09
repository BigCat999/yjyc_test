from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from hytest import *
import  config

def open_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(10)
    GSTORE['wd'] = wd

def login(username, password, path):
    url = config.configs.url
    wd = GSTORE['wd']
    wd.get(f'{url}{path}')
    wd.find_element(By.CSS_SELECTOR, '#username').send_keys(username)
    wd.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
    wd.find_element(By.CSS_SELECTOR, 'button[type = "submit"]').click()

if __name__ == '__main__':
    open_browser()
    login(123,345)