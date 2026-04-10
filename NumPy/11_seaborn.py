import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

data = [1,2,2,3,3,3,4,4,4,5,5,5,5]
data1 = [30,35,40,45,50,55,60,65,70,75,80,85,90]
notes = [44,35,67,55,47,87,65,56,87,66,23,90,64,62,59]

sb.displot(data) #Histograph graph // sb.histplot(data)
sb.displot(data, kind="kde") #Kernal density estimation // yumuşak çizgili sb.kdeplot(data)
sb.displot(data, kind="ecdf") #Empirical cumulative distribution function 
plt.show()