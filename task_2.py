"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random


def merge_sort(obj_list):
    if len(obj_list) > 1:
        center = len(obj_list) // 2
        left_obj_list = obj_list[:center]
        right_obj_list = obj_list[center:]

        merge_sort(left_obj_list)
        merge_sort(right_obj_list)

        i, j, k = 0, 0, 0
        while i < len(left_obj_list) and j < len(right_obj_list):
            if left_obj_list[i] < right_obj_list[j]:
                obj_list[k] = left_obj_list[i]
                i += 1
            else:
                obj_list[k] = right_obj_list[j]
                j += 1
            k += 1

        while i < len(left_obj_list):
            obj_list[k] = left_obj_list[i]
            i += 1
            k += 1
        
        while j < len(right_obj_list):
            obj_list[k] = right_obj_list[j]
            j += 1
            k += 1
        return obj_list


my_list = [random.uniform(0, 50) for _ in range(5)]
print(f'исходный список - {my_list}')
"""
исходный список - [27.738978301020833, 3.95149792124867, 28.015236934627385, 27.719376288554155, 34.49386971825727]
"""
print(f'отсортированный список - {merge_sort(my_list)}')
"""
отсортированный список -
[3.95149792124867, 27.719376288554155, 27.738978301020833, 28.015236934627385, 34.49386971825727]
"""
