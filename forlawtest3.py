students = ['ahmad' , 'mona' , 'ramy' , 'rema']

for i,a in enumerate (students):
    #print (i)
    #print (a)
    pass

students = ['ahmad' , 'mona' , 'ramy' , 'rema']

for i,a in enumerate (students):
    #print (a , i)
    pass

students = ['samy' , 'mona' , 'ramy' , 'rema']
grades = [25 , 33 , 50 , 78]
for i,a in zip (students , grades): 
    #print (' students ' + i + ' got ' + str(a) + ' degree ')
    pass

a = [i for i in range (20) if i %3 == 0]
#print (a)

b = [i for i in range(20) if i %4 == 0 and i %2 == 0]
#print(b)

c = [i for i in range (100) if i %3 == 0 and i %5 == 0]
#print (c)

d = [i**2 for i in range(20)] 
#print (d)

e = [i%4 for i in range(40)]
#print(e)

f = [i**2 for i in range (30) if i %3 == 0 and i %2 == 0]
#print (f)

g = [(i**3,j+5) for i in range (6) for j in range (9)]
#print (g)

for h in range (15) : 
    #print (h)
    pass
else : 
    #print ('done')
    pass

for i in range (0,41,3) :
    #print (i)
    pass

else : 
    #print ('donee')
    pass

#print(sum([k for k in range (20)]))

#print(sum([1/k for k in range (1,11)]))

#print(sum([3*(k**2) for k in range (150)]))

a = [3*x for x in [y**2 for y in range (10)]]
#print (a)

b = [ 10*x for x in [y**4 for y in range (20)]]
print (b)