
# работа с менеджером контекста в SQLite:
# https://natenka.io/python/fluent-python-with-statement/

import sqlite3
import contextlib
import json
import csv
import os.path

PHONE_BOOK_LIST = []
PHONE_BOOK_PROP_DICT = \
    {"id":{"name":"ИД", "len":5, "type":"INT", "dbprop":{'type':'INTEGER', "constraint":'PRIMARY KEY AUTOINCREMENT'}},
    "firstName":{"name":"Фамилия", "len":15, "type":"STR", "dbprop":{'type':'TEXT', "constraint":None}},
    "phoneNumber": {"name":"Телефон", "len":11, "type":"STR", "dbprop":{'type':'TEXT', "constraint":None}}}
DB_NAME = r'./L4_S1_HW/Phone_Book/phone_book.db'
FILE_NAME_JSON_EXPORT = './L4_S1_HW/Phone_Book/phone_book_export.json'
FILE_NAME_JSON_IMPORT = './L4_S1_HW/Phone_Book/phone_book_import.json'
FILE_NAME_CSV_EXPORT = './L4_S1_HW/Phone_Book/phone_book_export.scv'
FILE_NAME_CSV_IMPORT = './L4_S1_HW/Phone_Book/phone_book_import.scv'


#@contextlib.contextmanager
#def sqlite3_connection(DB_NAME):
#    connection = sqlite3.connect(DB_NAME)
#    yield connection
#    connection.close()

def get_item(where_statment_as_dict=None):
    # where_statment_as_dict = {'id': 1, 'firstName': 'Jon', 'phoneNumber': '79998887766'}
    # where_statment_as_dict = {'firstName': 'Jon', 'phoneNumber': '79998887766'}
    # where_statment_as_dict = {'firstName': 'Jon'}
    # where_statment_as_dict = {'phoneNumber': '79998887766'}
    r = []
    sql_statment_select = 'SELECT ' +  ', '.join([key for key in PHONE_BOOK_PROP_DICT.keys()]) + ' FROM PHONE_BOOKS'
    if where_statment_as_dict is not None:
        where_statment_str = ' WHERE ' + ' AND '.join([(key + (' LIKE ' if PHONE_BOOK_PROP_DICT[key]['type'] == 'STR' else ' = ') + '?') for key in where_statment_as_dict.keys()])
        where_statment_param = tuple(('%'+where_statment_as_dict[key]+'%' if PHONE_BOOK_PROP_DICT[key]['type'] == 'STR' else where_statment_as_dict[key])  for key in where_statment_as_dict.keys()) 
    else:
        where_statment_str = ''
        where_statment_param = ()
    cursor = CONNECTION.cursor()
    if where_statment_as_dict:
        cur_select = cursor.execute(sql_statment_select+where_statment_str, where_statment_param)
    else:
        cur_select = cursor.execute(sql_statment_select)
    for el in cur_select:
        item_as_dict = {}
        for i, key in enumerate(PHONE_BOOK_PROP_DICT.keys()):
            item_as_dict[key] = el[i] 
        r.append(item_as_dict)
    cur_select.close()
    return r

def save_item_to_bd(item_as_dict):
    # item_as_dict = {'firstName': 'Jon', 'phoneNumber': '79998887766'}
    sql_statment_insert = 'INSERT INTO PHONE_BOOKS ('+ ', '.join([el for el in item_as_dict.keys()]) + ') VALUES (' + ', '.join(['?' for el in item_as_dict.keys()])+ ');'
    cursor = CONNECTION.cursor()
    cursor.execute(sql_statment_insert, tuple(el for el in item_as_dict.values()))
    CONNECTION.commit()
    cursor.close()


def save_from_bd_to_json():
    item_list = get_item()
    with open(FILE_NAME_JSON_EXPORT, 'w') as f:
        json.dump(item_list, f)
    print(f'Файл {FILE_NAME_JSON_EXPORT} сохранен.')

def save_from_bd_to_csv():
    item_list = get_item()
    with open(FILE_NAME_CSV_EXPORT, 'w', newline='', encoding='utf-8') as f:
        fieldnames = [key for key in PHONE_BOOK_PROP_DICT.keys()]
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval='', extrasaction='ignore', dialect='excel')
        writer.writeheader()
        for el in item_list:
            writer.writerow(el)
    print(f'Файл {FILE_NAME_CSV_EXPORT} сохранен.')

