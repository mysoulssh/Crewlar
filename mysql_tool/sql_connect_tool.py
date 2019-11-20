import mysql.connector


def is_db_exist(cursor, db_name):
    is_exist = False
    for temp_db in cursor:
        if len(temp_db):
            if db_name in temp_db[0]:
                is_exist = True
                break
    return is_exist


def is_table_exist(cursor, table_name):
    is_exist = False
    for temp_table in cursor:
        if len(temp_table):
            if table_name in temp_table[0]:
                is_exist = True
                break
    return is_exist


class SqlTool:
    def __init__(self, host, user, password):
        assert len(host) != 0
        assert len(user) != 0
        assert len(password) != 0

        self.host = host
        self.user = user
        self.password = password

    def connect_sql(self):
        mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.password
        )
        return mydb

    def connect_sql_db(self, db_name):
        db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            database=db_name,
        )
        return db


DBTool = SqlTool
