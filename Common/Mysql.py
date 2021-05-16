import pymysql



def connect_db():
        db = pymysql.Connect("172.16.0.201", "test", "senmei654123", "dnp_db")
        cursor = db.cursor()
        # /*修改登录医生和护士的手机号*/
        a = cursor.execute("UPDATE dnp_db.mobile_code SET mobile='15213292472',status=1 WHERE code = '3788'")
        # 提交数据库进行执行
        db.commit()




