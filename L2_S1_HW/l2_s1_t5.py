# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n == 0:
        r = 0
    elif n == 1:
        r = 1 + fib(n-1)
    else:
        r = fib(n-1) + fib(n-2)
    return r


def fib_in_list(n, l):
    if n == 0:
        r = 0
    elif n == 1:
        r = 1 + fib_in_list(n-1, l)
    else:
        r = fib_in_list(n-1, l) + l[-2]
    l.append(r)
    return r

def fib_and_fibneg_in_list(n, l):
    if n == 0:
        r = 0
    elif n == 1:
        r = 1 + fib_in_list(n-1, l)
    else:
        r = fib_in_list(n-1, l) + l[-2]
    l.append(r)
    return r

def fib_neg(n):
    if n == -1:
        r = 1
    elif n == -2:
        r = -1
    else:
        r = fib_neg(n+2) - fib_neg(n+1)
    return r

def fib_neg_in_list(n, l):
    if n == -1:
        r = 1
    elif n == -2:
        r = - fib_neg_in_list(n+1, l)
    else:
        r = - fib_neg_in_list(n+1, l) + l[1] 
    l.insert(0, r)
    return r


n = int(input('Укажите целое число не меньшее 0 :'))
l =[]
# for i in range(n+1):
#       l.append(fib(i))
fib_in_list(n, l)                  # на каждом рекурсивном вызове добавляет элемент в список
# for i in range(-1, -n-1, -1):
#        l.insert(0, fib_neg(i))
if n > 0:  
    fib_neg_in_list(-n, l)         # на каждом рекурсивном вызове добавляет элемент в список
print(l)
