# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


import random

def item_number_take_bot(items_numbers_lost, items_number_on_step):
    r = 0
    if items_numbers_lost <= items_number_on_step:
        r = items_numbers_lost
    else:
#        r = random.randint(1,items_can_take)
        r = items_numbers_lost - ((items_numbers_lost//items_number_on_step)*items_number_on_step + 1)
    return r

items_numbers_at_start = 100 # 2021
items_numbers_lost = items_numbers_at_start
items_numbers_has_player = [0, 0]
items_number_on_step = 28
items_can_take = 0
n_as_num = 0
k = int(round(random.random(), 0))  # 0 ход делает первый игрок, 1 ход делает второй игрок
while items_numbers_lost > 0:
    items_can_take = items_number_on_step if items_numbers_lost >= items_number_on_step else items_numbers_lost
    if k == 1:
        n = input(f'Ход игрока {k+1}. Осталось {items_numbers_lost} конфет.  \
            Укажите число конфет от 1 до {items_can_take} включительно (q - выход):')
    else:
        n = str(item_number_take_bot(items_numbers_lost, items_number_on_step))
        print(f'Ход игрока {k+1}. Взял {n} конфет ')
    if n == 'q':
        print(f'Игра прервана {k + 1}-м игроком.')
        break
    elif len(n.strip()) > 2 or not n.strip().isdigit() or not 0 < int(n.strip()) <= items_can_take:
        continue
    else:
        n_as_num = int(n.strip())
        items_numbers_lost -= n_as_num   # нужно, чтобы выйти из цикла
        if items_numbers_lost == 0:      # bingo
            items_numbers_has_player[k] = items_numbers_at_start
            print(f'Победил игрок {k + 1}. Он получает все конфеты')
        else:
            items_numbers_has_player[k] += n_as_num
            k = 0 if k == 1 else 1

