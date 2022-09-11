# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке
# строк некое число.

import random

file_content = ''
with open('./L2_S1_HW/fish_text.txt', 'r', encoding="utf8") as f:
    for l in f.readline():
        file_content = file_content + l
    f.close
file_content_split = file_content.split(' ')
for i in range(20):
    s = str(random.randint(1,999))
    el_num = random.randint(0,len(file_content_split)-1)
    if len(file_content_split[el_num]) >= len(s):
        print(s)
        if len(file_content_split[el_num]) == len(s):
            pos = 0
        else:
            pos = random.randint(0,len(file_content_split[el_num])-1-len(s))
        file_content_split[el_num] = file_content_split[el_num][:pos] + s + file_content_split[el_num][pos+len(s):]
# print(file_content_split)

ss = input('Укажите искомое число :')
for file_content_split_item in file_content_split:
    if file_content_split_item.find(ss) != -1:
        # break
        pass
print(f'I am find! it in {file_content_split_item}!')





