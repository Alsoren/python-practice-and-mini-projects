# File Handling Writing
fruits = ["strawberry\n", "banana\n", "apple\n", "orange\n", "kiwi\n", "mango\n"]
with open("Files/dosya.txt", "w", encoding="utf-8") as f:  # Kullanıldığında dosyadaki her şey silinir
    f.writelines(fruits)

with open("Files/dosya.txt", "r+", encoding="utf-8") as f: 
    print(f.read())
    f.seek(0)
    f.write("<yeni_meyve>\n")  # var olan metin üzerine yazılır