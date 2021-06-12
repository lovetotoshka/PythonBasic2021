"""
Домашнее задание №1
Функции и структуры данных
"""
def power_numbers(*args):
    lst = []
    numbers = args
    print(numbers)
    gen = (val**2 for val in numbers)
    return(list(gen))
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):
        if num ==1:
            return False
        if num % 2 == 0:
            return num == 2
        i = 3
        while i * i <= num and num % i != 0:
            i += 2
        return i * i > num

def filter_numbers(lst, param):
    if param == ODD:
        return list(filter(lambda x: x % 2 != 0, lst))
    if param == EVEN:
        return list(filter(lambda x: x % 2 == 0, lst))
    if param == PRIME:
        return list(filter(lambda x: is_prime(x), lst))
