"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
from collections import deque
from timeit import timeit


my_list = list(range(1000))
my_deque = deque(range(1000))
# print(my_list)
# print(my_deque)


def list_add_back():
    for i in range(1001, 1500):
        my_list.append(i)


def deque_add_back():
    for i in range(1001, 1500):
        my_deque.append(i)


def list_del_back():
    for i in range(500):
        my_list.pop()


def deque_del_back():
    for i in range(500):
        my_deque.pop()


def list_add_first():
    for i in range(1001, 1500):
        my_list.insert(0, i)


def deque_add_first():
    for i in range(1001, 1500):
        my_deque.appendleft(i)


def list_del_first():
    for i in range(500):
        my_list.pop(0)


def deque_del_first():
    for i in range(500):
        my_deque.popleft()


def list_sum():
    sum(my_list)


def deque_sum():
    sum(my_deque)


print("-------------------add to back------------------")
print(f'list_add_back - {timeit("list_add_back()", setup="from __main__ import list_add_back", number=100)}')
print(f'deque_add_back - {timeit("deque_add_back()", setup="from __main__ import deque_add_back", number=100)}')
print("-------------------delete from back------------------")
print(f'list_del_back - {timeit("list_del_back()", setup="from __main__ import list_del_back", number=100)}')
print(f'deque_del_back - {timeit("deque_del_back()", setup="from __main__ import deque_del_back", number=100)}')
print("-------------------add to beginning------------------")
print(f'list_add_first - {timeit("list_add_first()", setup="from __main__ import list_add_first", number=100)}')
print(f'deque_add_first - {timeit("deque_add_first()", setup="from __main__ import deque_add_first", number=100)}')
print("-------------------add from beginning------------------")
print(f'list_del_first - {timeit("list_del_first()", setup="from __main__ import list_del_first", number=100)}')
print(f'deque_del_first - {timeit("deque_del_first()", setup="from __main__ import deque_del_first", number=100)}')
print("-------------------sum------------------")
print(f'list_sum - {timeit("list_sum()", setup="from __main__ import list_sum", number=100)}')
print(f'deque_sum - {timeit("deque_sum()", setup="from __main__ import deque_sum", number=100)}')

"""
list_add_back - 0.0074438
deque_add_back - 0.007322300000000004
скорость функций добавления в конец в list и deque примерно равны

list_del_back - 0.006589499999999998
deque_del_back - 0.006410899999999997
скорость функций удаления последних элементов из list и deque примерно равны

list_add_first - 0.8505476000000001
deque_add_first - 0.007891399999999993
добавление элементов в начало deque намного быстрее, чем list

list_del_first - 0.5359587
deque_del_first - 0.006326000000000054
также с удалением элементов

list_sum - 0.0008984000000000769
deque_sum - 0.0010129000000000943
в deque суммироние элементов происходит быстрее чем в list
"""