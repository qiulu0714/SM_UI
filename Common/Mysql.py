import pymysql



def connect_db():
        db = pymysql.Connect(host = "47.101.43.146", user = "test", password = "senmei654123", db = "dnp_db",
                             port = 64316 )
        cursor = db.cursor()
        # /*修改登录医生和护士的手机号*/
        a = cursor.execute("UPDATE dnp_db.mobile_code SET mobile='15213292473',status=1 WHERE code = '3788'")
        # 提交数据库进行执行
        db.commit()



if __name__ == '__main__':
    connect_db()


