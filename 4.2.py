import random 
def quicksort(arr):
	if len(arr) < 2:
		return arr
	else:
		n = random.randint(1,len(arr))
		pivot = arr[n-1]
		arr.pop(n-1)
		less = [i for i in arr[:] if i <= pivot ]
		greater = [i for i in arr[:] if i > pivot]
		return quicksort(less) + [pivot] + quicksort(greater)
		
print(quicksort([9,8,10,3,3,4,2,1,1]))
