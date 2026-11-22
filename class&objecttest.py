class employee : 
    
    def __init__(self , name , age , gender , salary) : 
        
        self.name = name
        
        self.age = age 
        
        self.gender = gender 
        
        self.salary = salary 
     
    def totalsalary(self, target) : 
        totalsalary = self.salary + target 
        print("totalsalary = " , totalsalary)
        return totalsalary
        
    def printall(self) : 
        print("name =  " , self.name)
        print("age =  " , self.age)
        print("gender =  " , self.gender)
        print("salary =  " , self.salary)
        
em1 = employee ("yosef" , 25 , "male" , 2500)
em1.printall()
em1.totalsalary(1000)


em2 = employee ("mohamed" , 24 , "male" , 1500)
em2.printall()
em2.totalsalary(1500)
