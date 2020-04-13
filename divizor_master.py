'''Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000.
 Модуль содержит функции:
1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
2) выводит список всех делителей числа;
3) выводит самый большой простой делитель числа.;'''
import math

def f_prost_chisla(n):
    digit = []
    for i in range(2, n+1 ):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            digit.append(i)
    print(f'Простые числа введеного числа \n {digit}')    # вывод простых чисел


#функция выводит список всех делителей числа;
def f_delitely_chisla(n):
    i = 2
    spisok_delitely = []
    while i <= n:
        if n % i == 0:
            spisok_delitely.append(i)
            n //= i
        else:
            i += 1
    print(spisok_delitely)
    delitely = []
    for d in spisok_delitely:

        if d % i == 0:
            break
        else:
            i+=1
            delitely.append(d)
    print(f'{delitely} - простые делители числа. Значит ищем наибольший делитель:')
    spisok_delit_sort = sorted(delitely, reverse=True)
    print(f'Наибольший простой делитель числа {spisok_delit_sort[0]}')

######pro
#4) функция выводит каноническое разложение числа

def f_mnogitely(n):
    print(f' Вы ввели число {n}')
    Mnogitely = []
    j = 2
    while j <= n:
        if n % j == 0:
            Mnogitely.append(j)
            n //= j
        else:
            j += 1

    if n > 1:
        Mnogitely.append(n)


#функция выводит самый большой делитель (не обязательно простой) числа

    Sort_mnogitely = sorted(Mnogitely)
    Bigest_mnogityl = Sort_mnogitely[-1]
    print(f' Множители числа  - {Mnogitely}. Наибольший множитель: {Bigest_mnogityl}')

#f_mnogitely(144560)
#f_prost_chisla(144)
#f_delitely_chisla(500)








