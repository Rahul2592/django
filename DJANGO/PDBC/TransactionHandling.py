from dbconfig import getConnection
conn=getConnection("batch3to4apmarch")
csr=conn.cursor()

qry1="Insert Into Marksheet values(6, 'Raju', 90, 85, 69)"
qry2="Insert Into Marksheet values(7, 'Sonu', 80, 75, 79)"
qry3="Insert Into Marksheet values(8, 'Rajkumar', 91, 82, 67)"
try:
    conn.autocommit=False
    csr.execute(qry1)
    csr.execute(qry2)
    csr.execute(qry3)
    conn.commit()
    print("Transaction Done")
except Exception as e:
    print(e)
    conn.rollback()
    print("Transaction Faild")
finally:
    csr.close()
    conn.close()
