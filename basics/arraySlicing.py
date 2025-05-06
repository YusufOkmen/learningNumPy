import numpy as np

# arr[start:end:step]

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[1:5])
# print(arr[4:])
# print(arr[:4])
# print(arr[-7:-1])
# print(arr[1:5:2])
# print(arr[::2])

arr2D = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr2D[0, 0:3:2]) 
# print(arr2D[0:2, 4])# take rows between 0 and 2. Then selec their index-2 element.
print(arr2D[0:2, 1:4])