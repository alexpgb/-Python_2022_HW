# Напишите программу, которая принимает на вход
#  вещественное число и показывает сумму его цифр.

s = input('Укажите число :')
summ = 0
# Было 
for i in s:
    if i.isnumeric():
        summ = summ + int(i)
print(f'Сумма цифр {summ}')
# Стало
print(f'Сумма цифр {sum([int(i) for i in s if i.isnumeric()])}')

