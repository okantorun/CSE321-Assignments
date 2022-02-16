def seperation(arr, l, r):
     
    x = arr[r]
    i = l
    for j in range(l, r):
         
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
             
    arr[i], arr[r] = arr[r], arr[i]
    return i
 
def meaningful_results(arr, l, r, k):
 

    if (k > 0 and k <= r - l + 1):
 
        index = seperation(arr, l, r)

        if (index - l == k - 1):
            return arr[index]
 
        if (index - l > k - 1):
            return meaningful_results(arr, l, index - 1, k)

        return meaningful_results(arr, index + 1, r,
                                        k - index + l - 1)
    
arr = [ 15, 6, 3, 10, 4, 1 ]
n = len(arr)
k = 3
print("The success rate of the first meaningful_results {}th experiment is {}".format(k,meaningful_results(arr,0,n-1,k)))