# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.


import random


l = [random.randint(1,10) for i in range(random.randint(1, 30))]
print(l)
l_as_set = set(l)
print(f'{", ".join(map(str, l_as_set))}')
