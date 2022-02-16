def polynomial(n:int,x:int):
    
   
    temp = 1
    result = 0
    
    for i in range(1,n+1):
        temp = temp * x
        result = result + i*temp
        
    return result


print(polynomial(2, 4))