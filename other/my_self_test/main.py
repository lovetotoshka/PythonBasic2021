# -*- coding: utf-8 -*-

import os
from random import randint
import nltk
import re

# import questions_and_answers
# from PythonBasic2021.other.my_self_test import questions_and_answers
from other.my_self_test import questions_and_answers


def input_value_from_x_to_y(x=0, y=5):
    correct_value = False
    while not correct_value:
        try:
            score = int(input())
            if x <= score <= y:
                correct_value = True
            else:
                print(f'Ваше число слишком большое. Ведите число от {x} до {y}')
        except ValueError:
            print(f'Вы можете ввести только числа. Ведите число от {x} до {y}')
    return score


def select_topic_and_our_func(func):
    def inner():
        print("\nКакая тема Вас интересует?\n'1' - topic_1\n'2' - topic_2 ")
        topic = str(input_value_from_x_to_y(1, 2))
        func('topic_' + topic)

    return inner  # убрала скобки


@select_topic_and_our_func
def all_test_on_the_right_topic(topic):
    all_score = 0
    lst = questions_and_answers.all_questions[topic]['questions']
    for i, question in enumerate(lst):
        print(f"Вопрос №{i + 1}")
        input(question)
        answer = questions_and_answers.all_questions[topic]['answers'][i]
        print("\nПравильный ответ: \n\t", answer, '\nОцените себя за этот вопрос по шкале от 0 до 5')
        num = input_value_from_x_to_y(0, 5)
        all_score += num
        os.system('cls')
    print(f"Вы набрали {all_score} из {len(lst) * 5}")


def all_test(lst):
    all_score = 0
    for i in lst:
        question, answer = i
        input(question)
        print("\nПравильный ответ: \n\t", answer, '\nОцените себя за этот вопрос по шкале от 0 до 5')
        num = input_value_from_x_to_y(0, 5)
        all_score += num
        os.system('cls')
    print(f"Вы набрали {all_score} из 50")


@select_topic_and_our_func
def select_a_rand_question_in_necessary_topic(topic):
    questions = questions_and_answers.all_questions[topic]['questions']
    i = randint(0, len(questions) - 1)
    print(questions[i])
    input()
    our_answer = questions_and_answers.all_questions[topic]['answers'][i]
    print("\nПравильный ответ: \n", our_answer)


def select_a_rand_question(lst):
    i = randint(0, len(lst) - 1)
    our_question, our_answer = lst[i]
    print(our_question)
    input()
    print(repr("\nПравильный ответ: \n", our_answer))


def add_question_and_answer(lst):
    question = input("Введите свой вопрос\n")
    answer = input("Введите свой ответ\n")
    lst.append((question, answer))
    return lst


@select_topic_and_our_func
def add_question_and_answer_to_topic(topic):
    question = input("Введите свой вопрос \n")
    answer = input("Введите свой ответ \n")
    questions_and_answers.all_questions[topic]['questions'] += [question]
    questions_and_answers.all_questions[topic]['answers'] += [answer]


@select_topic_and_our_func
def remove_question_and_answer_from_topic(topic):
    print("Введите номер вопроса")
    num = input_value_from_x_to_y(1, len(questions_and_answers.all_questions[topic]['questions']))
    questions_and_answers.all_questions[topic]['questions'].pop(num - 1)
    questions_and_answers.all_questions[topic]['answers'].pop(num - 1)


def clean(text):
    cleaned_text = ''
    for char in text.lower():
        if char in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz ':
            cleaned_text += char
    return cleaned_text


def get_a_suitable_question(in_text):
    all_q = []  # list of all questions
    for topic in questions_and_answers.all_questions.keys():
        for question in questions_and_answers.all_questions[topic]['questions']:
            question = clean(question)
            list_of_words = re.findall(r'\w+', question)
            text2 = clean(in_text)
            for text1 in list_of_words:
                if nltk.edit_distance(text1, text2) / max(len(text1), len(text2)) < 0.4:
                    all_q += [question]
    if all_q == []:
        return 'Не удалось определить вопрос'
    else:
        return all_q


def find_a_question_by_keywords():
    word = input("Введите ключевое слово")
    question = get_a_suitable_question(word)
    if question == 'Не удалось определить вопрос':
        print("Извините, я не могу найти вопрос с таким словом")
    else:
        for i, n in enumerate(question):
            print(f"{i}) {n}")


@select_topic_and_our_func
def show_all_questions_in_topic(topic):
    for n, item in enumerate(questions_and_answers.all_questions[topic]['questions']):
        print(f"{n}) {item}")



def show_menu_and_select_an_action():
    print("""
       ||================================================||
       || меню:                                          ||
       || "1" - выбрать случайный вопрос из нужной темы  ||
       || "2" - пройти весь тест                         ||
       || "3" - пройти тест только по нужной теме        ||
       || "4" - добавить вопрос и ответ                  ||
       || "5" - удалить вопрос и ответ по номеру         ||
       || "6" - найти вопрос по ключевому слову          ||
       || "7" - Вывести список вопросов по теме          ||
       || "8" - Выйти                                    ||
       ||================================================||\n""")
    num = input_value_from_x_to_y(1, 8)
    return num


if __name__ == '__main__':
    lst = questions_and_answers.new_list()
    start = True
    while start:
        num = str(show_menu_and_select_an_action())
        if num == '1':
            select_a_rand_question_in_necessary_topic()
        elif num == '2':
            all_test(lst)
        elif num == '3':
            all_test_on_the_right_topic()
        elif num == '4':
            add_question_and_answer_to_topic()
        elif num == '5':
            remove_question_and_answer_from_topic()
        elif num == '6':
            find_a_question_by_keywords()
        elif num == '7':
            show_all_questions_in_topic()
        elif num == '8':
            start = False


'''
1) нужно записать вопросы по правильным топикам - общее
2) найти вопрос по ключевым словам - готово
3) удалить пару ключ - значение из словаря - сделано для вопроса по номеру, лучше сделать по ключевым словам и 
   добавить изменение ответа на вопрос
4) сделать возможность пройти весь тест с помощью словаря
5) создать файл с ответами и вопросами

'''
