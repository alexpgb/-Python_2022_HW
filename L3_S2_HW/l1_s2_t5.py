# Реализуйте алгоритм перемешивания списка.

import random as rand

l1 = []
l2 = []
n = int(input('Укажите размер списка : '))
for i in range(n):
    l1.append(rand.randint(0, 50))
print(l1)
l11 = l1.copy()
# было
for i in range(n):
    e = rand.randint(0, len(l1)-1)
    print(e)
    e2 = l1.pop(e)
    l2.append(e2)
print(l2)

# стало
l3 = [l2.pop(rand.randint(0, len(l2)-1)) for i in range(len(l2))]
print(l3)