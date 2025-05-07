import numpy as np

# it will go trough each element one by one
arr1 = np.array([1, 2, 3, 4, 5])

for nums in arr1:
    print(nums)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])

for nums in arr2:
    print(nums)

# If we iterate on a n-D array it will go through n-1th dimension one by one.

# to iterate the actual values, the scalars, we have to iterate arrays in each dimension. 
for arrays in arr2:
    for nums in arrays:
        print(nums)

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for firstArray in arr3:
    for secondArray in firstArray:
        for nums in secondArray:
            print(nums)

# But it is not always okay to type n for loops so there is a function called nditer

for nums in np.nditer(arr3):
    print(nums) 

# NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].

arr4 = np.array([1, 2, 3, 4, 5])

# In here flags=["buffered"] is a space to execute the action. In other words take the elements of arr4 and iterate through them as string in a space called buffered.

for nums in np.nditer(arr4, flags=["buffered"], op_dtypes=["S"]):
    print(nums)

# Iterating with different step size

for nums in np.nditer(arr2[:,::2]):
    print(nums)

# Enumerated iteration using ndenumerate

for idx, nums in np.ndenumerate(arr1):
    print(idx, nums)

for idx, nums in np.ndenumerate(arr2):
    print(idx, nums)