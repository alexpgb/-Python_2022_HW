# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

polynom_as_str = ''
k = random.randint(1,6)
polynom_as_dict = {i:( 1 if round(random.random(),0) == 1 else -1 , random.randint(0,50))   for i in range(k+1)}
print(polynom_as_dict)
for el in polynom_as_dict.keys():
    if polynom_as_dict[el][1] != 0:
        polynom_as_str = f"{' + ' if polynom_as_dict[el][0] > 0 else ' - '} {polynom_as_dict[el][1]}{'' if el == 0 else 'x**'+str(el) }" + polynom_as_str
polynom_as_str += ' = 0'
print(polynom_as_str)

