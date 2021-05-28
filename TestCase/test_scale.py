#! /usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
import pytest
from selenium.webdriver.support import expected_conditions as EC




class Test_scale():

    @pytest.mark.assess
    def test_assess(self,base):
        base.click("点击患者管理",'''//div[text()="患者管理"]''')
        sleep(2)
        base.click("点击赵俊",'''//span[text()="超级小兵"]''')
        sleep(2)
        base.click("点击评估量表",'''//li[text()="评估量表"]''')
        sleep(2)
        a = base.local_elements('//div/span[text() = "评估"]')
        for i in a:
            print(i)
            base.click("点击评估",'i' )
            base.click("点击取消","//button/span[text()='取 消']")

