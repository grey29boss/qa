
with open ("str_1.txt") as f:# чтение из файла
    for line in f:
        line = line.rstrip().split()#тут сделал список
        print(line)
        #print(len(line))
s=line[::-1]#список последний элемент на первом месте
print(str(s))
with open ("new.txt","w") as file:#запись списка в файл в строчку, потому что ' ' пробел, а если было '\n' , то каждый элемент сновой строки
    for items in s:
        file.write(items+' ')



#with open('dataset.txt') as inf:
    #for line in inf:
        #line= line.replace('\n')
        #line=line.strip().lower().splitlines()
       #print(line)
#def create_dict(list_of_words):#создание словаря из списка строк- функция
    #d = {}
    #for word in list_of_words:
        #if word not in d:
            #d[word]=1
        #else:
            #d[word]+=1
    #return d

#sl = create_dict(line)
#print(sl)