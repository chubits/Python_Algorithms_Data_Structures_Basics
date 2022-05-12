'''
Определить, какое число в массиве встречается чаще всего.
'''

from random import randint


while input("Прогнали[y/n]: ").lower() == 'y':
    items_cnt = int(input("Введите количество элементов в списке: "))
    array = [randint(0, items_cnt // 2) for _ in range(items_cnt)]

    print(array)

    size = len(array)
    max_cnt = 1
    item = array[0]

    for i in range(size - 1):
        cnt = 1
        for j in range(i + 1, size):
            if array[i] == array[j]:
                cnt += 1

        if cnt > max_cnt:
            max_cnt = cnt
            item = array[i]

    print("*" * 10, ' через итерации ', "*" * 10)
    print(f"Число {item} повторяестся {max_cnt} раз(а)")

    max_cnt = 1
    item = array[0]

    for i in set(array):
        cnt = array.count(i)
        if cnt > max_cnt:
            max_cnt = cnt
            item = i

    print("*" * 10, ' через множество и count ', "*" * 10)
    print(f"Число {item} повторяестся {max_cnt} раз(а)")
