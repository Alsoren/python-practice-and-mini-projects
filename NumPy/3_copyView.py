#Copy and View Arrays 

import numpy as np

base_array = np.array([1, 2, 3, 4, 5])

copy_array = base_array.copy()
view_array = base_array.view()

copy_array[0] = 10
view_array[0] = 20

print("Base Array:", base_array)
print("Copy Array:", copy_array) #copy array farklı bir  array gibi çalışır değişiklikler etkilenmez
print("View Array:", view_array) #view array, temel dizinin bir görünümüdür, değişiklikler etkilenir