import random
from time import sleep
import pytest
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver_path = os.path.join(os.path.dirname(__file__), "../chromedriver/chromedriver.exe")
dr = webdriver.Chrome(driver_path)
dr.maximize_window()  # 最大化浏览器
dr.implicitly_wait(8)  # 设置隐式时间等待
from Common.Mysql import connect_db

def test_assess():
    connect_db()
    dr.get("https://n-web.sersmed.cn/#/login")
    # 输入用户名
    dr.find_element_by_xpath('''//input[@placeholder="手机号"]''').send_keys('15213292473')
    sleep(2)
    # 输入密码
    dr.find_element_by_xpath('''//input[@placeholder="验证码"]''').send_keys('3788')
    sleep(2)
    # 点击登录
    dr.find_element_by_xpath("""//button/span[text()="登 录"]""").click()
    sleep(2)
    dr.find_element_by_xpath('''//div[text()="患者管理"]''').click()
    sleep(2)
    dr.find_element_by_xpath('''//span[text()="超级小兵"]''').click()
    sleep(2)
    dr.find_element_by_xpath('''//li[text()="评估量表"]''').click()
