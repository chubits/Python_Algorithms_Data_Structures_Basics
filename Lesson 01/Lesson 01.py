'''
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''
a = int(input("Введите число a = "))
b = int(input("Введите число b = "))
c = int(input("Введите число c = "))

if a < b < c or a > b > c:
    print(b)
elif b < c < a or b > c > a:
    print(c)
else:
    print(a)
