import numpy as np

arrInt = np.array([1, 2, 3, 4, 5])
arrStr = np.array(['Hello', 'Goodbye'])

# print(arrInt.dtype)
# print(arrStr.dtype)

newArr = np.array([1, 2, 3, 4, 5], dtype="S")

arr2 = np.array([1, 2, 3, 4], dtype="i4")

# arr3 = np.array(["a", "2", "3"], dtype="i")

# print(newArr.dtype)
# print(arr2.dtype)
# print(arr3.dtype)

arr4 = np.array([1.1, 2.1, 3.1])

arr5 = arr4.astype("i")


# print(arr4.dtype)
# print(arr5)
# print(arr5.dtype)

arr6 = np.array([1, 0 ,3])

arr7 = arr6.astype("bool")

print(arr6)
print(arr6.dtype)
print(arr7)
print(arr7.dtype)