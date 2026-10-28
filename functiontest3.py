
"""

def print_values(**values) : 
    
    print(values)
    
print_values (one = 1 , two = 2)

"""


"""

def print_values(**values) : 
    for key , value in values.items() : 
        print ("{} = {}" .format(key,value))
        
print_values(one = 1 , two = 2 , three = 3 , four = 4 , five = 5)

"""



"""


def greet_me(**kwargs) :
    
    if kwargs is not None :
        
        for key , value in kwargs.items() : 
            print ("%s == %s" %(key,value))
            
greet_me (name = "python")

 
"""
 
 
 


"""
 
def avg_of_two(a,b) : 
    
    print((a+b)/ 2)
    
def avg_of_three(a,b,c) :
    
    print((a+b+c)/3) 
    
var1 = {'a' : 1 , 'b' : 2}

avg_of_two (**var1)

var2 = {'a' : 1 , 'b' : 2 , 'c' : 3}

avg_of_three (**var2) 


"""


"""

def show_details(a,b,*args,**kwargs) : 
    print ("a is" , a)
    print ("b is" ,b)
    print("args is" ,args)
    print ("kwargs is" ,kwargs)

show_details (1,2,3,4,5,6,7,8,9)
print("-------------------")
    
show_details (1,2,3,4,5,6,c = 7,d = 8 , e = 9)
print("-------------------")

"""





def test_args_kwargs(arg1 , arg2 , arg3) : 
    print ("arg1:" ,arg1)
    print ("arg2:" ,arg2)
    print ("arg3:" ,arg3)
    
#first with #args

args = ("two" , 3,5)

test_args_kwargs (*args)


# now with kwargs : 

kwargs = {"arg3" : 3 , "arg2" : "two" , "arg1" : 5}

test_args_kwargs (**kwargs) 