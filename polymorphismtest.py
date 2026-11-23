

class summation :
    def sum(self , a = None , b = None , c = None) :
        if a != None and b!= None and c!= None :
            s = a+b+c
            print("total = " , s)
        elif a != None and b != None :
            s = a+b 
            print("total = " , s)
        else : 
            print("total = " , a)
            
            
sum1 = summation()
sum1.sum(9,4,7)







class summation : 
    def sum (datatype, *args) : 
        if datatype == 'int' : 
            count = 0 
        if datatype == 'str' : 
            count = ''
        
        for x in args : 
            count = count + x 
            print("total = " , count)
            
sum1 = summation 
sum1.sum('int' , 1, 2, 7, 9, 4, 3)

sum2 = summation 
sum2.sum('str' , 'yosef' , 'mohamed')