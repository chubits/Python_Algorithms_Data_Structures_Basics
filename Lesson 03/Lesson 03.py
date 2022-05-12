'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

from random import randint


run = True

while run:
    items_cnt = int(input("Введите количество элементов в списке: "))

    array = [randint(-100, 100) for _ in range(items_cnt)]
    min_value_idx = max_value_idx = 0
    max_value = min_value = array[0]

    print(array)

    for idx in range(1, len(array)):
        if array[idx] > max_value:
            max_value_idx, max_value = idx, array[idx]
        elif array[idx] < min_value:
            min_value_idx, min_value = idx, array[idx]

    array[min_value_idx], array[max_value_idx] = array[max_value_idx], array[min_value_idx]
    print(array)

    run = input("Продолжить [y/n]: ") == 'y' or False
