# Numpy Array Filtering 
import numpy as np


arr = np.array([71,72,73,74,75,76,77,78,79])
filter_arr = []
for item in arr:
    if item > 74:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

new_arr = arr[filter_arr]
print(new_arr)

# Kolay yol

new_arr = arr[(arr>74)]
print(new_arr)

# 3. yol

index = np.where(arr>74)
print(arr[index])