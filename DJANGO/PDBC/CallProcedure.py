from dbconfig import getConnection
conn=getConnection("batch3to4apmarch")
csr=conn.cursor()

csr.callproc("getalldata")
for res in csr.fetchall():
    print(res)
csr.close()
conn.close()