
"""

a = [1,2,3,6,8,9]

b = (1,6,3,6,9,8,9)

print(a[4])

print(b[6])

print(min(a))

print(max(a))

print(min(b))

print(max(b))

a[5] = 34

print (a)


"""


"""

a = [1,2,3,6,8,9]

b = (1,6,3,6,9,8,9)

c = tuple(a)

print(c)

d = list(b)

print(d)

a = tuple(a)

print (a)

b = list(b)

print(b)

"""



ages = [ ('alya' , 'reineh' ,20) ,('aya' , 'sakhnin' ,24) ,('rawzan' , 'yaffo' ,21) ,('mayar' , 'lod' ,30) ,('salam' , 'arraba' ,28) ,('roza' , 'tamra' ,23) ]

newages = sorted(ages,key = lambda student : student[0])

print(newages)

newages = sorted(ages,key = lambda student : student[1])

print(newages)

newages = sorted(ages,key = lambda student : student[2])

print(newages)

