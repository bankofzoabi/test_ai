




class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def printall (self) : 
        print(self.name)
        print(self.age)
        print(self.gender)
        
        
class employee(person):
    def __init__(self, name, age, gender, salary):
        super().__init__(name, age, gender)
        self.salary = salary

    def printall(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.salary)


emp1 = employee("yosef", 25, "male", 2700)
emp1.printall()
       


class manager : 
    def __init__(self, name, id, location) : 
        self.name = name 
        self.id = id 
        self.location = location 
    
    def printall (self) : 
        print(self.name)
        print(self.id)
        print(self.location)
        
man1 = manager("yosef" , 2 , "egypt") 
man1.printall()
        
        
        
class ceo(employee,manager) : 
    def __init__(self, name, age, gender, salary, id, location) :
        manager. __init__(self, name, id, location) 
        employee. __init__(self, name, age, gender, salary)
        
        
    def printall(self) : 
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.salary)
        print(self.id)
        print(self.location)
         
         
ceo1 = ceo("mohamed", 1 , "palestine" , 48 , "male" , 120000) 
ceo1.printall()