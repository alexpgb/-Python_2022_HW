# 3 Напишите программу, которая определит позицию второго вхождения строки в списке либо # сообщит, что её нет.
# Пример: 
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

import random

file_content = ''
with open('./L2_S1_HW/fish_text.txt', 'r', encoding="utf8") as f:
    for l in f.readline():
        file_content = file_content + l
    f.close
file_content_split = file_content.split(' ')
for i in range(20):
    s = random.randint(1,999)
    el_num = random.randint(0,len(file_content_split)-1)
    file_content_split[el_num] = s
# print(file_content_split)
ss = input('Укажите искомую строку :')
n = 0
for i  in range(len(file_content_split)):
    if file_content_split[i] is str and file_content_split[i].find(ss) != -1:
        n += 1
        if n >= 2:
            print(f'I am find it in {file_content_split[i]} element index {i}! )')
            break
if n < 2:
    print(f'I am cannot find it (. -1')