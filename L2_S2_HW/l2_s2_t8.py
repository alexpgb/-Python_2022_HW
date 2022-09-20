# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача -
# сформировать файл, содержащий сумму многочленов.

# from l2_s2_t7 import polinom_from_dict_as_str
import l2_s2_t7 as l2

p_a = []
p1 = '-  38x**4 +  41x**3 -  20x**2 +  40x**1 +  12 = 0'
{0: (1, 12), 1: (1, 40), 2: (-1, 20), 3: (1, 41), 4: (-1, 38)}
p2 = '+  16x**6 +  2x**5 +  21x**4 +  5x**3 -  16x**1 -  26 = 0'
p3 = '+  16x**6 +  2x**5 +  21x**4 +  5x**3 -  16x -  26 = 0'
{0: (-1, 26), 1: (-1, 16), 2: (1, 0), 3: (1, 5), 4: (1, 21), 5: (1, 2), 6: (1, 16)}

def parse_polynom_as_str(p):
    r = {}
    l = []
    f = True
    p = ''.join(p.split())
    while f:
        # разберем многочлен на члены
        for i in range(len(p)):
            if p[i: i + 1] == '=': # нашли знак "="
                f = False
                break
            if p[i: i + 1] in ['+', '-']: # первый элемент отдельного члена
                for j in range(i + 1, len(p)):         # начинаем искать завершение члена 
                    if p[j : j + 1]  in ['+','-','=']:    # нашли конец
                        l.append(p[i:j]) 
                        if p[j:j + 1] == '=':
                            f= False
                        i = j + 1
                        break
            if f == False:          
                break
    # print(l)
    l = l[::-1]
    # print(l)
    s = ''
    k = ''
    if len(l) > 0:
        for i, el in enumerate(l):            # перебираем элементы списка 
            if 'x' in el:                     # не последний член многочлена
                if '*' in el:                 # не предпоследний член многочлена
                    el = el.replace('*', '')
                    el_as_list = el.split('x')
                    r[int(el_as_list[1])] = 1 if el_as_list[0][0] == '+' else -1 , int(el_as_list[0][1:])
                else:                          # Предпоследний член многочлена если последний 
                                               #член сформирован в виде +16x
                    el = el.replace('x', '')
                    r[1] = 1 if el[0] == '+' else -1 , int(el[1:])

            else:                               # последний член многочлена в виде - 26
                r[0] =  1 if el[0] == '+' else -1 ,  int(el[1:])
        pass
    return r


def polinoms_sum(polynom_as_dict1, polynom_as_dict2):
    r = {}
    for i in range(max(list(polynom_as_dict1.keys()) + list(polynom_as_dict2.keys()))):
        if i in polynom_as_dict1.keys() or i in polynom_as_dict2.keys():   # проверяем есть член степени i в обоих многочленах
            s = \
                (polynom_as_dict1[i][1] * polynom_as_dict1[i][0] if i in polynom_as_dict1.keys() else 0) +\
                (polynom_as_dict2[i][1] * polynom_as_dict2[i][0] if i in polynom_as_dict2.keys() else 0)
            
            r[i] = 1 if s >= 0 else -1, abs(s)
    return(r)

p_a.append(parse_polynom_as_str(p1))
p_a.append(parse_polynom_as_str(p2))
# сложение многочленов
result_polinom_as_dict = polinoms_sum(p_a[0], p_a[1])
result_polinom_as_str = l2.polinom_from_dict_as_str(result_polinom_as_dict)
print('\n'.join([p1, '+', p2, '-' * 20]))
print(result_polinom_as_str)
