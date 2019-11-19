import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from mysql_tool import DBTool

headers = {
    "User-Agent": UserAgent(path='./fake_useragent.json').random,
}


def request_url(url_string):
    response = requests.get(url_string, headers=headers)
    content = response.content.decode("gbk")
    soup = BeautifulSoup(content, "lxml")
    soup_tag = soup.find_all('div', attrs={'class': 'el'})
    # print(soup_tag)
    for tag in soup_tag:
        company = tag.find_all('span', class_='t2')
        location = tag.find_all('span', class_='t3')
        money = tag.find_all('span', class_='t4')
        time = tag.find_all('span', class_='t5')
        if len(company):
            var = company[0].text
            print("公司:", var)
        if len(location):
            print("地点:", location[0].text)
        if len(money):
            if len(money[0].text):
                print("工资:", money[0].text)
            else:
                print("工资:", "面议")
        if len(time):
            print("时间:", time[0].text)


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
    is_exist_db = False
    for temp_db in cursor:
        print(temp_db[0])
        if db_string in temp_db[0]:
            is_exist_db = True
            break
    if is_exist_db:
        crewlar_db = db.connect_sql_db("crewlar_db")
        crewlar_db_cursor = crewlar_db.cursor()

        crewlar_db_cursor.execute("CREATE TABLE works (comany VARCHAR(255), job VARCHAR(255), location VARCHAR(255), wages VARCHAR(255), time VARCHAR(255))")
        crewlar_db_cursor.execute("SHOW TABLES")
        for db in crewlar_db_cursor:
            print(db)
    else:
        cursor.execute("CREATE DATABASE crewlar_db")
        print("创建数据库crewlar_db成功")

    # request_url("https://search.51job.com/list/090200,000000,0000,00,9,99,%2B,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=")
