#Try / Except

try:
    x = int(input("Enter a number: "))
    print(x)
except:
    print("Invalid input")
try:
    a = 10 / 0
except:
    print("There is an error")
try:
    x = int("hello")
except ValueError:
    print("Value error")
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
try:
    x = int(input("Enter number: "))
    result = 10 / x
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
try:
    x = int(input("Enter number: "))
except ValueError:
    print("Invalid")
else:
    print("Correct input:", x)
try:
    x = int(input("Enter number: "))
except ValueError:
    print("Invalid")
finally:
    print("Finished")


#Datetime — Date

from datetime import date
now = date.today()
print(now)
from datetime import date
a = date(1982, 2, 2)
print(a)
from datetime import date
now = date.today()
a = date(1982, 2, 2)
z = now - a
print(z)
print(z.days)
from datetime import date
a = date(1982, 2, 2)
b = date(2011, 3, 15)
z = b - a
print(z)


#strftime

from datetime import date
now = date.today()
a = now.strftime("%m-%d-%y")
print(a)
from datetime import date
now = date.today()
a = now.strftime("%d %b %Y")
print(a)
from datetime import date
now = date.today()
a = now.strftime("%d %b %Y is a %A")
print(a)


#Datetime — Date + Time

from datetime import datetime
a = datetime(
    year=2011,
    month=3,
    day=15,
    hour=13,
    minute=15,
    second=9
)
print(a)
from datetime import datetime
now = datetime.now()
print(now)
from datetime import datetime
a = datetime(
    year=2011,
    month=3,
    day=15,
    hour=13,
    minute=15,
    second=9
)
b = datetime(
    year=1982,
    month=2,
    day=2,
    hour=18,
    minute=43,
    second=12
)
print(a)
print(b)
print(a - b)



#Time

import time
t = time.gmtime()
print(t)
import time
print(time.time())
import time
print("Start")
time.sleep(3)
print("Finish")



#5Wait Function

import time
def wait(x):
    t0 = time.time()
    while time.time() - t0 < x:
        time.sleep(1)
    return x
print("start")
wait(3)
print("finish")

