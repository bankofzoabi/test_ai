import random as rn

a = rn.random()

#print(a)

b = rn.randint (1,20)

#print(b)

c = rn.uniform (1,20)

#print(c)

d = rn.randrange(150)

#print(d)

e = rn.randrange (256)

#print (e)

f = rn.randrange (0,24,2)

#print (f)

h = rn.choice (['a','b','c'])

#print (h)

i = rn.choice ('sweet home alabama')

#print (i)

g = rn.sample(range(200) ,10)

#print (g)
 
items = [1,2,3,4,5,6]

rn.shuffle (items)

print (items)
