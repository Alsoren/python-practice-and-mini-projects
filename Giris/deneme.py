def numToStr(num1):
    list1 = ["bin", "iki bin", "üç bin", "dört bin", "beş bin", "altı bin", "yedi bin", "sekiz bin", "dokuz bin"]
    list2 = ["", " yüz", " iki yüz", " üç yüz", " dört yüz", " beş yüz", " altı yüz", " yedi yüz", " sekiz yüz", " dokuz yüz"]
    list3 = ["", " on", " yirmi", " otuz", " kırk", " elli", " altmış", " yetmiş", " seksen", " doksan"]
    list4 = ["", " bir", " iki", " üç", " dört", " beş", " altı", " yetmiş", " seksen", " doksan"]
    thousends = int(num1 / 1000)
    houndreds = int((num1 / 100) - (thousends * 10))
    tens = int((num1 / 10) - (thousends * 100) - (houndreds * 10))
    ones = int(num1 - (thousends * 1000) - (houndreds * 100) - (tens * 10))

    print(list1[thousends-1] + list2[houndreds] + list3[tens] + list4[ones])



num1 = int(input("Please enter a 4 digit number: "))
if(num1 / 1000 < 10 and num1 / 1000 >= 1):
    numToStr(num1)
else:
    print("düzgün sayı yaz sikmim")