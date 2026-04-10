import re

text = "Hello my telephone number is 123-456-7890 and my age is 32"

result = re.findall(r"[^0-9]+", text) # 'findall' metninde rakam olmayan karakterleri arar '+' sayesinde bir veya daha fazlasını bulur
print(result)

result = re.findall(r"[0-9]+", text) # 'findall' metninde rakam olan karakterleri arar 
print(result)

# Search METHODU
result = re.search(r"number", text) # 'search' metninde "number" kelimesini arar
print(result)

# Start POSITION
print(result.start()) # "number" kelimesinin başlangıç pozisyonu yazdırır 

# Span METODU
print(result.span()) # "number" kelimesinin başlangıç ve bitiş pozisyonlarını yazdırır

# String METODU
print(result.string) # "number" kelimesinin bulunduğu metni yazdırır

# Group METODU
print(result.group()) # "number" kelimesini yazdırır

# Split METODU
result = re.split(r"\s+", text, maxsplit=2) # Metni boşluklara göre 2 defa böler
print(result)

# Sub METODU
result = re.sub(r"number", "NUMARA", text) # "number" kelimesini "NUMARA" ile değiştirir
print(result)

result = re.sub(r"\s", "-", text) # Boşlukları "-" ile değiştirir
print(result)

# Match METODU
result = re.match(r"Hello", text) # 'match' metninde "Hello" kelimesini arar
print(result)
