"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
from timeit import timeit


def memorize(func):
    def wrap(n, memory={}):
        record = memory.get(n)
        if record is None:
            record = func(n)
            memory[n] = record
        return record
    return wrap


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


@memorize
def recursive_reverse_with_memo(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


my_num = 650056139379613
# print(recursive_reverse(my_num))
print(timeit('recursive_reverse(my_num)', setup='from __main__ import recursive_reverse, my_num', number=10000))
# print(recursive_reverse_with_memo(my_num))
print(timeit('recursive_reverse_with_memo(my_num)', setup='from __main__ import recursive_reverse_with_memo, my_num',
             number=10000))

"""
для ускорения работы функции использовал функцию обертку memorize, которая сохраняет в кэш повторяющиеся числа
без обертки 0.49310160000000003 сек.
с использованием обертки 0.002728100000000011 сек.
функция memorize значительно ускоряет работу функции
"""