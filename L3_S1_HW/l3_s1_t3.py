# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# Алгоритм:
# 1. Используем файл fish_text.txt как источник текста.
# 2. Вставим в случайные слова в случайном месте искомый текст 'абв'
# 3. Найдем и удалим эти слова из текста.

import random

file_content = ''
s = 'абв'
with open('./L2_S1_HW/fish_text.txt', 'r', encoding="utf8") as f:
    for l in f.readlines():
        file_content = file_content + l
    f.close
file_content_split = file_content.split(' ')
for i in range(20):         
    el_num = random.randint(0,len(file_content_split)-1)
    if len(file_content_split[el_num]) >= len(s):
        if len(file_content_split[el_num]) == len(s):
            pos = 0
        else:
            pos = random.randint(0,len(file_content_split[el_num])-1-len(s))
        file_content_split[el_num] = file_content_split[el_num][:pos] + s + file_content_split[el_num][pos+len(s):]
# print(file_content_split)
file_content = ' '.join(file_content_split)
file_content = file_content.replace(',', ' ,')  # Выделим знаки препинания, чтобы они не удалились вместе со словами.
file_content = file_content.replace('.', ' .')
print(file_content)
file_content_result = ' '.join([el for el in file_content.split(' ') if s not in el])
file_content_result = file_content_result.replace(' ,', ',')  # Вернем обратно знаки препинания
file_content_result = file_content_result.replace(' .', '.')
print(file_content_result)
