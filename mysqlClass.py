__author__ = 'shadow walker'
import pymysql
import pymysql.cursors


class MySQL:
    def __init__(self, DBHOST, DBPORT, DBUSER, DBPASSWD, DBNAME):
        try:
            self.conn = pymysql.connect(host=DBHOST, port=DBPORT, user=DBUSER, passwd=DBPASSWD, db=DBNAME,cursorclass=pymysql.cursors.DictCursor)
        except ConnectionError as exc:
            print("DB Connection Failed. Exception that occured: ", exc);
            exit

    def executeSQL(self,sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
        except Exception as sql_exception:
            print("Sql Failed:" + sql + " Reason: " + sql_exception)
            exit

        temp = []
        result = {}

        count = 0
        for row in cur:
            temp.append(row)
            count += 1
        result['rows'] = temp
        result['count'] = count
        cur.close()
        return result

    def escapeString(self,arg):
        return self.conn.escape_string(arg)

    def lastInsertId(self):
        self.conn.insert_id()

    def afftectedRows(self):
        self.conn.affected_rows()

    def destroy(self):
        self.conn.close()