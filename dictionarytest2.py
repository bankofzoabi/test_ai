


newdictionary = {'usa' : '001' ,'uk' : '0044' ,'egy' : '002' ,'ksa' : '002' ,'uea' : '00971' }

degress = {'ahmad' : 26 , 'soad' : 55 , 'mona' : 42 , 'zakarya' : 53 , 'george' : 36 , 'mostafa' : 36}

weights = {23 : 'bag 1' , 34 : 'bag 2' , 54 : 'bag 3' , 78 : 'bag 4' , 18 : 'bag 5' , 49 : 'bag 6' , 58 : 'bag 7'}
 
a = degress.get('mona')

"""

print (a)

b = degress.get('soad' , 35)

print (b) 

degress ['samer'] = 81

degress ['atef'] = 29 

weights ['bag 10'] = 65 

print (degress)

print (weights)

del (degress['ahmad'])

print (degress)

degress.clear 

degress ['yosef'] = 100

print (degress)

del (degress)

"""

"""

newdegress = degress.copy()

newdegress ['ahmad'] = 99

print(degress)

print(newdegress)

"""





set1 = {'a' , 'b' , 'c' , 'd'}

dec = dict.fromkeys(set1)

print(dec)

dec ['a'] = 50

dec ['b'] = 100

dec ['c'] = 150

dec ['d'] = 200

print (dec)