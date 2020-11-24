"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
from timeit import timeit
import random


def bubble_sort_rev(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_rev_opt(list_obj):
    n = 1
    swapped = True
    while n < len(list_obj):
        if not swapped:
            break
        swapped = False
        for i in range(len(list_obj)-n):
            if list_obj[i] < list_obj[i+1]:
                swapped = True
                list_obj[i], list_obj[i+1] = list_obj[i+1], list_obj[i]
        n += 1
    return list_obj


def bubble_sort_rev_opt_2(list_obj):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list_obj) - 1):
            if list_obj[i] < list_obj[i + 1]:
                list_obj[i], list_obj[i + 1] = list_obj[i + 1], list_obj[i]
                swapped = True
    return list_obj


my_list = [random.randint(-100, 100) for j in range(10)]

print(f'исходный список - {my_list}')
print(f'отсортированный список bubble_sort_rev - {bubble_sort_rev(my_list[:])}')
print(f'отсортированный список bubble_sort_rev_opt - {bubble_sort_rev_opt(my_list[:])}')
print(f'отсортированный список bubble_sort_rev_opt_2 - {bubble_sort_rev_opt_2(my_list[:])}')
"""
исходный список - [-84, 23, -84, 45, 92, 1, -34, -96, -44, 31]
отсортированный список bubble_sort_rev - [92, 45, 31, 23, 1, -34, -44, -84, -84, -96]
отсортированный список bubble_sort_rev_opt - [92, 45, 31, 23, 1, -34, -44, -84, -84, -96]
отсортированный список bubble_sort_rev_opt_2 - [92, 45, 31, 23, 1, -34, -44, -84, -84, -96]
"""

print(timeit("bubble_sort_rev(my_list[:])",
             setup="from __main__ import bubble_sort_rev, my_list", number=1000))  # 0.013648499999999994
print(timeit("bubble_sort_rev_opt(my_list[:])",
             setup="from __main__ import bubble_sort_rev_opt, my_list", number=1000))  # 0.014246900000000007
print(timeit("bubble_sort_rev_opt_2(my_list[:])",
             setup="from __main__ import bubble_sort_rev_opt_2, my_list", number=1000))  # 0.014729199999999998
"""
функции отрабатывают примерно одинаково, оптимизация неэфективна
"""

my_list_second = [50, 45, 20, 10, 5, -5, -17, -32, -49, -82]
print(timeit("bubble_sort_rev(my_list_second[:])",
             setup="from __main__ import bubble_sort_rev, my_list_second", number=1000))  # 0.008962799999999993
print(timeit("bubble_sort_rev_opt(my_list_second[:])",
             setup="from __main__ import bubble_sort_rev_opt, my_list_second", number=1000))  # 0.004295800000000002
print(timeit("bubble_sort_rev_opt_2(my_list_second[:])",
             setup="from __main__ import bubble_sort_rev_opt_2, my_list_second", number=1000))  # 0.0047861999999999905
"""
обе оптимизированые функции работают значительно быстрее с заранее отсортированым списком (а также со списками,
в которых требуется несколько изменений
"""
