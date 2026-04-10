# NumPy Array Methods
# reshape 

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr = arr.reshape((3, 4)) # array tekrardan boyutlanır parametrelerden birisi -1 girilirse şekillendirme otomatik yapılır

print(arr.shape) # (3, 4)
print(arr) # view_array

new_arr = arr.flatten() # arrayi vektörel hale getirir // Copy array döndürür
print(new_arr)

new_arr2 = arr.ravel() # arrayi vektörel hale getirir // View array döndürür
print(new_arr.base) # none döndürmesi onun bir View array olduğunun kanıtıdır

# Flip - FlipUP - FlipLR

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
print("-"*18)
print(np.flip(arr2,axis=0)) # Yukaru aşağıya = print(np.flipud(arr2)
print("-"*18)
print(np.flip(arr2,axis=1)) # sağ sola = print(np.fliplr(arr2)
print("-"*18)
print(arr2.T) # satır sütuna değişim