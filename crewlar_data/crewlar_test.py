import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from mysql_tool import DBTool
from mysql_tool import is_db_exist, is_table_exist

headers = {
    "User-Agent": UserAgent(path='./fake_useragent.json').random,
}


def request_url(url_string, cursor, db):
    response = requests.get(url_string, headers=headers)
    content = response.content.decode("gbk")
    soup = BeautifulSoup(content, "lxml")
    soup_tag = soup.find_all('div', attrs={'class': 'el'})
    # print(soup_tag)

    # sql = "INSERT INTO {0} (company, job, location, wages, pu_time, local_code) VALUES (%s, %s, %s, %s, %s, %s)".format("works")
    # val = ("1", "2", "3", "4", "5", "6")
    # cursor.execute(sql, val)
    # db.commit()
    # print("加入记录:", cursor.rowcount)

    for tag in soup_tag:
        company = tag.find_all('span', class_='t2')
        location = tag.find_all('span', class_='t3')
        money = tag.find_all('span', class_='t4')
        time = tag.find_all('span', class_='t5')

        works = tag.find_all('a')

        if len(company):
            var = company[0].text
            print("公司:", var)
        if len(location):
            var = location[0].text
            print("地点:", var)
        if len(money):
            var = money[0].text
            if len(var):
                print("工资:", var)
            else:
                print("工资:", "面议")

        if len(time):
            print("时间:", time[0].text)

        if len(company):
            job = "工作"
            if len(works):
                var = works[0]
                job = var['title']
            print("工作:", job)

            sql = "INSERT INTO {0} (company, job, location, wages, pu_time, local_code) VALUES (%s, %s, %s, %s, %s, %s)".format("works")
            if len(money):
                # val = (company[0].text, job, location[0].text, money[0].text, time[0].text, "090200")
                val = ("28282", "6", "6", "4", "5", "6")
                cursor.execute(sql, val)
                db.commit()
            else:
                val = (company[0].text, job, location[0].text, "面议", time[0].text, "090200")
                cursor.execute(sql, val)
                db.commit()
            break

    print("完成")


def connect_db(db_tool, db_name):
    crewlar_db = db_tool.connect_sql_db(db_name)
    crewlar_db_cursor = crewlar_db.cursor()

    table_name = "works"
    crewlar_db_cursor.execute("SHOW TABLES")
    has_table = is_table_exist(crewlar_db_cursor, table_name)
    url_string = "https://search.51job.com/list/090200,000000,0000,00,9,99,%2B,2," \
                 "1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
    if has_table:
        print("存在表:", table_name)
        # 删除表
        # sql = "DROP TABLE IF EXISTS {}".format(table_name)
        # crewlar_db_cursor.execute(sql)

        request_url(url_string, crewlar_db_cursor, crewlar_db)

        # sql = "INSERT INTO {0} (company, job, location, wages, pu_time, local_code) VALUES (%s, %s, %s, %s, %s, %s)".format("works")
        # val = ("1", "2", "3", "4", "5", "6")
        # crewlar_db_cursor.execute(sql, val)
        # crewlar_db.commit()
        # print("加入记录:", crewlar_db_cursor.lastrowid)


    else:
        crewlar_db_cursor.execute("CREATE TABLE {0} (id INT AUTO_INCREMENT PRIMARY KEY, company TEXT, job TEXT, location TEXT, wages TEXT, "
                                  "pu_time TEXT, local_code TEXT)".format(table_name))
        crewlar_db_cursor.execute("SHOW TABLES")
        if is_table_exist(crewlar_db_cursor, table_name):
            print("创建表{}成功".format(table_name))
            request_url(url_string, crewlar_db_cursor, crewlar_db)


if __name__ == '__main__':
    print("Hello python")
    db = DBTool(host="localhost", user="root", password="Qwe123456")
    print(db.host, db.user, db.password)
    mydb = db.connect_sql()
    cursor = mydb.cursor()
    # 创建数据库
    # cursor.execute("CREATE DATABASE crewlar_db")
    db_string = "crewlar_db"
    cursor.execute("SHOW DATABASES")
    is_exist_db = is_db_exist(cursor, db_string)
    if is_exist_db:
        print("存在数据库", db_string)
        connect_db(db, db_string)
    else:
        cursor.execute("CREATE DATABASE {0}".format(db_string))
        cursor.execute("SHOW DATABASES")
        if is_db_exist(cursor, db_string):
            print("创建数据库{0}成功".format(db_string))
            connect_db(db, db_string)
