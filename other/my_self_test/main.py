# -*- coding: utf-8 -*-

import os
from random import randint

#import questions_and_answers
from other.my_self_test import questions_and_answers


def all_test(lst):
    all_score = 0
    for i  in lst:
        question, answer = i
        print(question)
        input()
        print("\nПравильный ответ: \n\t", answer)
        print("Оцените себя за этот вопрос по шкале от 0 до 5")
        correct_value = False
        while not correct_value:
            try:
                score = int(input())
                if 0 <= score < 6:
                    correct_value = True
                    all_score += score
                else:
                    print('Ваше число слишком большое. Ведите число от 0 до 5')
            except ValueError:
                print('Вы можете ввести только числа. Ведите число от 0 до 5')
        os.system('cls')
    print(f"Вы набрали {all_score} из 50")

def select_a_rand_question(lst):
    i = randint(0, len(lst) - 1)
    our_question, our_answer = lst[i]
    print(our_question)
    input()
    print("\nПравильный ответ: \n", our_answer)


if __name__ == '__main__':
    #new_lst = questions_and_answers.new_list
    lst = questions_and_answers.new_list()
    #select_a_rand_question(lst)
    all_test(lst)

