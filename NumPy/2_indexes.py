import numpy as np

arr1D = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) # index 0 = 1, index 1 = 2, index 2 = 3, index 3 = 4, index 4 = 5
print(arr1D[1:6:2]) # 1.indexten başlar 6. indexe kadar gider ve 2'şer atlayarak alır

arr2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2D[1, 2]) # 1. satır 2. sütundaki elemanı alır
print(arr2D[:,0:2]) # 0. ve 1. sütunlardaki elemanları alır