import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.shape)
row_sum = np.mean(arr , axis=1)
print(row_sum)
