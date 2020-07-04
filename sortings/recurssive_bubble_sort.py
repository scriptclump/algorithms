def bubble_sort(arr):
    for i, val in enumerate(arr): 
        try: 
            if arr[i+1] < val: 
                arr[i] = arr[i+1] 
                arr[i+1] = val 
                bubble_sort(arr) 
        except IndexError: 
            pass
    return arr


arr = [12,11,44,23,55,1,4,54]
print("Unsorted array", arr)
sorted_arr = bubble_sort(arr)
print("Sorted array", sorted_arr)
