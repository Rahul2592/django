from dbconfig import getConnection

conn=getConnection("batch3to4apmarch")
csr=conn.cursor()
qry="Select * from Marksheet order by physics desc"
rn=input("Enter RollNo get Marksheet\n")
csr.execute(qry)
data=csr.fatchmany(3)
print(data)

for row in data:
    print(row)

print("-----------------------------")
print("Rollno\tName\tPhy\tChem\tMaths")
for row in data:
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")
csr.close()
conn.close()
