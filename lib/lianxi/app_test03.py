from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey
from time import time, sleep

desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '10', # 手机安卓版本
  'deviceName': 'TEL-AN00a', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.ibox.calculators', # 启动APP Package名称
  'appActivity': 'com.ibox.calculators.SplashActivity', # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}
# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 设置缺省等待时间
driver.implicitly_wait(5)
# driver.find_element(By.ID, 'com.ibox.calculators:id/user_privacy_ok').click()
# # sleep(10)
amt = driver.find_element(By.CLASS_NAME, 'android.view.View')
if amt:
  amt.click()
driver.find_element(By.ID, 'com.ibox.calculators:id/digit3').click()
driver.find_element(By.ID, 'com.ibox.calculators:id/plus').click()
driver.find_element(By.ID, 'com.ibox.calculators:id/digit9').click()
driver.find_element(By.ID, 'com.ibox.calculators:id/equal').click()
driver.find_element(By.ID, 'com.ibox.calculators:id/mul').click()
driver.find_element(By.ID, 'com.ibox.calculators:id/digit5').click()
driver.find_element(By.ID, 'com.ibox.calculators:id/equal').click()
sleep(2)
# text = driver.find_element(By.ID, '9f11a414-fdc2-42ee-bdaa-21edc1030663').text
result = driver.find_element(AppiumBy.XPATH, '//android.widget.RelativeLayout[@resource-id="com.ibox.calculators:id/cv"]/android.widget.TextView[2]').text
result = driver.find_element(AppiumBy.XPATH, '//android.widget.RelativeLayout[@resource-id="loading_view"]').text



if result == '60':
  print('测试通过')
else:
  print('测试失败')



# # 如果有`青少年保护`界面，点击`我知道了`
# iknow = driver.find_elements(By.ID, "text3")
# if iknow:
#     iknow.click()
#
# # 根据id定位搜索位置框，点击
# driver.find_element(By.ID, 'expand_search').click()
#
# # 根据id定位搜索输入框，点击
# sbox = driver.find_element(By.ID, 'search_src_text')
# sbox.send_keys('白月黑羽')
# # 输入回车键，确定搜索
# driver.press_keycode(AndroidKey.ENTER)
#
# # 选择（定位）所有视频标题
# eles = driver.find_elements(By.ID, 'title')
#
# for ele in eles:
#     # 打印标题
#     print(ele.text)
#
# input('**** Press to quit..')
# driver.quit()