import model as m
import view_person as v

def main():
    while True:
        v.print_main_menu()
        action = v.get_action()
        if action == '1':   # напечатать список всех сотрудников
            v.print_emp_list(m.EMP_LIST)
        elif action == '2':  # добавить нового сотрудника
            emp_as_dict = v.get_new_employer()
            # emp_as_dict = {'id': 1, 'firstName': 'Ivanov', 'position': 'Head', 'salary': 10}
            m.add_emp_to_list(emp_as_dict) 
            m.save_json()
        elif action == '3':  # найти сотрудника по id
            id = int(v.get_emp_info(m.EMP_PROP_DICT['id']['name']))
            emp_list_filtered = m.find_person_by_id(id)
            v.print_emp_list(emp_list_filtered)
        elif action == '4':  # отфильтровать сотрудников по фамилии
            firstName = v.get_emp_info(m.EMP_PROP_DICT['firstName']['name']).strip()
            emp_list_filtered = m.find_person_by_first_name(firstName)
            v.print_emp_list(emp_list_filtered)
        elif action == 'q':  # завершение работы
            break




