a = '35326356'
b = a.isdigit()
#print (b)
c = "YOSEF MY MENTOR"
e = c.isupper()
#print(e)
f = "yosef is my MENTOR"
h = f.islower()
#print (h)
r = f.istitle()
#print(r)
d = "yosef my mentor"
x = d.endswith("tor")
#print (x)
y = d.startswith("y")
#print (y)
t = '###'.join(('yosef','my','mentor'))
#print (t)
g = '\n'.join(('yosef', 'my','mentor'))
#print(g)
l = ' 3>  '.join(('yosef','my','mentor'))
#print(l)
import numpy as np
s = ' '.join([str(i) for i in np.randon.randint(10,size=100)])
print(s)