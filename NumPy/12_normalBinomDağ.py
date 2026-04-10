# Normal (Gaussian), Binomial Distribution
import matplotlib.pyplot as plt
import seaborn as sb
from numpy import random

#Normal Dağılımı (Gaussian)
arr = random.normal(loc=0,scale=1,size=1000) #loc sayıların ortalaması / scale standart sapma / size üretilen sayı miktarı

sb.displot(arr, kind="kde")
plt.title("Normal Dağılımı")
plt.show()

#Binomial Dağılım
arr = random.binomial(n=10, p=0.5, size=1000) #n kişi başı deneme / p ihtimal // kişi başı başarı sayısını guruplandırır true false
sb.displot(arr)
plt.title("Binom Dağılımı")
plt.show()