arr = [23,12,34,56,1,34,23,11,13,4,5]
print('Unsorted array', arr)

l = len(arr)
for i in range(l):
	low = i
	for j in range(i+1, l):
		if arr[low] > arr[j]:
			low = j

	arr[i], arr[low] = arr[low], arr[i] 
	
print('Sorted array',arr)	
