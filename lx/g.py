# coding:utf-8

from selenium import webdriver

import os

driver_path = os.path.join(os.path.dirname(__file__), "../chromedriver/chromedriver.exe")
dr = webdriver.Chrome(driver_path)

dr.get("https://www.cnblogs.com/yoyoketang/")

all = dr.find_elements_by_css_selector(".postTitle2")

for i in all:

    i.click()

    print(dr.current_url)   # 打印当前页url

    dr.back()