for s in range (20) : 
    
    #print (s)
    pass

for m in range (7,20) : 
    
    #print (m)
    pass

for g in range (9,29,2) : 
    
    #print (g)
    pass

w = [(x,y) for x in range (10) for y in range (10)] 

#print (w)  

r = [(v,z) for v in range (3,8,15) for z in range (30,40,5)]

#print (r)

c = [(x,y) for x in range (10) for y in range (10) if x < y ]

#print (c)

u = "supercalifragelisticexplaidaaicious"

for l in range (len(u)) : 
    
    #print (u[l])
    pass

s = " how are you doing yosef "

for l in range (len(s)) : 
    
    #print (s[l])
    pass

s = ""

y = "yosef is my mentor"

for m in range(len(y)):
    
    s = s + y[len(y) - m - 1]
    
    print (s)