__author__ = 'shadow walker'

import mysqlClass

dbConnection = mysqlClass.MySQL('localhost', 3306, 'root', '', 'mysql')
sql = "SELECT * FROM USERS"
print(dbConnection)
print(sql)
print(dbConnection.executeSQL(sql))