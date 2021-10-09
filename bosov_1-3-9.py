
with open ("str_1.txt") as f:# чтение из файла
    for line in f:
        line = line.rstrip().split()#тут сделал список
        print(line)
        
s=line[::-1]#список последний элемент на первом месте
print(str(s))
with open ("new.txt","w") as file:#запись списка в файл в строчку, потому что ' ' пробел, а если было '\n' , то каждый элемент сновой строки
    for items in s:
        file.write(items+' ')
