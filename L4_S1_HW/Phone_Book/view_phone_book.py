
import model as m

def print_main_menu():     #   напечатали меню
    print('Выберите действие:\n'+
          '1 - отобразить весь список\n'+
          '2 - добавить элемент в список\n'+
          '3 - найти элемент(-ы) по номеру телефона\n'+
          '4 - найти элемент(-ы) по наименованию\n'+
          '5 - импортировать  информацию из json\n'+
          '6 - экспортировать информацию в json\n'+
          '7 - импортировать  информацию из csv\n'+
          '8 - экспортировать информацию в scv\n'+
          'q - завершение работы.' )


def print_item_list(emp_list_as_dict):
    if len(emp_list_as_dict) == 0:
        print('Нет информации для отображения')
    else:
        # зададим ширину и наименование колонок
        col_name_as_dict = {el:m.PHONE_BOOK_PROP_DICT[el]['name'] for el in m.PHONE_BOOK_PROP_DICT.keys()}
        col_len_as_dict = {el:m.PHONE_BOOK_PROP_DICT[el]['len'] for el in m.PHONE_BOOK_PROP_DICT.keys()}
        sep = '|'
        # определим максимальную ширину каждого в словаре для печати
        # for dict_key in enumerate(emp_list_as_dict[0].keys()):
        #     col_len_as_dict[dict_key] = max([len(el[dict_key]) for  el in emp_list_as_dict])
        # напечатаем шапку
        print((' ' + sep + ' ').join([f'{col_name_as_dict[key]:<{col_len_as_dict[key]}}' for key in col_name_as_dict.keys()]))
        # напечатаем тело таблицы
        for el in emp_list_as_dict:
            print((' ' + sep + ' ').join([f'{el[key]:<{col_len_as_dict[key]}}' for key in col_name_as_dict.keys()]))


def get_action():
    action = input('')
    return action

def get_item_el_info(info_type):
    r = input(f'Укажите {info_type} :')
    return r

def get_new_item():
    emp_as_dict = {}
    for el in m.PHONE_BOOK_PROP_DICT.keys():
        if not m.PHONE_BOOK_PROP_DICT[el]['dbprop']['constraint'] \
            or  'AUTOINCREMENT' not in m.PHONE_BOOK_PROP_DICT[el]['dbprop']['constraint'] :
            emp_as_dict[el] = get_item_el_info(m.PHONE_BOOK_PROP_DICT[el]['name'])
            if m.PHONE_BOOK_PROP_DICT[el]['type'] == 'INT':
                emp_as_dict[el] = int(emp_as_dict[el])
            elif m.PHONE_BOOK_PROP_DICT[el]['type'] == 'STR':
                emp_as_dict[el] = emp_as_dict[el].strip()
    return emp_as_dict
