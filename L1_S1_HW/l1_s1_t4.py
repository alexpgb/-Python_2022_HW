# .Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).

while True:
    x = input('Укажите номер четверти (q - выход) :') 
    if x == 'q':
        break
    elif  x.isalpha() or int(x) < 1 or int(x) > 4:
        continue
    else:
        r = ''        
        if int(x) == 1:
            r = 'x > 0; y > 0'
        elif int(x) == 2:
            r = 'x < 0; y > 0'
        elif int(x) == 3:
            r = 'x < 0; y < 0'
        elif int(x) == 4:
            r = 'x > 0; y < 0'
        else:
            r = '?'
        print(r)