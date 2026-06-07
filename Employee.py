class Employee:
  name = "Ben"
  designation = "Sales Executive"
  salesMadeThisWeek = 6

  def __init__(self, argname):
      self.name = argname

  def hasAchievedTarget(self):
      if (self.salesMadeThisWeek >= 6):
          print("Target has been achieved")
      else:
          print("Target has not been achieved")

  def employeeDetails(self):
      self.name = "Ben"
      print("Name=",self.name)

  def printEmployeeDetails(self):
      print("Printing in another method")
      print("Name:",self.name)
      #print("Age:",age)

  def printme(self):
      print("I am in static method")
      

    
