class Marksheet:

    def __init__(self) -> None:
        self.rollno=0
        self.name=""
        self.physics=0
        self.chemistry=0
        self.math=0

    def setRollno(self, rollno):
        self.rollno=rollno
    def getRollno(self):
        return self.rollno
    
    def setName(self, name):
        self.name=name
    def getName(self):
        return self.name
    
    def setPhysics(self, physics):
        self.physics=physics
    def getPhysics(self):
        return self.physics
    
    def setChemistry(self, chemistry):
        self.chemistry=chemistry
    def getChemistry(self):
        return self.chemistry
    
    def setMaths(self, maths):
        self.maths=maths
    def getmaths(self):
        return self.maths
    
