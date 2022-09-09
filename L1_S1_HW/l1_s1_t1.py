
# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
s = 0 
while True:
    s = input('Укажите номер дня недели от 1 до 7. 0 - Выход :')
    if len(s.strip()) > 1 or not s.isdigit() or int(s) < 0 or int(s) > 7:
        continue
    elif s == '0':
        break
    elif s in ['6','7']:
        print('Yes')        
    else:
        print('No')
