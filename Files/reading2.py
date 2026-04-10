#File Handling Reading and Truncate
with open("Files/dosya.txt", "r+", encoding="utf-8") as f: #Reading yaparken dosya açma ve kapama aynı anda yapılır doğru kullanım böyledir
    print(f.read(10))
    print(f.tell())
    f.truncate(5)  # dosyanın boyutunu 5 byte'a düşür yani ilk 5 byte'ı saklar 