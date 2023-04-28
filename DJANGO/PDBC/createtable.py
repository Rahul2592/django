# 1. Import the Module
import pymysql
print("Module imported")

# 2. create a connection object
connection=pymysql.connect(host="localhost",
                port=3306,
                user="root",
                password="Sonu@2592",
                database="batch3to4apmarch")
print("Connection established")

#3. Create a cursor Object
csr=connection.cursor()

#4. Create a Sql Query 
qry="""Create Table Marksheet 
(rollno int primary key,
name varchar(20), physics float, chemistry float, maths float)
"""
#5. Execute query using cursor Object
csr.execute(qry)
print("Table Is Created")

#6. Close the Connection and cursor
csr.close()
connection.close()