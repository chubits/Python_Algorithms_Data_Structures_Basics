'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

array = list(range(2, 100))

print(array)

two_mult = three_mult = four_mult = five_mult = six_mult = seven_mult = eight_mult = nine_mult = 0

for item in array:
    if not item % 2:
        two_mult += 1
    if not item % 3:
        three_mult += 1
    if not item % 4:
        four_mult += 1
    if not item % 5:
        five_mult += 1
    if not item % 6:
        six_mult += 1
    if not item % 7:
        seven_mult += 1
    if not item % 8:
        eight_mult += 1
    if not item % 9:
        nine_mult += 1

print("*" * 50)
print(two_mult, three_mult, four_mult, five_mult, six_mult, seven_mult, eight_mult, nine_mult)
