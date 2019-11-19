import mysql.connector
import sys


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


DBTool = SqlTool
