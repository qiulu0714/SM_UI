# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

import os

driver_path = os.path.join(os.path.dirname(__file__), "../chromedriver/chromedriver.exe")
dr = webdriver.Chrome(driver_path)
dr.implicitly_wait(20)

# 打开腾讯企业邮箱
dr.get("https://exmail.qq.com/login")
#完全匹配判定
title1 = EC.title_contains("扫码登录")
print(title1(dr))
# dr.find_element_by_xpath("")
# all_wt = dr.find_elements_by_xpath("//div[3]/div/div/div/div/div[2]/div/div")
# for j in all_wt:
#     j.find_element_by_xpath("//div[3]/div/div/div/div/div[2]/div/div[j]/div/div/label[2]").click()
# continue