#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

import pytest
from selenium import webdriver
from Common.Baseui import baseUI
from Common.Mysql import connect_db

@pytest.fixture(scope="session")
def base():
    connect_db()
    # fixture装饰器可以设置前置后置步骤
    # 返回值存到了方法名中
    # 测试用例中，根据方法名来使用该方法的返回值
    driver_path = os.path.join(os.path.dirname(__file__), "../chromedriver/chromedriver.exe")
    # 打开浏览器
    dr = webdriver.Chrome(driver_path)
    dr.maximize_window()  # 最大化浏览器
    dr.implicitly_wait(8)  # 设置隐式时间等待
    # 使用baseUI
    base = baseUI(dr)
    # 打开登录页面
    dr.get("https://n-web.sersmed.cn/#/login")
    # 输入用户名
    base.send_keys("输入手机号", '''//input[@placeholder="手机号"]''', '15213292472')
    # 输入密码
    base.send_keys("输入密码", '''//input[@placeholder="验证码"]''', '3788')
    # 点击登录
    base.click("点击登录", """//button/span[text()="登 录"]""")
    assert '肃医慢病临床病情管理(护士)系统' in dr.page_source
    yield base
    dr.quit()




@pytest.fixture(scope="session")
def test_session():
    print('------------------session之前---------------------------')
    yield
    print('------------------session之后---------------------------')

@pytest.fixture(scope="module")
def test_module():
    print('------------------module之前---------------------------')
    yield
    print('------------------module之后---------------------------')
@pytest.fixture(scope="class")
def test_class():
    print('------------------class之前---------------------------')
    yield
    print('------------------class之后---------------------------')

@pytest.fixture(scope="function")
def test_function():
    print('------------------function之前---------------------------')
    yield
    print('------------------function之后---------------------------')

