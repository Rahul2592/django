from dbconfig import getConnection

conn=getConnection("batch3to4apmarch")
csr=conn.cursor()
qry="Insert Into Marksheet value (1, 'Rahul',85,90,89.5)"
i=csr.execute(qry)
conn.commit()
print(f"Row Inserted {i}")
csr.close()
conn.close()