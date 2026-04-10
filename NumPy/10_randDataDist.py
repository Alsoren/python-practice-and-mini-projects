#Randome Data Distribution and Randome Permutations
import numpy as np
from numpy import random

arr = np.array([2,4,6,8,10])
result = random.choice(arr,p=[0.2,0.3,0.4,0.1,0.0],size=10) # p sayının seçilme ihtimalini verir size kaç sayı seçileceğini iki boyut da yapılabili
print(result)

#Permutation 
new_arr = random.permutation(arr) # Copy arraya orjinal arrayi karıştırıp verir (permitasyon)
print(f"Orginal array: {arr}")
print(f"New array: {new_arr}")

#Shuffle
# random.shuffle(arr) orjinal arrayin sıralamasını değiştirir 