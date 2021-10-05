#Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран. Обратите внимание, что на вход программе приходят вещественные числа.
a = float(input())
b = float(input())
print('\nДля получения остатка от деления введите "mod"','\nДля возведения в степень введите "pow"','\nДля целочисленного деления чисел введите "div"')
c = str(input('Оператор + - / *:  '))
#вводить функции?
# сумма
def plus(a,b,c): 
    c == '+'
    rez_s = a+b
    print(rez_s)

# вычитание    
def minus(a,b,c):
    c=='-'
    rez_m = a-b
    print(rez_m)

#деление - division  
def division (a,b,c):
    try:
        c == '/'
        b == 0
        rez_d = a / b
        print(rez_d)
    except ZeroDivisionError:
        print('Деление на 0!')

# умножение multiplication    
def multi (a,b,c):
    c == '*'
    rez_mul =a * b
    print (rez_mul)

#возведение в степень -  exponentiation   
def expon (a,b,c):
    c == 'pow'
    rez_expon = a**b
    print (rez_expon)

#возможность взятия остатка от деления (mod)
def mod (a,b,c):
    c == 'mod'
    rez_mod = a%b
    print (rez_mod)

#возможность целочисленного деления чисел (div)
def div (a,b,c):
    c == 'div'
    rez_div = a//b
    print (rez_div)

if c == '+':
    plus(a,b,c)
elif c == '-':
    minus(a,b,c)
elif c == '/':
    division(a,b,c)
elif c == '*':
    multi(a,b,c)
elif c == 'pow':
    expon (a,b,c)
elif c == 'mod':
    mod(a,b,c)
elif c == 'div':
    div(a, b, c)





