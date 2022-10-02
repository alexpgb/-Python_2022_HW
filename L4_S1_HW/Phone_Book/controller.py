import model as m
import view_phone_book as v

def main():
    while True:
        v.print_main_menu()
        action = v.get_action()
        if action == '1':   # напечатать все элементы
            item_list = []
            item_list = m.get_item()
            v.print_item_list(item_list)
        elif action == '2':  # добавить элемент 
            item_as_dict = v.get_new_item()
            # item_as_dict = {'firstName': 'Ivanov', 'phoneNumber': '79998887761'}
            m.save_item_to_bd(item_as_dict)
        elif action == '3':  # найти элемент по номеру телефона
            el_name = 'phoneNumber'
            el_of_item = v.get_item_el_info(m.PHONE_BOOK_PROP_DICT[el_name]['name'])
            item_list = m.get_item({'phoneNumber': el_of_item})
            v.print_item_list(item_list)
        elif action == '4':  # найти элемент по наименованию
            el_name = 'firstName'
            el_of_item = v.get_item_el_info(m.PHONE_BOOK_PROP_DICT[el_name]['name'])
            item_list = m.get_item({'firstName': el_of_item})
            v.print_item_list(item_list)
        elif action == '5': # импортировать  информацию из json
            m.load_from_josn_to_bd()
        elif action == '6': # экспортировать информацию в json
            m.save_from_bd_to_json()
        elif action == '7': # импортировать  информацию из csv
            m.load_from_csv_to_bd()
        elif action == '8': # - экспортировать информацию в scv
            m.save_from_bd_to_csv()
        elif action == 'q':  # завершение работы
            m.CONNECTION.close()
            break

