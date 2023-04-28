from dbconfig import getConnection
conn=getConnection("batch3to4apmarch")
csr=conn.cursor()

csr.execute("Select * from Marksheet")
metadata=csr.description
for data in metadata:
    print(data)
csr.close()
conn.close()
