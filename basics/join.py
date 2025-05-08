import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Even though it unites the two array the result still is a 1 dimensional
arr3 = np.concatenate((arr1, arr2))

result = arr3

arr4 = np.array([
    [1, 2, 3],
    [4, 5, 6]
                ])

arr5 = np.array([
    [7, 8, 9],# axis 0
    [10 ,11 ,12] #axis 0
                ])

# Gathering colums
arr6 = np.concatenate((arr4, arr5), axis=1)

result = arr6

# Stacking

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
arr7 = np.stack((arr1, arr2), axis=1)

# Takes colums to the row. Extending the row sideways. Same dimension.Adds columns side by side. ROW-WISE EXPANSION
arr8 = np.hstack((arr1, arr2))

#Adds rows on top of each other. Like adding new rows. COLUMN-WISE STACKING
arr9 = np.vstack((arr1, arr2))

arr10 = np.dstack((arr1, arr2))

result = arr7
result = arr8
result = arr9
result = arr10

print(result)