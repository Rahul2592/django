from dbconfig import getConnection

conn=getConnection("batch3to4apmarch")
csr=conn.cursor()
qry="Select * from Marksheet where rollno=%s"
rn=input("Enter RollNo get Marksheet\n")
result=csr.execute(qry, rn)
row=csr.fatchone()
print(row)
print("Rollno\tName\tPhy\tChem\tMaths")
print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")
csr.close()
conn.close()
