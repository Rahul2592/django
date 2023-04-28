from dbconfig import getConnection
conn=getConnection("batch3to4apmarch")
csr=conn.cursor()
qry="Delete from Marksheet where rollno=?"
rn=input("Enter rollno\n")
i=csr.execute(qry,rn)
conn.commit()
print(f"Row Deleted {i}")
csr.close()
conn.close()