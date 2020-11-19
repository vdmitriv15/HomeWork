"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
from collections import defaultdict
import functools

numbers = defaultdict(list)
for i in range(2):
    number = input('введите шестнадцатеричное число ')
    numbers[number] = list(number)
print(numbers)

sum_of_numbers = sum([int(''.join(i), 16) for i in numbers.values()])
print(f'сумма - {sum_of_numbers}')

mult_of_numbers = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in numbers.values()])
print(f'произведение - {mult_of_numbers}')

