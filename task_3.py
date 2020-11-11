"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
import hashlib


def num_of_str(my_str):
    my_list = set()
    for i in range(len(my_str)):
        for j in range(i, len(my_str)):
            sub_str = my_str[i: j + 1]
            if sub_str == my_str:
                continue
            my_list.add(hashlib.sha256(sub_str.encode()).hexdigest())
    return my_list


word = 'papaз'
print(num_of_str(word))
print(f'в строке "{word}" {len(num_of_str(word))} уникальных подстрок')

