# Splitting Array 
import numpy as np

#np.split() -- Eşit veya özel bölme 
#np.array_split() -- Eşit olmasa bile bölmeye izin verir
#np.hsplit() -- stünlara (horizontal) göre bölme
#np.vsplit() -- satırlara (vertical) göre bölme
#np.dsplit() -- Derinlipe göre bölme

# 1 Boyutta Vertical
x_1D = np.array([1,2,3,4,5,6])    #np.vsplit()
result = np.split(x_1D, 3)
for item in result:
    print(item, end=" ")
    print()
print("*"*18)

# 2 Boyutta Horizontal
x_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])   
result = np.hsplit(x_2D, 3)   #np.array_split(x_2D, 3, axis= 1)
for item in result:
    print(item, end=" ")
    print()
print("*"*18)