# 

dec = int(input('Укажите целое положительное числои : '))
bin = ''
n = 0
while True:
    bin = str(dec//2**n%2) + bin
    n += 1
    if dec//2**n == 0:
        break
print(f'{dec} -> {bin}')
