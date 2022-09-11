# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора 
# псевдослучайных чисел.


import time

def random_number1():
    return float(str(time.perf_counter())[::-1][:3:])/1000


def random_number2(minimum,maximum):
    now = str(time.perf_counter())
    rnd = float(now[::-1][:3:])/1000
    return round(minimum + rnd*(maximum-minimum),3)

for i in range(10):
    print(random_number1())    
    print(random_number2(1, 5))    