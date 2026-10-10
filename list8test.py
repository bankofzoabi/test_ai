
"""


a = iter([1, 4, 3, 5, 5, 7, 3, 5, 8, 9, 3, 1, 3, 5])


print(len(list(a)))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))



b = iter(['mohamed','yosef','alaa','sara','hanen','mona','ahmad']) 


print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

print(len(next(b)))
print(len(next(b)))
print(len(next(b)))
print(len(next(b)))
print(len(next(b)))
print(len(next(b)))
print(len(next(b)))



c = next(b)
print(c[0])
c = next(b)
print(c[0])
c = next(b)
print(c[0])
c = next(b)
print(c[0])
c = next(b)
print(c[0])
c = next(b)
print(c[0])
c = next(b)
print(c[0])

"""


"""

x = [1,2,4,3,5,6,9,8,7,4,3,2,5,3,5,6,9,7,6]

w = [4,6,4,2,5,7,8,4,2,1,4,6,7,6,4,3,2,2,4,6,4,2]

print(len(x))
print(x[4])
print(x[8])
print(w[12])
print(len(w))
print(w[21])

y = x 

z = w 

z.extend(y)

print(z)

"""


"""

x = [1,2,5,7,3,8,9,2,4,5,3,5,7,9,2]

y = x.copy()

f = x.copy()

g = x.copy()

h = x.copy()

print (y[3])

print (y)

print(len(x))

f[5] = 55 
y[3] = 99
g[1] = 100
h[7] = 200

print(y)
print(f) 
print(g)
print(h)

"""



"""

namesofstudents = [4,3,2,5,6,2,3,5,4,2,1]

copyofnames = namesofstudents.copy()

secondcopy = namesofstudents.copy()

thirdcopy = namesofstudents.copy()

"""

"""

names = ["a","v ","s ","w ","t ","g ","y ","h ","n ","m "]

for c , value in enumerate (names , 10) : 
    
    print(c , value)

for s , value in enumerate (range(30) , 100) : 
    
    print(s , value)
    
"""    


"""

counries = ['palestine','egypt','jordan','lebanon','syria','france','turkey']

names = ['mohamed','yosef','ahmad','mona','sara','ward','tamer']

for a , b in zip (names , counries) : 
    
    print(a + ' is living in ' + b)
    

"""



"""

from operator import itemgetter

students = [ ('ahmad','egypt', 35) , ('mohamed','palestine',24) , ('sara','lebanon',19) , ('ward','syria',30) , ('tamer','turkey',27)]

x = sorted(students , key = itemgetter(2))

z = sorted(students , key = itemgetter(0))

w = sorted(students , key = itemgetter(1))

d = sorted(students , key = itemgetter(1,2))

print(x)  

print(z)

print(w) 
 
print(d) 

"""


"""
 
from operator import methodcaller 
 
m = ['ahamd' , 'lamia' , 'alaa' , 'mostafa' , 'abed']

q = sorted(m , key = methodcaller ('count' , 'a'))

print (q) 

"""

