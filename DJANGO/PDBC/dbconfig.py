import pymysql

def getConnection(dbname=None):
    conn=pymysql.connect(host="localhost",
                    port=3306,
                    user="root",
                    password="Sonu@2592",
                    db=dbname)
    return conn
