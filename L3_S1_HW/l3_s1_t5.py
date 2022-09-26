# 5 Создайте программу для игры в "Крестики-нолики".


import random

def input_is_valid(s, p):
    r = False
    if  len(s.strip()) == 2 and s.strip()[0] in 'abc' and s.strip()[1] in '123':
        r = True
    return r


def print_field(p):
    print('  ' + ' | '.join(lines_h))
    for i, el in enumerate(p):
        print(lines_v[i] + ' ' + ' | '.join([' ' if j == None else j for j in el]))

def input_throw_to_field(m, s, p):
    n = [lines_h_dict[s[0]], lines_v_dict[s[1]]]
    if p[n[1]][n[0]] == None:
        p[n[1]][n[0]] = m
        return True
    return False


def is_bingo(p):
    r = False
    if not r:
        for el in p:
            if len([i for i in el if i == el[0] and el[0] != None]) == 3: #проверяем горизонтали
                r = True
                break
    if not r:
        for el in list(zip(*p)):                        # транспонируем игровое поле
            if len([i for i in el if i == el[0] and el[0] != None]) == 3: #проверяем горизонтали
                r = True
                break
    if not r:
        if len([p[i][i] for i in range(len(p)) if p[i][i] == p[0][0] and p[0][0] != None]) == 3: #проверяем главную диагональ
            r = True
    if not r:
        if len([p[i][-1-i] for i in range(len(p)) if p[i][-1-i] == p[0][-1] and p[0][-1] != None ]) == 3: #проверяем другую диагональ
            r = True
    return r

def is_final(p):
    r = True
    for el in p:
        if None in el:
            r= False
            break
    return r

lines_h_dict = {'a': 0, 'b': 1, 'c': 2}
lines_v_dict = {'1': 0, '2': 1, '3': 2}
lines_v = ['1','2','3']
lines_h = ['a','b','c']
p = [[None for i in range(3)] for j in range(3)]
k = int(round(random.random(), 0))  # 0 ход делает первый игрок, 1 ход делает второй игрок
print_field(p)
while True:
    m = "0" if k == 0 else "x"
    if True: # k == 1:
        s = input(f'Ход игрока играющего {m}. \
            Укажите поле, куда сделать ход, например a1 (q - выход):')
    # else:
    #     n = str(item_number_take_bot(items_numbers_lost, items_number_on_step))
    #     print(f'Ход игрока {k+1}. Взял {n} конфет ')
    if s == 'q':
        print(f'Игра прервана {k + 1}-м игроком.')
        break
    elif not input_is_valid(s, p):
        continue
    else:
        if input_throw_to_field(m, s, p): 
#            p = [['x', None, None], ['x', 'x', None], ['x', None, None]]
#            p = [['x', 'x', 'x'], [None, None, None], [None, None, None]]
#            p = [[None, None, None], [None, None, None], ['x', 'x', 'x']]
#            p = [['x', None, None], [None, 'x', None], [None, None, 'x']]
#            p = [[None, None, 'x'], [None, 'x', None], ['x', None, 'x']]
            print_field(p)
            if is_bingo(p):
                print(f'Выиграли {m}.')
                break
            elif is_final(p):
                print(f'Ничья.')
                break
            k = 0 if k == 1 else 1
        else:
            print(f'Поле заняато.')











