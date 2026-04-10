import re

def is_valid_name(name):

    result = re.split(r"\s+", name)
    for i in result:
        if not re.findall(r"\A[A-ZÇQİÖŞÜ]", i):
            return False
        
    if not re.findall("[^a-zA-ZçğıöşüÇĞİÖŞÜ]+", name):
        return False
    
    return True

while True:
    name = input("Please enter a name: ")

    if is_valid_name(name):
        break
    else:
        print("Please enter a valid name.")

print("Name is valid:", name)