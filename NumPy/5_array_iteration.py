import numpy as np

# 1D array iteration
array1D = np.array([1,2,3,4,5,6,7,8,9])
for item in array1D:
    print(item, end=" ")
print()
print("*"*18)

# 2D array iteration
array2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
for row in array2D:
    for column in row:
        print(column, end=" ")
    print()
print("*"*18)

# 3D array iteration
array3D = np.array([
                    [[1,2,3],
                     [4,5,6]],
                    [[7,8,9],
                     [10,11,12]],
                    [[13,14,15],
                     [16,17,18]]
                    ])
for item in array3D:#                       for item in array3D:
    for row in item:#                           for row in item:
        for column in row:#                         print(*row)
            print(column, end=" ") # ---->      print("-"*18)       sonuç aynı olacaktır
        print()#
    print("-"*18)#

# Tür değişimi:
print("Tür değişimi:")
for item in np.nditer(array1D, flags=["buffered"], op_dtypes=['S']):
    print(item)
print("*"*18)

#Dilimleme işlemleri
print("Dilimleme işlemleri: ")
for item in np.nditer(array2D[:,0:2]):
    print(item)
print("*"*18)

#İndex and Value
print("İndex and Value: ")
for array1D_index, array1D_value in np.ndenumerate(array1D):
    print(array1D_index, array1D_value)