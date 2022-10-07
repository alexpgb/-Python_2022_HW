
from unicodedata import name
import model as m

def print_main_menu():     #   напечатали меню
    print('Выберите действие:\n'+
          '1 - отобразить список всех сотрудников\n'+
          '2 - добавить нового сотрудника\n'+
          '3 - найти сотрудника по id\n'+
          '4 - отфильтровать сотрудников по Фамилии\n'+
          'q - завершение работы.' )


def print_emp_list(emp_list_as_dict):
    if len(emp_list_as_dict) == 0:
        print('Нет информации для отображения')
    else:
        # зададим ширину и наименование колонок
        col_name_as_dict = {el:m.EMP_PROP_DICT[el]['name'] for el in m.EMP_PROP_DICT.keys()}
        col_len_as_dict = {el:m.EMP_PROP_DICT[el]['len'] for el in m.EMP_PROP_DICT.keys()}
        sep = '|'
        # определим максимальную ширину каждого в словаре для печати
        # for dict_key in enumerate(emp_list_as_dict[0].keys()):
        #     col_len_as_dict[dict_key] = max([len(el[dict_key]) for  el in emp_list_as_dict])
        # напечатаем шапку
        print((' ' + sep + ' ').join([f'{col_name_as_dict[key]:<{col_len_as_dict[key]}}' for key in col_name_as_dict.keys()]))
        # напечатаем тело таблицы
        for el in emp_list_as_dict:
            print((' ' + sep + ' ').join([f'{el[key]:<{col_len_as_dict[key]}}' for key in col_name_as_dict.keys()]))


def get_push(m):
    s = input(f'Ход игрока играющего {m}.' \
            'Укажите поле, куда сделать ход, например a1 (q - выход):')
    return s

def print_message(m):
    print(m)

def print_field():
    print(m.BOARD)
    

