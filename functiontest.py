
"""

def find_avg(a,b) : 
    average = (a+b) / 2
    print("average is" ,average)
    
find_avg(2,3)

"""


"""

def find_avg (*numbers) :
    sum = 0 
    for i in numbers :
        sum += i
    print("average is", sum / len(numbers))
    print(numbers)
    
find_avg (2,3)

find_avg (2,3,4)

find_avg (1,2,3,4,5,6,7,8,9,10)



"""



"""

def avg_of_two(a,b) : 
    
    print((a+b)/ 2)

def avg_of_three(a,b,c) :
    
    print((a+b+c)/3) 
    
var1 = (1,2)

avg_of_two (*var1)

var2 = (1,2,3) 

avg_of_three (*var2) 

"""





def test_var_args(f_arg , *args) : 
    print("first normal arg:" , f_arg)
    for arg in args :
        print("another arg through *argv :" , arg)
        
test_var_args('jumana' , 'mohamed' , 'sara', 'fares')



        