#Требуется сложить два целых числа А и В.

#Входные данные
#В единственной строке входного файла INPUT.TXT записаны два натуральных числа через пробел. Значения чисел не превышают 109.
#Выходные данные
#В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — сумму чисел А и В.


with open ( 'input.txt' ) as inf:#считываем текст
	for line in inf:
		line = line.strip().split()#делаем список из строк
		#print(line)
		line_2 = []
		for i in range(len(line)):#переводим строки в числа
			t = int(line[i])
			line_2.append(t)
		#print(line_2)
		s = sum(line_2)#сумма всех элементов
		#print(s)
		s = str(s)#переводим числовое выражение в строчное
with open ('output.txt', 'w') as ouf:#открываем файл и записываем в него результат
	ouf.write(s)
with open ('output.txt', 'r') as ouf:#просто проверка
	s1=ouf.readline()
	print(s1)
