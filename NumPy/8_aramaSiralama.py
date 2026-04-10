# Searching and Sorting
import numpy as np

#np.where() | Koşula göre indeks döner
#np.isin() | Eleman başka dizide var mı?
#np.nonzero() | Sıfır olmayanların indekslerini döner
#np.argmax() / np.argmin() | En büyük / en küçük değerin indeksi
#np.searchsorted() | Sıralı diziye öğe yerleştirme konumu
#np.sort() | Sıralı yeni dizi döner
#np.argsort() | Sıralama için gerekli indeksleri döner
#np.ndarray.sort() | Yerinde (in-place) sıralama
#np.lexsort() | Birden fazla anahtarla sıralama (tuple)

arr = np.array([1,0,3,2,5,7,0,19])
arr_sorted = np.array([1,3,5,9,11,13,16,19])

#Where
print("Where: ")
result = np.where(arr%2==1)
print(result) #İndex numarası döner

#İsin 
print("Is in: ")
arr_Isin = np.array([2,3])
result = np.isin(arr,arr_Isin)
print(result)


print("Non zero:")
result = np.nonzero(arr) 
print(result) #İndex numarası döner

#Argmax, Argmin
print("Argmax ve Argmin: ")
print(np.argmax(arr), np.argmin(arr)) #İndex numarası döner

#Search sorted
print("Search Sorted: ")
result = np.searchsorted(arr_sorted, [4,10,12], side="left") # Sıralanmış bir dizide verilen sayıları hangi indexe yerleştirilebilirse onu döner
print(result)

#Sorting
print("Sort: ")
sorted_arr = np.sort(arr) # verilen diziyi sıralar ve yeni bir diziye aktarır // Copy array oluşur // 2 boyutlu dizilerde satıra göre sıralar 
print(sorted_arr) # arr.sort() np kütüphanesinden bağımsız python kodu orjinal arrayi sıralar 

#Argsort
print("Argsort: ")
result = np.argsort(arr) # Sıralama için gerekli indeksleri döner
print(result)

#Lexsort
print("lexsort: ")
names = np.array(["Ahmet", "Mehmet", "Ahmet", "Mehmet"]) 
scores = np.array([100,90,80,70]) # Ahmet->100, Mehmet->90, Ahmet->80 ...
idx = np.lexsort((scores, names)) # Önce names arrayine göre sonra scores arrayine göre sıralar 
print(idx)
print(list(zip(names[idx], scores[idx])))