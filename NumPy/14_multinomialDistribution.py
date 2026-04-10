#Multinomial, Exponential Distribution
import matplotlib.pyplot as plt
import seaborn as sb
from numpy import random
#Multinomial Distribution
data = random.multinomial(n=10.0, pvals=[0.2,0.3,0.5], size=7) # 7 farklı şehirde 10 farklı kişiye 3 kategoriden seçim sunuluyor
print(data)
#Exponential Distribution
data = random.exponential(scale=1, size=1000)
sb.histplot(data, bins=30, kde=True) # zaman uzadıkça bir kişinin atmye uğrama olasılığı o kadar azalıyor
plt.title("Exponential Distribution (Üstel Dağılım Lambda=2)")
plt.xlabel("Süre")
plt.ylabel("Frekans")
plt.show()