from Marksheet import Marksheet
from dbconfig import getConnection

class MarksheetDAO:
    def nextPk(self):
        conn=getConnection("batch3to4apmarch")
        csr=conn.cursor()
        qry="Select max(rollno) from Marksheet"
        csr.execute(qry)
        pk=csr.fatchone()
        print(pk)
        return pk[0]+1


    def add(self, bean=None):
        if isinstance(bean, Marksheet):
            conn=getConnection("batch3to4apmarch")
            csr=conn.cursor()
            qry="Insert into Marksheet value (%s,%s,%s,%s,%s)"
            rn=bean.getRollno()
            name=bean.getName()
            p=bean.getPhysics()
            c=bean.getChemistry()
            m=bean.getmaths()
            i=csr.execute(qry,(rn, name,p,c,m))
            csr.close()
            conn.close()
            if(i>0):
                return True
            else:
                return False
