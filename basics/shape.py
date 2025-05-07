import numpy as np

arr = np.array([[1, 2 ,3], [4, 5, 6]])

# array arr has 2 dimensions. First dimension has 2 elements and the second one has 3 elements.
# print(arr.shape)

#Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:
arr1 = np.array([1, 2, 3 ,4], ndmin=5)

# print(arr1)
# print(arr1.shape)

# Reshaping  arrays
# We can add or remove dimensions form an array or change number of elements in each dimensions.
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

arr3 = arr2.reshape(4, 3)

arr4 = arr2.reshape(2, 3, 2)

# print(arr2)
# print(arr3)
# print(arr4)
# print(arr2.base)
# print(arr3.base)

arr5 = np.array([1, 2,3 ,4 ,5 ,6, 7, 8])

# NumPy will calculate the last number for us
newArr = arr5.reshape(2, 2, -1)

# print(arr5)
# print(newArr)

# Flattening the array

arr6 = np.array([[1, 2, 3], [4, 5, 6]])

arr7 = arr6.reshape(-1)

print(arr6)
print(arr7)