def DecAndConq(length,count):
    if(length < 2):
        return 1
    else:
        return 1 + DecAndConq(length/2,count)

number = 15
print("The minimum cutting for " +str(number) + " is "+ str(DecAndConq(15, 0)))


