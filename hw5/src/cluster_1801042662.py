def cluster(branches):
    temp = branches[0]
    maxSum = branches[0]
    for i in range(1, len(branches)):
        temp = temp + branches[i]
        temp = max(branches[i], temp)
        maxSum = max(maxSum, temp)

    return maxSum

branches = [3,-5,2,11,-8,9,-5]
print("Maximum profit is:"+str(cluster(branches)))