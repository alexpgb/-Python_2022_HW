# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

import random

l = [random.randint(1,10) for i in range(random.randint(1, 30))]
print(l)

# было 
l_as_set = set(l)
print(f'{", ".join(map(str, l_as_set))}')

# стало
print([el for i, el in enumerate(l) if el not in l[:i] or i == 0])
