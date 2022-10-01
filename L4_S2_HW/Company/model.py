
import os.path
import json

EMP_LIST = []
EMP_PROP_DICT = {"id":{"name":"ИД", "len":5, "type":"int"},
                 "firstName":{"name":"Фамилия", "len":15, "type":"str"},
                 "position": {"name":"Должность", "len":15, "type":"str"},
                 "salary":{"name":"Зарплата", "len":5, "type":"int"}}
FILE_NAME = './L4_S2_HW/company.json'

def read_json():
    if not os.path.isfile(FILE_NAME):
        print(f'Файл не существует {FILE_NAME}')
    else:
        with open(FILE_NAME, 'r') as f:
            global EMP_LIST
            EMP_LIST = json.load(f)
    return True

def add_emp_to_list(emp_as_dict):
    EMP_LIST.append(emp_as_dict) 

def find_person_by_id(id):
    r = []
    r = [el for el in EMP_LIST if el['id'] == id]
    return r

def find_person_by_first_name(name):
    r = []
    r = [el for el in EMP_LIST if el['firstName'] == name]
    return r

def save_json():
    with open(FILE_NAME, 'w') as f:
        json.dump(EMP_LIST, f)
    print(f'Файл {FILE_NAME} сохранен.')


read_json()



