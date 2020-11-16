"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_gen(nums):
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr


my_nums = list(range(1000))
# print(func_1(list(range(1000))))
print(timeit("func_1(my_nums)", setup="from __main__ import func_1, my_nums", number=1000))
# print(func_gen(list(range(1000))))
print(timeit("func_gen(my_nums)", setup="from __main__ import func_gen, my_nums", number=1000))

"""
func_1 отрабатывает за 0.1773103 сек.
func_gen отрабатывает почти в два раза быстее 0.1024613 сек.
"""
