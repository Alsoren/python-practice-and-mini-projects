# Regular Expressions (Regex) in Python
import re

# * (sıfır veya daha fazla) karakter bulunabilir 
text = "Say hello to my little friend"
text2 = "Hello my telephone number is 123-456-7890 an my age is 32"
result = re.findall(r"l.*r", text)  # 'findall' metninde "l" harfinden sonra gelen sıfır veya daha fazla karakteri arar
if result:
    print("Findall result:", result)  
else:
    print("No match found")  

result = re.findall(r"Say*r", text)  # 'findall' metninde "Say" harfinden sonra gelen sıfır veya daha fazla karakteri arar
if result:
    print("Findall result:", result)  
else:
    print("No match found")  

# + (bir veya daha fazla) karakter bulunabilir
result = re.findall(r"l.+r", text)  # 'findall' metninde "l" harfinden sonra gelen bir veya daha fazla karakteri arar
if result:
    print("Findall result:", result)  
else:
    print("No match found")  

# ? (sıfır veya bir) karakter bulunabilir
result = re.findall(r"lo?i*t", text)  # 'findall' metninde "l" harfinden sonra gelen sıfır veya bir karakteri arar
if result:
    print("Findall result:", result)  
else:
    print("No match found")  

# {} (belirli sayıda karakter bulunabilir)
result = re.findall(r"hel{2}o", text)  # 'findall' metninde "l" harfinden sonra gelen tam olarak iki "l" ve ardından "o" harfini arar
if result:
    print("Findall result:", result)  
else:
    print("No match found")  

result = re.findall(r"hel{1,2}o", text)  # 'findall' metninde "l" harfinden sonra gelen min bir max iki "l" ve ardından "o" harfini arar
if result:
    print("Findall result:", result)  
else:
    print("No match found")  

result = re.findall(r"\d{2}", text2)  # 'findall' metninde tam olarak iki basamaklı sayıları arar
if result:
    print("Findall result:", result)  
else:
    print("No match found")  

# ( ) (grup oluşturma)
result = re.findall(r"(l.)", text)  # 'findall' metninde "l" harfinden sonra gelen bir karakteri gruplar
if result:
    print("Findall result:", result)  
else:
    print("No match found")  

# | (veya) işlemi
result = re.findall(r"l|r", text)  # 'findall' metninde "l" veya "r" harflerini arar
if result:
    print("Findall result:", result)  
else:
    print("No match found")  
