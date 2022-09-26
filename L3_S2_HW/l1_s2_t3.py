# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример: - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# (1+1/n)**n

n = int(input('Укажите n :'))
# было 
s = 0
d = {}
summ = 0
for i in range(1, n+1):
    s = (1+1/i)**i
    d[i] = s
    summ += s
    print(s)
print(d)
print(summ)

# стало
print(sum([(1+1/i)**i for i in range(1, n + 1)]))