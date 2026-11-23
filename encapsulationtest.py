



class employee : 
    def __init__(self, name, salary) : 
        self.name = name 
        self.salary = salary 
        
    def setmanagersalary(self , obj, newsalary) : 
        obj.salary = newsalary
        
        
class manager : 
    def __int__(self , name, salary) : 
        self.name = name 
        self._salary = salary 
        
    def getmanagersalary(self, obj) : 
        print(obj._salary)


class ceo(manager) : 
    def __init__(self , name, salary) : 
        self.name = name 
        self.salary = salary 
        
    def setmanagersalary(self ,obj, newsalary) : 
        obj._salary = newsalary 
  
    def setceoalary(self , obj, newsalary) : 
        obj.__salary = newsalary
        
    def getceosalary(self , obj) : 
        print(obj.salary)
      
        
emp1 = employee("yosef" , 3000)
mng1 = manager("mohamed" , 5000)

emp1.setmanagersalary(mng1,6000)
mng1.getmanagersalary(mng1)
ceo1 = ceo("khaled" , 20000)
ceo1.setmanagersalary(mng1 , 5700)
mng1.getmanagersalary(mng1)
ceo1.getmanagersalary(mng1)
ceo1.getmanagersalary(ceo1)
ceo1.setceosalary(ceo1 , 35000)
ceo1.getceosalary(ceo1)
