# Array Concatenation : Dizi Birleştirme
import numpy as np

#np.concatenate() | Dizi birleştirme (ekseni belirleyerek)
#np.stack() | Yeni bir eksenle dizileri üst üste koyma
#np.hstack() | Yatay (horizontal) birleştirme
#np.vstack() | Dikey (vertical) birleştirme
#np.dstack() | Derinlik (depth) ekseniyle birleştirme

x = np.array([1,7,4])
y = np.array([19,3,10])

x_2D = np.array([[2,11,5],[3,14,17]])
y_2D = np.array([[18,24,21],[6,0,21]])

result = np.concatenate((x_2D,y_2D),axis=1)


print(result)