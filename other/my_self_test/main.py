# -*- coding: utf-8 -*-

import os
from random import randint

#import questions_and_answers
from other.my_self_test import questions_and_answers

def input_correct_value():
    correct_value = False
    while not correct_value:
        try:
            score = int(input())
            if 0 <= score < 6:
                correct_value = True
            else:
                print('Ваше число слишком большое. Ведите число от 0 до 5')
        except ValueError:
            print('Вы можете ввести только числа. Ведите число от 0 до 5')
    return score

def all_test(lst):
    all_score = 0
    for i  in lst:
        question, answer = i
        input(question)
        print("\nПравильный ответ: \n\t", answer, '\nОцените себя за этот вопрос по шкале от 0 до 5')
        num = input_correct_value()
        all_score += num
        os.system('cls')
    print(f"Вы набрали {all_score} из 50")

def select_a_rand_question(lst):
    i = randint(0, len(lst) - 1)
    our_question, our_answer = lst[i]
    print(our_question)
    input()
    print("\nПравильный ответ: \n", our_answer)

def add_question_and_answer(lst):
    question = input("Введите свой вопрос\n")
    answer = input("Введите свой ответ\n")
    lst.append((question, answer))
    return lst


if __name__ == '__main__':
    lst = questions_and_answers.new_list()
    start = True
    while start:
        print("""
        меню:
        "1" - выбрать случайный вопрос
        "2" - пройти весь тест
        "3" - пройти тест только по нужной теме
        "4" - добавить вопрос и ответ
        "5" - удалить вопрос и ответ
        "6" - найти вопрос по ключевым словам
        "7" Выйти \n""")
        num = input()
        if num == '1':
            select_a_rand_question(lst)
        elif num =='2':
            all_test(lst)
        elif num == '4':
            add_question_and_answer(lst)
        elif num == '7':
            start = False
        else:
            print("Введите число от 1 до 7")




    #select_a_rand_question(lst)
    #all_test(lst)

