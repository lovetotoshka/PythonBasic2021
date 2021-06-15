'''
* Задача 6
На входе имеем список строк разной длины. Необходимо написать 
функцию all_eq(lst), которая вернет новый список из строк 
одинаковой длины. Длину итоговой строки определяем исходя из 
самой большой из них. Если конкретная строка короче самой 
длинной, дополнить ее нижними подчеркиваниями с правого края
до требуемого количества символов.

Расположение элементов начального списка не менять.
'''

def all_eq(lst):
    
    d = len(lst[0])
    for i in lst:
        if len(i)>d:
            d = len(i)
    
    for i in lst:
        if len(i) < d:
            i += ((d - len(i))*'_')
            print (i)
    return lst


def all_eq_2(lst):
    
    d = len(lst[0])
    for i in lst:
        if len(i)>d:
            d = len(i)
    
    for n,i in enumerate(lst):
        if len(i) < d:
            lst[n] += ((d - len(i))*'_')
    return lst


def new_all_eq(lst):
    d = len(max(lst, key = lambda x: len(x)))
    return [item.ljust(d, '_') for item in lst]


str1 = ['a', 'bb', 'ccc', 'dddd', 'eeeee']
print(all_eq(str1))
str2 = ['A', 'BB', 'CCC', 'DDDD', 'EEEEE']
print(all_eq_2(str2))
str3 = ['1', '22', '333', '4444', '55555']
print(new_all_eq(str3))
