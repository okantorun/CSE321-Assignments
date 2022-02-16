def findPairs(arr, n):
	arr2 = [0]*n
	return _findPairs(arr, arr2 ,0, n - 1)


def _findPairs(arr, arr2, left, right):

	rop_count = 0

	if left < right:

		mid = (left + right)//2

		rop_count =rop_count+ _findPairs(arr, arr2,
								left, mid)

		rop_count =rop_count+ _findPairs(arr, arr2,
								mid + 1, right)

		rop_count =rop_count+ merge(arr, arr2,
								left, mid, right)
	return rop_count

def merge(arr, temp_arr, left, mid, right):


	i = left	
	j = mid + 1


	k = left	
	rop_count = 0


	while i <= mid and j <= right:

		if arr[i] <= arr[j]:
			temp_arr[k] = arr[i]
			k += 1
			i += 1
		else:

			temp_arr[k] = arr[j]
			rop_count =rop_count+ (mid-i + 1)
			k += 1
			j += 1

	while i <= mid:
		temp_arr[k] = arr[i]
		k += 1
		i += 1

	while j <= right:
		temp_arr[k] = arr[j]
		k += 1
		j += 1

	for n in range(left, right + 1):
		arr[n] = temp_arr[n]
		
	return rop_count


informations = [3, 17, 8, 7, 10]
n = len(informations)
result = findPairs(informations, n)
print("The number of reverse-ordered pairs is ", result ," in informations")
