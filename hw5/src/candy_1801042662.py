def candyShop(price, size):
    val = [0 for x in range(size+1)]
    val[0] = 0
    for i in range(1, size+1):
        max_val = -99
        for j in range(i):
             max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val
    return val[size]

price = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(price)
print("Maximum Obtainable Value is: " + str(candyShop(price, size)))
