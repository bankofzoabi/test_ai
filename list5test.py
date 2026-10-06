"""

a = [3,3,5,7,4,2,7,9,3,6,7,4]

b = ['s','f','d','a','c','x']

c = sorted (a, reverse = True)

d = sorted (b , reverse = True)

print(c)

print(d)


"""

"""

a = [('At', 85), ('Br', 35), ('Cl', 17), ('F', 9), ('I', 53)] 

b = sorted (a , key = lambda c : c[1])

c = sorted (a , key = lambda c : c[0])



print(b)
print(c)

"""


"""

x = [('yosef','egypt',26 ,19 ) , ('mohamed','palestine',24 ,20 ) , ('khaled','jordan',15 ,21 ) ,('mona','lebanon',12 ,30 )]

y = sorted (x, key = lambda c : c[0])

z = sorted (x, key = lambda c : c[1])

u = sorted (x, key = lambda c : c[2])

v = sorted (x, key = lambda c : c[3])

print(y)
print(z)
print(u)
print(v)

r = sorted(x , reverse = True  , key = lambda e : e[2])

print (r)

"""

"""

a  = 'i=love=python=it=is=an=easy=programing=software'

b = a.split(sep = '=')

print(b)

c = '55,66,3,4,554,3,4,54,34,24'

s =  c.split(sep = ',' , maxsplit = 5 )

print (s)

"""


"""

f = [4,54,3,4,543,4,45,22,6,654,56,7,765,33]

h = (96 in f )

print (h)

"""


a = ['a','d','r','t','y','w']

b = ['aa','dd','rr','tt','yy','ww']

b.extend (a)

print(b)
