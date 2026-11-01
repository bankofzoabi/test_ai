


"""

f = open ('D:\\1\\.txt','w')

f.write ('yosef is the best mentor')

f.close()

"""



"""

f = open ('D:\\1\\5.txt','a')
f.write ('\ni love python')
f.write ('\nhey AI')
f.write ('\nhello python')
f.close()

"""




"""

f = open ('D:\\1\\.txt','a')

f.write ('yosef is the best mentor')
f.write ('\n1')
f.write ('\n2')
f.write ('\n3')
f.write ('\n4')
f.write ('\n5')


f.close()

"""




"""

f = open ('D:\\1\\5.txt','r')

for a in f :
    print(a)

f.close ()



f = open ('D:\\1\\.txt','r')

for a in f :
    print(a)

f.close ()

"""





"""

outfile = open('D:\\1\\5.csv','w')

outfile.write('a')

outfile.close()



aa = open('D:\\1\\file.csv','w')

aa.write('newline')

aa.close()

"""



"""

outfile = open('D:\\1\\5.xls','w')

outfile.write('a')

outfile.close()

"""



"""

outfile = open('D:\\1\\5.xls','r')

outfile.write('a')

outfile.close()

"""




"""

import os 

a = os.getcwd

print(a)

"""




"""

import os 

os.makedirs('D:\\1\\00' , exist_ok = True)

os.makedirs('D:\\1\\00' , exist_ok = False)

"""




"""

import os 

a = os.path.exists ('D:\\1\\00')

print(a)

c = os.path.exists ('D:\\1\\0.txt') 

print (c)

b = os.path.exists ('D:\\1\\002')

print (b)

"""


"""

import os 

d = os.path.exists ('D:\\1\\5.xls')

print(d)

"""





import shutil as sh 

sh.copyfile ('D:\\1\\1.txt' , 'D:\\1\\00\\0.txt')

#sh.copytree ('D:\\1\\00' , 'D:\\1\\33')

#sh.move ('D:\\1\\1.txt' , 'D:\\1\\33\\55.txt')

