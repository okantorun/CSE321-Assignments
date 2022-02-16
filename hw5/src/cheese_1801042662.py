def sorting(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j][1]/arr[j][0] < arr[j+1][1]/arr[j+1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def putBox(cheeseTypes,weight):
    i=0
    maxValue=0
    while True:
        if(cheeseTypes[i][0] <= weight):
            maxValue+=cheeseTypes[i][1]
            weight-=cheeseTypes[i][0]
        else:
            maxValue+=cheeseTypes[i][1]*(weight/cheeseTypes[i][0])
            break
        i+=1
    return maxValue

cheeseTypes = [[10,150],[10,80],[10,100],[10,120]]
sorting(cheeseTypes)

print(putBox(cheeseTypes, 10))