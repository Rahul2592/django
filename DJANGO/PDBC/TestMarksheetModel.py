from MarksheetModel import MarksheetDAO
from Marksheet import Marksheet

class TestMarksheet:
    def testAdd():
        model=MarksheetDAO()

        #rn=input("Enter rollNo\n")
        rn=model.nextPk()
        name=input("Enter name\n")
        phy=input("Enter physics Score\n")
        chem=input("Enter chemistry Score\n")
        maths=input("Enter maths Score\n")

        bean=Marksheet()
        bean.setRollno(rn)
        bean.setName(name)
        bean.setPhysics(phy)
        bean.setChemistry(chem)
        bean.setMaths(maths)

        res=model.add(bean)
        if res:
            print("Marksheet Add Successfully")
        else:
            print("Marksheet Not Added")


TestMarksheet.testAdd()