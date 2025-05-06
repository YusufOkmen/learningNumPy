import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# print(type(arr))

arrTuple = np.array((1, 2, 3, 4, 5))

# print(arrTuple)


#---0-D Arrays---
array0D = np.array(42)

# print(array0D)

#---1-D Arrays---
array1D = np.array([1, 2, 3, 4, 5])

# print(array1D)

#---2-D Arrays---#Matrix
array2D = np.array([[1, 2, 3], [4, 5, 6]])

# print(array2D)

#---3-D Arrays---
array3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(array3D)

# Dimensions
# print(array0D.ndim)
# print(array1D.ndim)
# print(array2D.ndim)
# print(array3D.ndim)

newArr = np.array([1, 2, 3, 4, 5], ndmin=5)# Create a array with 5 dimensions.

# print(newArr, newArr.ndim)

