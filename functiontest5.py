


"""

def power (y,c) : 
    x = y**c
    return x 

print(power(2,3))

"""

"""

def power (y,c) : 
    x = y**c
    return x 

def times4 (xx) :
    z = 4*xx 
    return z 

def add7 (zz) : 
    w = zz+7
    return w 

d = int(input('first : '))
dd = int(input('second : '))

print (add7(times4(power(d,dd))))

"""



"""

xx = 5 

def gg () : 
    global xx
    xx = 14 
    
gg ()
print (xx)

"""



"""

powers = lambda x,y : x**y

print (powers(5,3))

"""



"""

powers = [lambda x : 1 , lambda x : x , lambda x : x**2 , lambda x : x**3]

print (powers[0](5))
print (powers[1](5))
print (powers[2](5))
print (powers[3](5))

"""


"""

mylist = [0,1,2,3,4,5,6,7,8,9]

evennumber = list (filter(lambda x : x % 2 == 0 , mylist))
oddnumber = list (filter(lambda x : x % 2 == 1 , mylist))

print (evennumber)
print (oddnumber)

"""


"""

mylist = (0,1,2,3,4,5,6,7,8,9)

print ("square list" , list(map(lambda x : x**2 , mylist)))

"""


"""

list1 = (1,2,3,4,5,6)

def cpower(x) : 
    return x**3

print (list(map(lambda x : cpower(x) , list1)))

#print (lambda x : x**3 , range(0,7))

x = range(7)

def cpower (x) : 
    return x**3

print (list(map(lambda x : cpower(x) , x )))

# warning !!!!! = trying from me 

"""




"""

def yie() : 
    for i in range (10) : 
        yield i 
        
for g in yie() : 

    print (g)

"""    



"""

def yie () : 
    for i in range (10) : 
        yield i 
        
f = yie()

print (next(f))
print (next(f))
print (next(f))
print (next(f))
print (next(f))
print (next(f))
print (next(f))
print (next(f))
print (next(f))
print (next(f))


"""




"""

def fibon (n) : 
    a = b = 1 
    result = []
    for i in range (n) :
        result.append (a)
        a , b = b , a+b
    return result

print (fibon(20))

"""




"""

def fibon (n) : 
    a = b = 1
    
    for i in range (n) : 
        yield a 
        a , b = b , a+b 
        
for x in fibon (20) : 
        print (x)



"""



def fac(n) : 
    if n == 1 : 
        return 1 
    else : 
        return n * fac (n-1)
    
print (fac(10))