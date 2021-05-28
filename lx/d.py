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




    all_pg = dr.find_elements_by_xpath('//div/span[text() = "评估"]')
    for i in all_pg:
        print(i)
        i.click()
        sleep(1)
        text = dr.find_element_by_xpath('//p[@class = "ASL-name"]').text
        if "医院焦虑抑郁量表(HAD)" in text :
            all_wt = dr.find_elements_by_xpath('//div[@class="onlyRadio-box"]')
            for j in range(len(all_wt)):
                suiji = random.randint(1, 4)
                dr.find_element_by_xpath('//div[%s]/div/div/label[{}]'.format(suiji) % (j + 2)).click()
                sleep(1)
            # dr.find_element_by_xpath("//button/span[text()='确 定']").click()
        # elif  "MOS-SS睡眠量表" in text :find_elements_by_xpath('//div[@class="onlyRadio-box"]')
        #         #     for j in range(len(all_wt)):
        #         #         try
            #     all_wt = dr.:
        #             suiji = random.randint(1, 5)
        #             dr.find_element_by_xpath('//div[%s]/div/div/label[{}]'.format(suiji)%(j+2)).click()
        #             sleep(1)
        #         except:
        #             dr.find_element_by_xpath('//input[@type="text"]').send_keys("8")
        #             sleep(1)
        #     # dr.find_element_by_xpath("//button/span[text()='确 定']").click()
        # elif  "国际不安腿综合征研究组评分标准（IRLSSG）" in text:
        #     all_wt = dr.find_elements_by_xpath('//div[@class="onlyRadio-box"]')
        #     for j in range(len(all_wt)):
        #         suiji = random.randint(1, 5)
        #         dr.find_element_by_xpath('//div[%s]/div/div/label[{}]'.format(suiji) % (j + 2)).click()
        #         sleep(1)
        #     # dr.find_element_by_xpath("//button/span[text()='确 定']").click()
        # elif "焦虑自评量表（SAS）" in text :
        #     all_wt = dr.find_elements_by_xpath('//div[@class="onlyRadio-box"]')
        #     for j in range(len(all_wt)):
        #         suiji = random.randint(1, 4)
        #         dr.find_element_by_xpath('//div[%s]/div/div/label[{}]'.format(suiji) % (j + 2)).click()
        #         sleep(1)
        #     # dr.find_element_by_xpath("//button/span[text()='确 定']").click()
        # elif "自评抑郁量表(SDS)" in text :
        #     all_wt = dr.find_elements_by_xpath('//div[@class="onlyRadio-box"]')
        #     for j in range(len(all_wt)):
        #         suiji = random.randint(1, 4)
        #         dr.find_element_by_xpath('//div[%s]/div/div/label[{}]'.format(suiji) % (j + 2)).click()
        #         sleep(1)
        #     # dr.find_element_by_xpath("//button/span[text()='确 定']").click()
        elif "社会支持评估量表" in text:
            all_wt_1 = dr.find_elements_by_xpath('//div[@class="onlyRadio-box"]')
            all_wt_2 = dr.find_elements_by_xpath('//div[@class="TRadio"]')
            all_wt_3 = dr.find_elements_by_xpath('//div[@class="RCAll"]')
            all_wt = all_wt_1 + all_wt_2 + all_wt_3
            for i in range(len(all_wt_1)):
                suiji = random.randint(1, 4)
                dr.find_element_by_xpath('(//div[@class="onlyRadio-box"])[%s]/child::div//label[{}]'.format(suiji) % (i + 1)).click()
                sleep(1)
            for j in range(len(all_wt_2)):
                suiji = random.randint(1, 4)
                dr.find_element_by_xpath('(//div[@class="TRadio"])[%s]/child::div//label[{}]'.format(suiji) % (j + 1)).click()
                sleep(1)
            for k in range(len(all_wt_3)):
                for d in range(1,8,2):
                    dr.find_element_by_xpath("(//span[text() = '下列来源（可选多项）'])[%s]/preceding-sibling::*"% (k + 1)).click()
                    sleep(1)
                    dr.find_element_by_xpath('(//div[@class="RCAll"])[%s]//div/div/div/label[%s]'%(k+1,d)).click()
                    sleep(1)
            # dr.find_element_by_xpath("//button/span[text()='确 定']").click()
        # elif "医院焦虑抑郁量表(HAD)" in text :
        #     all_wt = dr.find_elements_by_xpath("//div[3]/div/div/div/div/div[2]/div/div/div[1]")
        #     for j in range(len(all_wt)):
        #         suiji = random.randint(1, 5)
        #         dr.find_element_by_xpath('//div[%s]/div/div/label[{}]'.format(suiji) % (j + 2)).click()
        #     # dr.find_element_by_xpath("//button/span[text()='确 定']").click()
        # elif "自评抑郁量表(SDS)" in text :
        #     all_wt = dr.find_elements_by_xpath("//div[3]/div/div/div/div/div[2]/div/div/div[1]")
        #     for j in range(len(all_wt)):
        #         suiji = random.randint(1, 5)
        #         dr.find_element_by_xpath('//div[%s]/div/div/label[{}]'.format(suiji) % (j + 2)).click()
        #         # dr.find_element_by_xpath("//button/span[text()='确 定']").click()
        # elif "生活质量评估量表  " in text :
        #     all_wt = dr.find_elements_by_xpath("//div[3]/div/div/div/div/div[2]/div/div/div[1]")
        #     for j in range(len(all_wt)):
        #         suiji = random.randint(1, 5)
        #         dr.find_element_by_xpath('//div[%s]/div/div/label[{}]'.format(suiji) % (j + 2)).click()
        #         # dr.find_element_by_xpath("//button/span[text()='确 定']").click()
        # elif "简易精神状态检查量表MMSE" in text :
        #     all_wt = dr.find_elements_by_xpath("//div[3]/div/div/div/div/div[2]/div/div/div[1]")
        #     for j in range(len(all_wt)):
        #         suiji = random.randint(1, 5)
        #         dr.find_element_by_xpath('//div[%s]/div/div/label[{}]'.format(suiji) % (j + 2)).click()
        #         # dr.find_element_by_xpath("//button/span[text()='确 定']").click()
        # elif  "MOS-SS睡眠量表" in text :
        #     suiji = random.randint(1,5)
        #     all_wt = dr.find_elements_by_xpath("//div[3]/div/div/div/div/div[2]/div/div/div[1]")
        #     for j in range(len(all_wt)):
        #         suiji = random.randint(1, 5)
        #         dr.find_element_by_xpath('//div[%s]/div/div/label[{}]'.format(suiji) % (j + 2)).click()
        #         # dr.find_element_by_xpath("//button/span[text()='确 定']").click()
        # elif "国际不安腿综合征研究组评分标准（IRLSSG）" in text :
        #     all_wt = dr.find_elements_by_xpath("//div[3]/div/div/div/div/div[2]/div/div/div[1]")
        #     for j in range(len(all_wt)):
        #         suiji = random.randint(1, 5)
        #         dr.find_element_by_xpath('//div[%s]/div/div/label[{}]'.format(suiji) % (j + 2)).click()
        #         # dr.find_element_by_xpath("//button/span[text()='确 定']").click()
        # elif "SGA营养" in text :
        #     all_wt = dr.find_elements_by_xpath("//div[3]/div/div/div/div/div[2]/div/div/div[1]")
        #     for j in range(len(all_wt)):
        #         suiji = random.randint(1, 5)
        #         dr.find_element_by_xpath('//div[%s]/div/div/label[{}]'.format(suiji) % (j + 2)).click()
        #         # dr.find_element_by_xpath("//button/span[text()='确 定']").click()
        # elif  "症状自评" in text :
        #     suiji = random.randint(1,5)
        #     all_wt = dr.find_elements_by_xpath("//div[3]/div/div/div/div/div[2]/div/div/div[1]")
        #     for j in range(len(all_wt)):
        #         suiji = random.randint(1, 5)
        #         dr.find_element_by_xpath('//div[%s]/div/div/label[{}]'.format(suiji) % (j + 2)).click()
        #         # dr.find_element_by_xpath("//button/span[text()='确 定']").click()
        # elif "焦虑自评量表（SAS）" in text :
        #     all_wt = dr.find_elements_by_xpath("//div[3]/div/div/div/div/div[2]/div/div/div[1]")
        #     for j in range(len(all_wt)):
        #         suiji = random.randint(1, 5)
        #         dr.find_element_by_xpath('//div[%s]/div/div/label[{}]'.format(suiji) % (j + 2)).click()
        #         # dr.find_element_by_xpath("//button/span[text()='确 定']").click()
        # elif "医院焦虑抑郁量表(HAD)" in text :
        #     all_wt = dr.find_elements_by_xpath("//div[3]/div/div/div/div/div[2]/div/div/div[1]")
        #     for j in range(len(all_wt)):
        #         suiji = random.randint(1, 5)
        #         dr.find_element_by_xpath('//div[%s]/div/div/label[{}]'.format(suiji) % (j + 2)).click()
        #         # dr.find_element_by_xpath("//button/span[text()='确 定']").click()
        else:
            print(2)
        print(text)
        dr.find_element_by_xpath("//button/span[text()='取 消']").click()
        sleep(2)
        continue


        # # b = dr.find_element_by_xpath('''//div[@class = 'ASL-title']''')
        # # try:
        # #     b = EC.title_is(u"症状自评（SCL-90）")
        # #     print("存在")

        # # except:
        # #     print("不存在")
if __name__ == '__main__':
    test_assess()