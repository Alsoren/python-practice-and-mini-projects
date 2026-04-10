#File Handling f = open(filename, mod, buffering, encoding...)
#f = open("Files/dosya.txt", "x") // create a new file 
#f = open("Files/dosya.txt", "w") // create a new file or overwrite existing
#f = open("Files/dosya.txt", "a") // append to an existing file
f = open("Files/dosya.txt", "r", encoding="utf-8") #// read an existing file encoding türkçe karakter için ** file fonksiyonu mod verilmeden default hali read modunda yazar

print(f.read()) #// read the entire file
f.seek(0) #// reset the file pointer to the beginning
print(f.readline()) #// read the first line
f.seek(0) 
print(f.readlines()) #// read all lines
f.seek(0) 
my_list = f.readlines() #// read all lines into a list
print(my_list[2]) #// print the third line
