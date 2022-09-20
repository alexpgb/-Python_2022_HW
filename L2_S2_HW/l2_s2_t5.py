# Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.

# простое число, это число, которое делится без остатка на 1 и на само себя.
# Варианты решения:
# - число разложено на простые множители;
# - число явяляется простым числом
# Алгоритм:
# 1. Составляем список простых чисел начиная с 2
#  Находим первое простое число 
# 2. Делим N на простое число без остатка, добавляем в массив делитель.
# 3. Если список простых чисел исчерпан, идем за следующим простым числом. 


def get_next_prime_number(start_numer):
    next_prime_number = start_numer + 1
    k = 0
    while True:
        for i in range(2, next_prime_number + k + 1):
            if (next_prime_number + k) % i == 0:
                break
        if next_prime_number + k == i:
            next_prime_number = next_prime_number + k 
            break
        k +=1
    return next_prime_number

# print(get_next_prime_number(7))
    
prime_numer_list = [2]
multipliers = []
n = 1077
r = n
f = True
while f:
    i = 0
    while True:
        if r % prime_numer_list[i] == 0:
            multipliers.append(prime_numer_list[i])
            r = r / prime_numer_list[i]
            if r == 1:
                f = False
                break
        else:
            i += 1
            if i > len(prime_numer_list) - 1:
                prime_numer_list.append(get_next_prime_number(prime_numer_list[-1]))

if len(multipliers) == 1:
    print(f'{n} is prime number.')
else:
    print(f'{n} = {" * ".join(map(str, multipliers))}.')

