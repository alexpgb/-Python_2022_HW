# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Укажите N :'))
l = '' # '1 , 3, 5 , 7'
s = 0
c = 1
l1 = []
for i in range(-n, n+1):
    l1.append(i)
with open('./L1_S2_HW/list.txt', 'r') as f:
    l = f.readline()
l2 = l.split(',')
print(l) 
print(l1)
print(l2)
for i in l2:
    print(l1[int(i.strip())])
    c = c * l1[int(i.strip())]
print(c)    




#with open('list.txt', 'r') as f:
    
    
    
    
