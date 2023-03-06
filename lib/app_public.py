from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from lib.config import configs
from hytest import *


def app_lianjie(appPackage, appActivity):
    desired_caps = {
        'platformName': 'Android',  # 被测手机是安卓
        'platformVersion': '10',  # 手机安卓版本
        'deviceName': 'TEL-AN00a',  # 设备名，安卓手机可以随意填写
        'appPackage': appPackage,  # 启动APP Package名称
        'appActivity': appActivity,  # 启动Activity名称
        # 'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
        'resetKeyboard': True,  # 执行完程序恢复原来输入法
        'noReset': True,  # 不要重置App
        'newCommandTimeout': 6000,
        'automationName': 'UiAutomator2',
        'chromeOptions': {'w3c': False}
        # 'app': r'd:\apk\bili.apk',
    }
    return desired_caps


def login(url=configs.url, vcode=configs.vcode):
    desired_caps = app_lianjie('com.yjyxapp', '.MainActivity')
    wd = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    GSTORE['wd'] = wd
    # 设置缺省等待时间
    wd.implicitly_wait(5)
    sleep(2)
    setting = wd.find_elements(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="tabnav-settings"]/android.widget.TextView')
    print(setting)
    if setting:
        setting[0].click()
        wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                        '/android.view.ViewGroup[2]/android.view.ViewGroup['
                                        '1]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup'
                                        '/android.view.ViewGroup[1]/android.widget.TextView[2]').click()
    wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                    '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view'
                                    '.ViewGroup[2]/android.widget.EditText').send_keys(url)
    wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                    '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view'
                                    '.ViewGroup[3]/android.widget.EditText').send_keys(vcode)
    wd.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                    '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view'
                                    '.ViewGroup[4]/android.widget.TextView').click()


