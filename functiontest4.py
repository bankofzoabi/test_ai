


"""

def powers(m, n = 4) :
    
    print(m**(n))
    
powers(3,2)

"""



"""

def powers(m , n = 4) :
    
    print (m**(n))
    
powers(3)

"""

"""

def powers (m,n) :
    
    print (m**(n))
    
powers (m = 3 , n = 4)

"""


"""

def powers (m,n) :
    
    print (m**(n))
    
powers (n = 3 , m = 4)

"""



"""

def parrot(voltage , state = 'a stiff' , action = 'voom' ,type = 'norwegian blue') :
    
    print ("-- This parrot wouldn't " , action)
    print ("if you put" , voltage, "volts through it.")
    print ("-- lovely plumage , the" , type)
    print ("-- it's" , state , "!")
    
    
parrot (1000) # 1 positional argument
parrot (voltage = 1000) # 1 keyword argument
parrot (voltage = 1000000 , action = 'VOOOOOM') # 2 keyword arguments

"""
    



"""

def parrot(voltage , state = 'a stiff' , action = 'voom' ,type = 'norwegian blue') :
    
    print ("-- This parrot wouldn't " , action)
    print ("if you put" , voltage, "volts through it.")
    print ("-- lovely plumage , the" , type)
    print ("-- it's" , state , "!")
    
    
    
parrot (action = 'VOOOOOM' , voltage = 1000000) # 2 keyword arguments
parrot ('a million' , 'bereft of life' , 'jump') # 3 posintional arguments
parrot ('a thousand' , state = 'puching up the') # 1 postional , 1 keyword


"""