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


arr = []
print("Unsorted array", arr)
sorted_arr = bubble_sort(arr)
print("Sorted array", sorted_arr)
