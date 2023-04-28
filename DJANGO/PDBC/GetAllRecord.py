from dbconfig import getConnection
conn=getConnection("batch3to4apmarch")
csr=conn.cursor()

qry="Select * from Marksheet"
result=csr.execute(qry)
data=csr.fatchall()
print(data)
csr.close()
conn.close()
