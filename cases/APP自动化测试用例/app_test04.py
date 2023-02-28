from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey
from time import time, sleep
desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '10', # 手机安卓版本
  'deviceName': 'TEL-AN00a', # 设备名，安卓手机可以随意填写
  'appPackage': 'tv.danmaku.bili', # 启动APP Package名称
  'appActivity': '.MainActivityV2', # 启动Activity名称
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
# 如果有`青少年保护`界面，点击`我知道了`
# iknow = driver.find_elements(By.ID, "text3")
# if iknow:
#     iknow.click()
iknow = driver.find_elements(By.ID, "button")
if iknow:
    iknow[0].click()

# 协议弹窗
# iknow = driver.find_element(By.ID, "agree")
# if iknow:
#     iknow.click()
# 根据id定位搜索位置框，点击
driver.find_element(By.ID, 'expand_search').click()
# 根据id定位搜索输入框，点击
driver.find_element(By.ID, 'search_src_text').send_keys('白月黑羽')
# 输入回车键，确定搜索
driver.find_element(By.ID, 'action_search').click()
#查看更多
driver.find_element(By.ID, 'more_video').click()
sleep(2)
eles = driver.find_elements(By.ID, 'title')
for ele in eles:
    # 打印标题
    print(ele.text)
sleep(2)
print('111')
while True:
    # text = driver.find_elements(By.ID, 'text1')
    code = 'new UiSelector().text("再怎么找也没有啦")'
    text = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, code)
    print('222')
    print(text)
    if text:
        print('333')
        print(text[0].text)
        if text[0].text == '再怎么找也没有啦':
            break
    else:
        print('444')
        driver.swipe(start_x=700, start_y=2290, end_x=700, end_y=358, duration=800)
        eles = driver.find_elements(By.ID, 'title')
        for ele in eles:
            # 打印标题
            print(ele.text)
# input('**** Press to quit..')
# driver.quit()

