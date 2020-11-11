"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""


def time_of_function(function):
    import time

    def wrapped(*args):
        start_time = time.time()
        function(*args)
        end_time = time.time()
        print(f'время выполнения - {end_time - start_time} сек')
    return wrapped


@time_of_function
def my_list_func(n):
    my_list = [[x+1 for x in range(2)] for y in range(n)]
    return print("список сгенерирован")


@time_of_function
def my_dict_func(n):
    my_dict = {x: x + 1 for x in range(n)}
    return print("словарь сгенерирован")


n = 100000
my_list_func(n)
my_dict_func(n)

"""
в моем случае список заполняется медленее словаря, т.к. для заполнения списка использован цикл в цикле, т.е.
сложность O(N**2), а у генерации словаря O(N)
 """


@time_of_function
def my_list_func_second(n):
    my_list_sec = [n for x in range(n)]
    return print("список 2 сгенерирован")


my_list_func_second(n*2)

"""
Если использовать одинаковую сложность O(N), то словарь заполняется медленее, т.к. хэширует объекты
"""