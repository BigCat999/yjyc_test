from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from hytest import *
from lib.config import configs

def open_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(10)
    GSTORE['wd'] = wd

def login(username, password, path):
    url = configs.url
    wd = GSTORE['wd']
    wd.get(f'{url}{path}')
    wd.find_element(By.CSS_SELECTOR, '#username').send_keys(username)
    wd.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
    wd.find_element(By.CSS_SELECTOR, 'button[id = "submit"]').click()

def exit():
    wd = GSTORE['wd']
    wd.find_element(By.XPATH, '//*[@id="topbar"]/div/ul[2]/li/a/span[1]').click()
    wd.find_element(By.XPATH, '//*[@id="topbar"]/div/ul[2]/li/ul/li[4]/a/i').click()




