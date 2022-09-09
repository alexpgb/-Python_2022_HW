# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

while True:
    x = input('Укажите координаты точки по оси X :') 
    y = input('Укажите координаты точки по оси Y (q - выход) :') 
    if y == 'q':
        break
    elif  int(x) == 0 and int(y) == 0:
        continue
    else:
        r = ''        
        if int(x) > 0 and int(y) >0:
            r = '1'
        elif int(x) < 0 and int(y) > 0:
            r = '2'
        elif int(x) < 0 and int(y) < 0:
            r = '3'
        elif int(x) > 0 and int(y) < 0:
            r = '4'
        elif int(x) == 0:
            r = 'Точка на оси X'
        elif int(y) == 0:
            r = 'Точка на оси Y'
        else:
            r = '?'
        print(r)

