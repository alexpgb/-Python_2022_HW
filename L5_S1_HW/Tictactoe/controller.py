import random
import model as m
import view_tictactoe as v


def main():
    # здесь первый ход всегда делает первый игрок играющий X
    k = 1 # int(round(random.random(), 0)) + 1  # 1 ход делает первый игрок, 2 ход делает второй игрок 
    v.print_field()
    while True:
        mark = "X" if k == 1 else "O"
        s = v.get_push(mark).strip()
        if s == 'q':
            print(f'Игра прервана {k}-м игроком.')
            break
        elif not m.input_is_valid(s):
            v.print_message(f'Укажите значение в диапазоне {{a..c}}{{1..3}}.')
            continue
        elif m.is_position_busy(s):
            v.print_message(f'Указанная позиция {s} занята.')
        else:
            m.input_throw_to_field(s)
            v.print_field()
            if m.is_bingo():
                v.print_message(f'Выиграли {mark}.')
                break
            elif not m.is_empty_cell_exists():
                v.print_message(f'Ничья.')
                break
            else:
                k = 1 if k == 2 else 2
            