def load_from_josn_to_bd():
    if not os.path.isfile(FILE_NAME_JSON_IMPORT):
        print(f'Файл не существует {FILE_NAME_JSON_IMPORT}')
    else:    
        with open(FILE_NAME_JSON_IMPORT, 'r') as f:
            item_list = json.load(f)
            print(f'Файл {FILE_NAME_JSON_IMPORT} прочитан.')
            # item_as_dict = {'firstName': 'Jon', 'phoneNumber': '79998887766'}
            if len(item_list) > 0:
                cursor = CONNECTION.cursor()
                for item_as_dict in item_list:
                    item_as_dict_wo_id = {key: item_as_dict[key] for key in item_as_dict.keys() if key != 'id'}
                    sql_statment_insert = 'INSERT INTO PHONE_BOOKS ('+ ', '.join([el for el in item_as_dict_wo_id.keys()]) + ') VALUES (' + ', '.join(['?' for el in item_as_dict_wo_id.keys()])+ ');'
                    cursor.execute(sql_statment_insert, tuple(el for el in item_as_dict_wo_id.values()))
                CONNECTION.commit()
                cursor.close()

def load_from_csv_to_bd():
    if not os.path.isfile(FILE_NAME_CSV_IMPORT):
        print(f'Файл не существует {FILE_NAME_CSV_IMPORT}')
    else:
        with open(FILE_NAME_CSV_IMPORT, 'r', newline='') as f:
            reader = csv.reader(f, dialect='excel')
            for i, item_as_list in enumerate(reader):
                if i ==0:
                    headers_as_list = item_as_list
                else:
                    if i == 1:
                        cursor = CONNECTION.cursor()
                    item_as_dict_wo_id = {el: item_as_list[j] for j, el in enumerate(headers_as_list) if el != 'id'}
                    sql_statment_insert = 'INSERT INTO PHONE_BOOKS ('+ ', '.join([el for el in item_as_dict_wo_id.keys()]) + ') VALUES (' + ', '.join(['?' for el in item_as_dict_wo_id.keys()])+ ');'
                    cursor.execute(sql_statment_insert, tuple(el for el in item_as_dict_wo_id.values()))
            if i > 0:
                CONNECTION.commit()
            print(f'Из файла {FILE_NAME_CSV_IMPORT} прочитано {i} записей .')


# print()
CONNECTION = sqlite3.connect(DB_NAME)
cursor = CONNECTION.cursor()
# Создадим таблицу если ее нет.
table_definition = 'CREATE TABLE IF NOT EXISTS PHONE_BOOKS (' + ', '.join([(key + ' ' + PHONE_BOOK_PROP_DICT[key]['dbprop']['type'] +  (' ' + PHONE_BOOK_PROP_DICT[key]['dbprop']['constraint'] if PHONE_BOOK_PROP_DICT[key]['dbprop']['constraint'] else '')) for key in PHONE_BOOK_PROP_DICT.keys()]) + ')'
cursor.execute(table_definition)
CONNECTION.commit()
cursor.close()

# так не заработало выходит из контекста и БД закрывается.
# with sqlite3_connection(DB_NAME) as CONNECTION:
#     cursor = CONNECTION.cursor()
# #    table_definition = 'CREATE TABLE IF NOT EXISTS PHONE_BOOKS (' +  ', '.join([key + ' ' + PHONE_BOOK_PROP_DICT[key]['type']   for key in PHONE_BOOK_PROP_DICT.keys()]) + ')'
#     # Создадим таблицу если ее нет.
#     table_definition = 'CREATE TABLE IF NOT EXISTS PHONE_BOOKS (' + ', '.join([(key + ' ' + PHONE_BOOK_PROP_DICT[key]['dbprop']['type'] +  (' ' + PHONE_BOOK_PROP_DICT[key]['dbprop']['constraint'] if PHONE_BOOK_PROP_DICT[key]['dbprop']['constraint'] else '')) for key in PHONE_BOOK_PROP_DICT.keys()]) + ')'
#     cursor.execute(table_definition)
#     CONNECTION.commit()
#     cursor.close()
     



