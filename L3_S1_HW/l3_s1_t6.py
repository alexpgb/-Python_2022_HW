# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.



file_source_txt = './L3_S1_HW/fish_text.txt'
file_result_rle = './L3_S1_HW/fish_text.rle'
file_result_txt = './L3_S1_HW/fish_text_rest.txt.'
file_content_txt = ''
p = 0
block_len = 9
with open(file_source_txt, 'r', encoding="utf8") as f:
    for l in f:
        file_content_txt += l
# file_content_txt = '1222222222222333444455555666666777777788888888'
flag = True
with open(file_result_rle, 'w', encoding="utf8") as f: 
    while p < len(file_content_txt):
        block_size = 0
        s = file_content_txt[p:p+1]
        while p + block_size < len(file_content_txt):
            if s == file_content_txt[p + block_size + 1:p + block_size + 2] and block_size < block_len:
                block_size += 1
            else:
                f.write(s + str(block_size))
                p += (block_size + 1)
                break
print(f'Файл {file_result_rle} создан.')

block_len = 2
file_content_txt = ''
with open(file_result_rle, 'r', encoding="utf8") as f:
    while True:
        s = f.read(block_len)
        if len(s) == 0:
            break
        print(s[0] * int(s[1]), end='')
        file_content_txt += s[0] * (int(s[1])+1)


print(file_content_txt)
with open(file_result_txt, 'w', encoding="utf8") as f:
    f.write(file_content_txt)
print(f'Файл {file_result_txt} создан.')
