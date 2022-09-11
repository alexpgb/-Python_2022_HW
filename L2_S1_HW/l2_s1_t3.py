# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random as rand
# from random import randint

l1 = []
n = int(input('Укажите размер списка : '))
number_of_decimals = 2
mx = 0.0
mn = 0.0
for i in range(n):
    l1.append(round(rand.random()*10**rand.randint(0,3), number_of_decimals))
# l1 = [1.1, 1.2, 3.1, 5, 10.01]
print(l1)
mx = round(l1[0]%1, number_of_decimals)
mn = round(l1[0]%1, number_of_decimals)
print(mn)
print('-' * 5)
for i in range(1,len(l1)):
    if l1[i]%1 > mx:
        mx = round(l1[i]%1, number_of_decimals)
    if l1[i]%1 > 0 and l1[i]%1 < mn:
        mn = round(l1[i]%1, number_of_decimals)
    print(mn)
    print(mx)
    print('-' * 5)
print(f'min {mn}, max {mx}, max-min {round(mx - mn, number_of_decimals)}')

