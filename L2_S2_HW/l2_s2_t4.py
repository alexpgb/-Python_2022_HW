# Вычислить число c заданной точностью d 
# Пример:
# при d = 0.001, π = 3.141 10-1 <= d <= 10-10
import math

precision_of_number = ''
precision_of_number_as_list =[]
separator = '.'

while True:    
    precision_of_number = input(f'Задайте точность числа в формате 0{separator}001 (q - выход) :') 
    if precision_of_number == 'q':
        break    
    if separator not in precision_of_number:
        print('Формат задан неправильно.')
        continue
    precision_of_number_as_list = precision_of_number.split('.')
    if len(precision_of_number_as_list) != 2:
        print('Формат задан неправильно.')
        continue
    print(round(math.pi, len(precision_of_number_as_list[1])))



