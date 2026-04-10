#File Handling Veri Ekleme 


# BAŞA VERİ EKLEME

#    with open("Files/veriEkleme5.txt", "r+", encoding="utf-8") as f:  # 'r+' mode ekleme için kullanılır
#        my_text = f.read()  # Dosyadaki mevcut veriyi oku
#        my_text = "CSharp\n" + my_text   # Yeni veriyi başa ekle 
#        f.seek(0)  # Dosya imlecini başa al
#        f.write(my_text)  # Güncellenmiş veriyi yaz
#        f.seek(0)  # Dosya imlecini başa al
#        print(f.read())  # Güncellenmiş veriyi oku ve yazdır

# ORTALARA VERİ EKLEME

with open("Files/veriEkleme5.txt", "r+", encoding="utf-8") as f:  # 'r+' mode ekleme için kullanılır
    my_list = f.readlines()  # Dosyadaki mevcut verileri satır satır oku
    my_list.insert(2, "C\n")  # Yeni veriyi 3. satıra ekle
    f.seek(0)  # Dosya imlecini başa al
    f.writelines(my_list)  # Güncellenmiş listeyi yaz
    f.seek(0)  # Dosya imlecini başa al
    print(f.read())  # Güncellenmiş veriyi oku ve yazdır