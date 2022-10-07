
from tictactoe import Board

LINES_H_DICT = {'a': 0, 'b': 1, 'c': 2}
LINES_V_DICT = {'1': 0, '2': 1, '3': 2}        # перевод шахматной нотации в нотацию для класса BOARD 


def create_new_classic_board():
    global BOARD
    BOARD = Board(dimensions=(3, 3))

def input_is_valid(s):
    r = False
    if  len(s.strip()) == 2 and s[0] in 'abc' and s[1] in '123':
        r = True
    return r

def convert_shess_notation_to_tuple(s):
    return (LINES_H_DICT[s[0]],LINES_V_DICT[s[1]])

def is_position_busy(s):
    r = True
    s_as_tuple = convert_shess_notation_to_tuple(s)
    if BOARD.get_mark_at_position(s_as_tuple) == 0:
        r = False
    return r

def input_throw_to_field(s):
    s_as_tuple = convert_shess_notation_to_tuple(s)
    BOARD.push(s_as_tuple)  # отображает ход на поле

def is_bingo():
    r = False
    if BOARD.result():       # возвращает None если никто не выиграл; 1 - если выиграли Х; 2 - Если выиграли О
        r = True
    return r

def is_empty_cell_exists():
    r = True
    if len([list(el) for el in BOARD.possible_moves()]) == 0:  # возврщащает свободные клетки на поле
        r = False
    return r

create_new_classic_board()
# print(BOARD)
# print()


# Проверка возможных ходов.
# [LINES_H_DICT['c'],LINES_V_DICT['1']] in [list(el) for el in BOARD.possible_moves()]
# BOARD.get_mark_at_position((LINES_H_DICT['b'],LINES_V_DICT['1']))

