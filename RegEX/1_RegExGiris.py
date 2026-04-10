# Regular Expressions (Regex) in Python // Metinsel ifadeyi koşullandırmalar
import re 
text = "The rain in Turkey"

# Search METHODU

result = re.search(r"rain", text)  # 'r' raw string, 'search' metni arar
if result:
    print("Match found")  #Varsa match found döner
else:
    print("No match found") #yoksa no match found döner

# Findall METHODU
result = re.findall("rain", text)  # 'findall' metinde "rain" kelimesini arar ve liste olarak döner bulursa
print("Findall result:", result)

# Meta CHARACTERS
# []
result = re.findall(r"[a-m]", text)  # 'findall' metninde a-m aralığındaki harfleri arar ve liste olarak döner 
print("Findall result:", result)

# \d
result = re.findall(r"\d", text)  # 'findall' metninde rakamları arar ve liste olarak döner // kullanılan 'r' raw string yani kaçış dizilerini işler \ gibi karakterleri normal karaktermiş gibi okur aksi taktirde syntax error alınır
print("Findall result:", result)

# . (nokta)
result = re.findall(r"r..n", text)  # 'findall' noktaları boş bırakılan yerlerde herhangi bir karakter olan string arar
print("Findall result:", result)

# ^ (başlangıç)
result = re.findall(r"^Th", text)  # 'findall' metninin başlangıcında "Th" bulunuyor mu
print("Findall result:", result)

# $ (bitiş)
result = re.findall(r"Turkey$", text)  # 'findall' metninin sonunda "Turkey" bulunuyor mu
print("Findall result:", result)
