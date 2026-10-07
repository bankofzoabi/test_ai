#y = list(map(lambda x: x ** 3, range(12)))



"""

y = [x ** 3 for x in range(12)]

a = [x ** 4 for x in range(25)]

b = [x ** 0.5 for x in range(10)]

c = [x ** 3 for x in range(12,15)]

d = [x ** 3 for x in range(10,50,2)]

print(y)
print(b)
print(a)
print(c)
print(d)


"""


"""

a = list(map(lambda x: x ** 3, range(12)))

b = list(map(lambda x: x ** 3, range(11)))

c = list(map(lambda x: 10* x ** 3, range(11)))

d = list(map(lambda x: 10* x , range(101)))

e = list(map(lambda x: 10*x ** 2, range(101)))

f = list(map(lambda x: 10*x ** 0.5, range(50,101)))

g =list(map(lambda x: x ** 0.5, range(50,101)))

h = list(map(lambda x: x+2, range(50,101,3)))
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)


"""

"""

aa = [-5+ i*0.5 for i in range(20)]

bb = [-5+ i**0.5 for i in range(20)]

print(aa)
print(bb)

"""

"""

f = [(x,y) for x in [1,2,3] for y in [4,6,8]]

print(f)

"""

"""

career = [(sheinclub, shoesclub, shifttime) for sheinclub in ['hanan', 'lama', 'alaa'] for shoesclub in ['adan', 'reem', 'sara'] for shifttime in ['morning', 'med', 'night']]

print(career)


"""

"""

m = [[3 for i in range(5)] for j in range(7)]

print (m)

"""