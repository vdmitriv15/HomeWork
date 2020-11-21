"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from memory_profiler import profile
""" факрориал """


@profile
def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def factorial_rec(n):  # факториал высчитывается с помощью рекурсии
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)
"""если применить @profile к рекурсии, то результат будет выводиться n - раз"""


@profile
def check_rec(n):  # функция для проверки использования памяти рекурсией
    factorial_rec(n)


factorial(5)
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     18.8 MiB     18.8 MiB           1   @profile
    30                                         def factorial(n):
    31     18.8 MiB      0.0 MiB           1       res = 1
    32     18.8 MiB      0.0 MiB           5       for i in range(2, n + 1):
    33     18.8 MiB      0.0 MiB           4           res *= i
    34     18.8 MiB      0.0 MiB           1       return res
"""

check_rec(5)
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    45     18.8 MiB     18.8 MiB           1   @profile
    46                                         def check_rec(n):  # функция для проверки использования памяти рекурсией
    47     18.8 MiB      0.0 MiB           1       factorial_rec(n)
"""
"""в обеих функциях память расходуется одинаково"""


"""функция определяющая количество подстрок"""

import hashlib


@profile
def num_of_str_hash(my_str):  # с использованием хэширования
    my_list = set()
    for i in range(len(my_str)):
        for j in range(i, len(my_str)):
            sub_str = my_str[i: j + 1]
            sub_str_hash = hashlib.sha256(sub_str.encode()).hexdigest()
            my_str_hash = hashlib.sha256(my_str.encode()).hexdigest()
            if sub_str_hash == my_str_hash:
                continue
            my_list.add(sub_str_hash)
    return len(my_list)


@profile
def num_of_str(my_str):
    my_list = set()
    for i in range(len(my_str)):
        for j in range(i, len(my_str)):
            sub_str = my_str[i: j + 1]
            if sub_str == my_str:
                continue
            my_list.add(sub_str)
    return len(my_list)


num_of_str_hash('papa')
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    76     19.1 MiB     19.1 MiB           1   @profile
    77                                         def num_of_str_hash(my_str):  # с использованием хэширования
    78     19.1 MiB      0.0 MiB           1       my_list = set()
    79     19.1 MiB      0.0 MiB           5       for i in range(len(my_str)):
    80     19.1 MiB      0.0 MiB          14           for j in range(i, len(my_str)):
    81     19.1 MiB      0.0 MiB          10               sub_str = my_str[i: j + 1]
    82     19.1 MiB      0.0 MiB          10               sub_str_hash = hashlib.sha256(sub_str.encode()).hexdigest()
    83     19.1 MiB      0.0 MiB          10               my_str_hash = hashlib.sha256(my_str.encode()).hexdigest()
    84     19.1 MiB      0.0 MiB          10               if sub_str_hash == my_str_hash:
    85     19.1 MiB      0.0 MiB           1                   continue
    86     19.1 MiB      0.0 MiB           9               my_list.add(sub_str_hash)
    87     19.1 MiB      0.0 MiB           1       return len(my_list)
"""

num_of_str('papa')
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    90     19.1 MiB     19.1 MiB           1   @profile
    91                                         def num_of_str(my_str):
    92     19.1 MiB      0.0 MiB           1       my_list = set()
    93     19.1 MiB      0.0 MiB           5       for i in range(len(my_str)):
    94     19.1 MiB      0.0 MiB          14           for j in range(i, len(my_str)):
    95     19.1 MiB      0.0 MiB          10               sub_str = my_str[i: j + 1]
    96     19.1 MiB      0.0 MiB          10               if sub_str == my_str:
    97     19.1 MiB      0.0 MiB           1                   continue
    98     19.1 MiB      0.0 MiB           9               my_list.add(sub_str)
    99     19.1 MiB      0.0 MiB           1       return len(my_list)
"""
"""в обеих функциях память расходуется одинаково"""