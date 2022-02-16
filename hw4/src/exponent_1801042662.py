def DivAndConq(num,power):
    
    if (power == 0): 
        return 1
    result = DivAndConq(num, int(power / 2))
    if (int(power % 2) == 0):
        return result * result
    else:
        return result * result * num

def BruteForce(num,power):
    result = 1
    for i in range(power):
        result*=num
    return result

print(DivAndConq(2, 4))
print(BruteForce(2, 4))
