from crewlar_data import area_info
from mysql_tool import DBTool
from mysql_tool import is_db_exist, is_table_exist


def connect_db(db_tool, db_name, table_name):
    db = db_tool.connect_sql_db(db_name)
    cursor = db.cursor()
    cursor.execute("create table if not exists {0} (id INT AUTO_INCREMENT PRIMARY KEY, location_id TEXT, location_name TEXT, p_id TEXT, p_name TEXT, it_id TEXT, it_name TEXT) charset utf8".format(
        table_name))

    cursor.execute("select * from "+table_name+" where location_name = '成都'")
    result = cursor.fetchall()

    for x in result:
        print(x)

    # areaInfo = area_info.AreaInfo()
    # localDic = areaInfo.area
    # localtions = []
    # for k, v in localDic.items():
    #     localtions.append((k, v))
    #
    # if len(localtions):
    #     print(localtions)
    #     sql = "insert into {0} (location_id, location_name) values (%s, %s)".format(table_name)
    #     cursor.executemany(sql, localtions)
    #     db.commit()
    #     print("插入数据成功")


if __name__ == '__main__':
    # areaInfo = area_info.AreaInfo()
    # areaDic = areaInfo.area_detail
    # localDic = areaInfo.area

    # for k, v in areaDic.items():
    #     print("市/洲："+localDic[k])
    #     area_nums = str(v).split(",")
    #     areas = []
    #     for num in area_nums:
    #         areas.append(localDic[num])
    #     print(areas)

    # 替换key与value
    # resultLocal = {}
    # for k, v in localDic.items():
    #     resultLocal[v] = k
    # print(resultLocal)

    # input_local = input("请输入地区名：")
    # ret = resultLocal[input_local]
    # print("编号:"+ret)

    # 将地区存入数据库
    # 初始化数据库工具
    db = DBTool(host="localhost", user="root", password="Qwe123456")
    # 连接数据库
    mydbtool = db.connect_sql()
    cursor = mydbtool.cursor()

    db_string = "crewlar_db"
    db_table_string = "work_infos"

    cursor.execute("SHOW DATABASES")
    exist_db = is_db_exist(cursor, db_string)
    if exist_db:
        connect_db(db, db_string, db_table_string)
