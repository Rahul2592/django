from dbconfig import getConnection

conn=getConnection("batch3to4apmarch")
csr=conn.cursor()

qry="Insert Into Marksheet Values(%s,%s,%s,%s,%s)"
rn=input("Enter rollNo\n")
name=input("Enter name\n")
phy=input("Enter physics Score\n")
chem=input("Enter chemistry Score\n")
maths=input("Enter maths Score\n")
record=(rn, name, phy, chem, maths)
i=csr.execute(qry,record)
conn.commit()
print(f"Row Inserted {i}")
csr.close()
conn.close()
