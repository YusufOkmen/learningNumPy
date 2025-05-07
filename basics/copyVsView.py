import numpy as np


arr = np.array([1, 2, 3 ,4, 5])

#copy
newArr = arr.copy()
newArr[0] = 9

# print(arr)
# print(newArr)

newArr1 = arr.view()
newArr1[1] = 7

print(arr)
print(newArr1)

# Every NumPy array has the attribute base that returns None if the array owns the data. Otherwise, the base attribute refers to the original object

theArr = np.array([1, 2, 3, 4])

xArr = theArr.copy()
yArr = theArr.view()

print(xArr.base)
print(yArr.base)
