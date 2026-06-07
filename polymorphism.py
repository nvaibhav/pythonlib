class Employee:
    age = 70
    def getAge(self):
        return self.age

class Manager(Employee):
    def __init__(self) -> None:
        super().__init__()
        #self.age = 35

    def setAge(self,myage):
        Employee.age = myage

    def getAge(self):
        return self.age
    
    def resetAge(self):
        Employee.age = 70

manager = Manager()
print("Manager age:", manager.getAge(), end = " ") 
manager.setAge(35)
print("Manager age:", manager.getAge(), end = " ") 
manager.resetAge()
print("Manager age:", manager.getAge(), end = " ") 
