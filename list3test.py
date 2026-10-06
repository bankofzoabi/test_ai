

a = [1,3,4,2,66,77,3,8,86,4,5,55,9,76,52,21]

"""

print (a[5:])

print (a[10:])

print (a[3:])

print (a[15:])



a[0] = 21
a[1] = 32
a[2] = 40
a[3] = 29
a[8] = 36
a[15] = 91
a[6] = 76

print (a)



a[2:5] = []
a[:10] = []
a[9:11] = []
a[:-4] = []
a[10:] = []


print(a)

"""

"""
t = ['d','y','j']

s = [5,3,7,8,2,4,9]

r = [True,False,9.4,'k']

x = [t,s,r]

z = [t,'s','r']

print(x)
print(z)
print(x[0][0])
print(x[0][1])
print(x[0][2])
print(x[1][2])
print(x[1:2][0:9])

"""

"""

del a[5]
del a[:3]
del a[0:10]
del a[:-4]
del a [:-8]

print (a)

"""

a.remove(21)
a.remove(52)


print (a)