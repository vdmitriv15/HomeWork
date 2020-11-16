"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


my_num = 564923
"""
print(revers(my_num))
print(revers_2(my_num))
print(revers_3(my_num))
"""


def main_func():
    revers(my_num)
    revers_2(my_num)
    revers_3(my_num)


cProfile.run('main_func()')
"""
по cProfile не возможно определить какая функция отрабатывает быстрее
из статистеки видно, что revers (рекурсивная) функция отрабатывает 7 раз
"""


print(f"revers - {timeit('revers(my_num)', setup='from __main__ import revers, my_num', number=10000)}")
print(f"revers_2 - {timeit('revers_2(my_num)', setup='from __main__ import revers_2, my_num', number=10000)}")
print(f"revers_3 - {timeit('revers_3(my_num)', setup='from __main__ import revers_3, my_num', number=10000)}")

"""
revers - 0.027905999999999986
revers_2 - 0.0188334
revers_3 - 0.004812000000000011
рекурсивная функция самая медленная
самая эфективная revers_3 
"""

