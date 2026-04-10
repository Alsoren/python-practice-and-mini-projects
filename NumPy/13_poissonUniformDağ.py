#Poisson, Uniform, Logistic Distribution
import matplotlib.pyplot as plt
import seaborn as sb
from numpy import random

#Poisson Dağılımı (Similasyon - Simüle etmek)
data = random.poisson(lam=2, size=1000)#bir restoranta dkda 2 müşteri gririyor 1000dkya simüle etmek // 300dk boyunca her dk 2 müşteri girmiştir vs
sb.displot(data)
plt.title("Poisson Dagılımı")
plt.show()

#Uniform Dağılım (Bir zarın 6 yüzü)
data = random.uniform(low=1, high=6, size=1000) #zar atıldığında 6 yüzün de gelme ihtimali eşittir
sb.displot(data)
plt.title("Uniform Dagılımı")
plt.show()

#Ayrık Uniform Dağılım (Bir zarın 6 yüzü)
data = random.choice([1,2,3,4,5,6], size=1000)
sb.displot(data)
plt.title(" Ayrık Uniform Dagılımı")
plt.show()

# **Logistic Dağılım (machine lerning)
data = random.logistic(loc = 0, scale=1, size=1000)#değerler Normal ile aynı fakat bunda scale*pi/kök(3) standart sapmayı verir // çan eğrisi verir fakat uç değerlerde artma olur 
sb.histplot(data, kde=True)
plt.title("Logistic Dagılımı")
plt.show()