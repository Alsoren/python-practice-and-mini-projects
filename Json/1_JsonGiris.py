# JSON (JavaScript Object Notation) // JSON, veri değişimi (data interchange) ve (Data base) için hafif bir formattır.
import json 

person = '{"name": "John", "age": 30, "city": "New York", "hobbies": ["reading", "traveling", "swimming"]}' # 'person' nesnesinin JSON dizesi haline getirilmesi // # person json veri türü olduğu için kullanılamaz ve doğrudan işlenemez


# JSON dan Phtona veri çekme
with open("Json/1_JsonGiris.json", "r", encoding="utf-8") as f:  # 'open' fonksiyonu ile "person.json" dosyası okuma modunda açılır
    result=json.load(f)  # json dosyasını bir dictionary olarak yükler
    print(f"Name: {result['name']}")
    print(f"Age: {result['age']}")
    print(f"City: {result['city']}")
    print(f"Hobbies: ", end="")  # 'end' parametresi ile boşluk bırakılır
    for hobby in result["hobbies"]:  # 'hobbies' listesindeki her bir
        print(hobby, end=", ")  # Her bir hobi yazdırılır

# Dict veri türünü Json veri formatına çevirme
person = {"name": "Clair", "age": 23, "city": "Paris", "hobbies": ["acting", "reading", "hiking"]}
person_json = json.dumps(person, indent=4)  # Python sözlüğü JSON dizesine dönüştürülür

# JSON dizesini dosyaya yazma
with open("Json/1_JsonGiris.json", "w", encoding="utf-8") as f:
    json_result = json.dumps(person, indent=4) # JSON dizesi dosyaya yazılır
    f.write(json_result)