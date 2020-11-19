"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'j': 9, 'k': 10}
my_order_dict = OrderedDict(my_dict)
print(my_dict)
print(my_order_dict)


def dict_copy():
    new_dict = my_dict.copy()


def order_dict_copy():
    new_order_dict = my_order_dict.copy()


def dict_get():
    el = my_dict.get('f')


def order_dict_get():
    el = my_order_dict.get('f')


def dict_keys():
    my_keys = my_dict.keys()


def order_dict_keys():
    my_keys = my_order_dict.keys()


def dict_clear():
    my_dict.clear()


def order_dict_clear():
    my_order_dict.clear()


print('------------copy---------------')
print(f"dict_copy - {timeit('dict_copy()', setup='from __main__ import dict_copy', number=10000)}")
print(f"order_dict_copy - {timeit('order_dict_copy()', setup='from __main__ import order_dict_copy', number=10000)}")
"""
copy работает намного бысрее со словарями
dict_copy - 0.002473100000000006
order_dict_copy - 0.0120515
"""
print('------------get--------------')
print(f"dict_get - {timeit('dict_get()', setup='from __main__ import dict_get', number=10000)}")
print(f"order_dict_get - {timeit('order_dict_get()', setup='from __main__ import order_dict_get', number=10000)}")
"""
get работает примерно одинаково
dict_get - 0.0022527999999999992
order_dict_get - 0.0022483999999999976
"""
print('------------keys--------------')
print(f"dict_keys - {timeit('dict_keys()', setup='from __main__ import dict_keys', number=10000)}")
print(f"order_dict_keys - {timeit('order_dict_keys()', setup='from __main__ import order_dict_keys', number=10000)}")
"""
keys работает примерно одинаково
dict_keys - 0.0023804999999999937
order_dict_keys - 0.0023554000000000075
"""
print('------------clear--------------')
print(f"dict_clear - {timeit('dict_clear()', setup='from __main__ import dict_clear', number=10000)}")
print(f"order_dict_clear - {timeit('order_dict_clear()', setup='from __main__ import order_dict_clear', number=10000)}")
"""
clear работает примерно одинаково
dict_clear - 0.002204700000000004
order_dict_clear - 0.0022437999999999902
"""