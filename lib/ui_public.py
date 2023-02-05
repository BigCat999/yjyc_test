from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from hytest import *

def open_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(10)
    GSTORE['wd'] = wd

def login():
    wd = GSTORE['wd']
    wd.get('http://127.0.0.1:8087/mgr/sign.html')
    wd.find_element(By.CSS_SELECTOR, '#username').send_keys('byhy')
    wd.find_element(By.CSS_SELECTOR, '#password').send_keys('88888888')
    wd.find_element(By.CSS_SELECTOR, 'button[type = "submit"]').click()