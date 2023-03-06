from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey
from time import time, sleep
desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '10', # 手机安卓版本
  'deviceName': 'TEL-AN00a', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.example.jcy.wvtest', # 启动APP Package名称
  'appActivity': '.MainActivity', # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2',
  'chromeOptions':{'w3c':False}
  # 'app': r'd:\apk\bili.apk',
}
# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
driver.switch_to.context('WEBVIEW_com.example.jcy.wvtest')
driver.find_element(AppiumBy.ID, 'index-kw').send_keys('白月黑羽')
driver.find_element(AppiumBy.ID, 'index-bn').click()
driver.switch_to.context('NATIVE_APP')
driver.find_element(AppiumBy.ID, 'navigation_bili').click()
sleep(2)
driver.find_element(AppiumBy.ID, 'navigation_qq').click()



