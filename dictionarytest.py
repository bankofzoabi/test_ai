


newdictionary = {'usa' : '001' ,'uk' : '0044' ,'egy' : '002' ,'ksa' : '002' ,'uea' : '00971' }

degress = {'ahmad' : 26 , 'soad' : 55 , 'mona' : 42 , 'zakarya' : 53 , 'george' : 36 , 'mostafa' : 36}

weights = {23 : 'bag 1' , 34 : 'bag 2' , 54 : 'bag 3' , 78 : 'bag 4' , 18 : 'bag 5' , 49 : 'bag 6' , 58 : 'bag 7'}
 
e = {3*n : n**5 for n in range (6)}
 
print (e)

degress ['george'] = 27

degress ['soad'] = 75 

newdictionary ['egy'] = 974

weights ['bag 3'] = 54 

print (degress)

print (newdictionary)

print (weights)

print ('usa' in newdictionary )

print ('yosef' in degress)

print (23 in weights) 

print ('bag 1' in weights.values) 

print (55 in degress.values)

print ('002' in newdictionary )


