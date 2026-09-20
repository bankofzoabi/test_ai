import numpy as np 
import re
a = "the value of pi is {}".format(np.pi) 
#print (a)
b = "{0} and {1}".format("yosef", "mohamed")
#print (b)
c = "{0} is mentor of {1}" .format("yosef","mohamed")
#print(c)
d = "{1} and {0}".format("yosef", "mohamed")
#print(d)
e = "First: {first}. Last: {last}.".format(last="mohamed", first="yosef")
#print(e)
f = "pi = {0:.2f}".format(np.pi)
#print (f)
g = "{:s} mohamed from palestine {:d} years old".format("I am", 20)
h = " {:s} finished {:d} weeks of ai course".format("I am", 2)
#print(g, end= "") 
#print(h)
i = "I" + "{:^150}".format("free palestine") + "I"
#print(i)
j = "I" + "{:^200}".format("egypt mom's world") + "I"
#print (j)
k = "{0:50} ==> {1:100d}".format("mohamed", 56322)
#print(k)
email = re.compile(r'\w+@\w+\.[a-z]{3}')

text = "To email Guide, try guido@python.org or guido@google.com"

#print(email.findall(text))
text = "To email Guido, try guido@python.org or guido@google.com"

email3 = re.compile(r'([\w.]+)@(\w+)\.([a-z]{3})')

#print(email3.findall(text))

text = "To email Guido, try guido@python.org or guido@google.com"

email4 = re.compile(r'(?P<user>[\w.]+)@(?P<domain>\w+)\.(?P<suffix>[a-z]{3})')
match = email4.match('guido@python.org')
print(match.groupdict())
