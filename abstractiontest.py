

from abc import ABCMeta , abstractmethod



class animal(metaclass=ABCMeta) : 
    @abstractmethod
    def __init__(self , name, speed) : 
        self.name = name 
        self.speed = speed 
        
        
    @abstractmethod
    def getsound (self) : 
        pass 
    
    
    def ihave (self) :
        print('ihave a body')
        print('ihave a eyes')
        print('ihave a heart')
        

class dog(animal) : 
    def __init__(self , name, speed) :
        animal.__init__(self , name, speed) 
        
    def getsound(self) : 
        print('ho ho')
        
        

class cat(animal) : 
    def __init__(self , name, speed) :
        animal.__init__(self , name, speed) 
        
    def getsound(self) : 
        print('meow')
        
        
dog1 = dog('leo' , 80)
print(dog1.name) 
print(dog1.speed) 

cat1 = cat('kitty' , 20) 
print(cat1.name)
print(cat1.speed) 

dog1.getsound()
cat1.getsound()

dog1.ihave()
cat1.ihave()
        