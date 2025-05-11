import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])

# What is the index of value "3" in arr1
arr2 = np.where(arr1 == 3)
arr3 = np.where(arr1 == 5)
# Find the indexes where the values are even
arr4 = np.where(arr1 % 2 == 0)
# Find the indexes where the valeus are odd
arr5 = np.where(arr1 % 2 == 1)

result = arr2
result = arr3
result = arr4
result = arr5

# Search Sorted
# Returns the index where the specified value would be inserted to maintain the search order.
arr6 = np.array([1, 2, 3, 4, 6, 8, 9])

arr7 = np.searchsorted(arr6, 7)
# Start searching from right
arr8 = np.searchsorted(arr6, 7, side='right')

result = arr7
result = arr8

# Searching Multiple Values
arr9 = np.array([1, 3, 5, 7, 8])

arr10 = np.searchsorted(arr9, [2, 4 ,6])

result = arr10

print(result)