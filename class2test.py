
"""

class car:
    length = 15
    width = 6
    height = 8
    color = 'white'
    volume = length * width * height

print(car.color)
print(car.volume)
print(car.length)
print(car.width)
print(car.height)

"""




"""

class car () :
    color = 'blue'
    
skoda = car 
bmw = car 

skoda.color = 'grey'
bmw.color = 'bronze'

print(skoda.color)
print(bmw.color)

"""






"""

class car () :
    def __init__(self , color) :
        self.color = color
        
skoda = car('grey')
bmw = car ('brnze')

print(skoda.color)
print(bmw.color)    

"""






"""


class calc :
    def __init__(self,p2,p3) :
        self.power2 = p2**2 
        self.power3 = p3**3
        
a = calc (25,60)

print (a.power2)
print(a.power3)

"""





"""

class d : 
    def __init__(self , p2 = 15 , p4 = 30) : 
        self.power2 = p2**2
        self.power4 = p4**4

a = d()

print(a.power2)
print(a.power4)


"""





"""

class d : 
    def __init__(self , p2 = 43 , p4 = 29) : 
        self.power2 = p2**2
        self.power4 = p4**4

a = d(10,11)

print(a.power2)
print(a.power4)

"""








"""

class d :
    def __init__(self , nn , p2 = 5 , p5 = 50) :
        
        self.power2 = p2**2
        self.power5 = p5**5
        self.roots = nn

    def root (self) : 
        print(self.roots**0.5)

a = d (4800)

a.root()

"""










"""

class Account:

    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show(self):
        print(self.name, self.no, self.balance)


a1 = Account(
    "mohamed zoabi",
    "1937155",
    350000
)

a2 = Account(
    "yosef egy",
    "1934761",
    500000
)


print("a1 balance:", a1.balance)
print("a2 no:", a2.no)


a1.deposit(1540)

a1.withdraw(4530)

a2.withdraw(10240)

a2.withdraw(489759.5)  #you don't have money hahaahhahhaahahaahahahaha 

a1.deposit(10000000000)


print("a1 balance:", a1.balance)
print("a2 balance:", a2.balance)


a1.show()
a2.show()

"""








class d : 
    def square(n) :
        print(n**2)
    
    def summ (a,b,c,d,e,f) : 
        return ((a+b-c+e) * (d+f))
    
a = d 
a.square(3)
print (a.summ(1,2,3,4,5,7))