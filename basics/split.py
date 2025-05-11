import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# Slice the array into three new arrays. If it cannot divide into an integer then it will throw an error.
newArr = np.split(arr, 3)

result = newArr 

# If we want to get a list of arrays even the result is not an integer we must use array_split method.
arr2 = np.array([1, 2, 3, 4, 5, 6, 7])

arr3 = np.array_split(arr2, 3)

result = arr3

# We can access splitted arrays like normal arrays

result = arr3[0]
result = arr3[1]
result = arr3[2]

# splitting 2-D Arrays
# Each splitted array still will be 2D array
arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

arr5 = np.split(arr4, 3)
arr6 = np.split(arr4, 3, axis=1)
arr7 = np.hsplit(arr4, 3)

result = arr5
result = arr6
result = arr7

print(result)