from to_do_list.helpers.functional import functions
from to_do_list.data.entrences import dict_with_affairs
from to_do_list.source.available_tasks import part_name
from to_do_list.source.available_tasks import change_on_done_task
from to_do_list.source.available_tasks import change_priority
from to_do_list.source.available_tasks import delete_task
from to_do_list.source.available_tasks import all_plan_task
from to_do_list.source.available_tasks import sorted_plan_task
from to_do_list.source.available_tasks import not_complete_task
from to_do_list.source.available_tasks import complete_task
from to_do_list.source.available_tasks import overdue_task
from to_do_list.source.available_tasks import statistic
from to_do_list.source.available_tasks import test_data
from to_do_list.data.all_for_json import create_json
from to_do_list.data.all_for_json import print_json
from to_do_list.source.available_tasks import append_on_csv_file
import time
import datetime


def screen_clear():
    '''Очистити єкран'''
    print('\n' * 10)
    time.sleep(1)


def my_time(date):
    '''Перевоl дати у коректний вид'''
    date = date.split('-')
    while True:
        year = date[0]
        month = date[1]
        day = date[2]
        hour = date[3]
        minutes = date[4]
        right_time = datetime.datetime(int(year), int(month), int(day), int(hour), int(minutes))
        return right_time.strftime('%d/%m/%Y %H:%M')


def title(long):
    '''Максимальна довжина розділу title 50 символів'''
    if len(long) > 50:
        return long[:51]


def done_or_plane():
    answer = input('Cправа виконана/запланована - ').lower()
    while True:
        if answer == 'виконана':
            return True
        elif answer == 'запланована':
            return False
        else:
            answer = input('Введіть коректну відповідь(виконана/запланована) -  ')


def test_desciption(desc):
    while True:
        if len(desc) > 0:
            break
        else:
            desc = input('Опис справи обов`язковий - ')
    return desc


def priority(priorities):
    '''Перевірка на коректний пріоритет від 1 до 10'''
    while True:
        if 11 > int(priorities) > 0:
            break
        else:
            priorities = int(input('Введіть коректну пріоритетність(1-10) - '))
    return priorities


def input_info():
    input_dict = {}
    input_dict['id'] = len(dict_with_affairs) + 1
    input_dict['title'] = title(str(input("Коротка назва справи(необов`язково) - ")))
    input_dict['description'] = test_desciption(input('Опис справи - '))
    if not input_dict['title']:
        input_dict['title'] = input_dict['description']
    input_dict['priority'] = priority(input('Пріорітет справи(1-10]) - '))
    input_dict['due_date'] = my_time(input('До якого числа запланована справа(РРРР-ММ-ДД-ГОД-ХВ) - '))
    input_dict['done'] = done_or_plane()

    dict_with_affairs.append(input_dict)


def perfomance_func(button):
    if button == 'a':
        input_info()
        print(dict_with_affairs)
    elif button == 'b':
        part_name()
    elif button == 'c':
        change_on_done_task()
    elif button == 'd':
        change_priority()
    elif button == 'e':
        delete_task()
    elif button == 'f':
        all_plan_task()
    elif button == 'g':
        sorted_plan_task()
    elif button == 'h':
        not_complete_task()
    elif button == 'i':
        complete_task()
    elif button == 'j':
        overdue_task()
    elif button == 'k':
        statistic()
    elif button == 'l':
        test_data()
    elif button == 'm':
        append_on_csv_file()





def choose_function(button):
    while True:
        if button == 'n':
            create_json(dict_with_affairs)
            print_json()
            break
        else:
            perfomance_func(button)
            functions()
            button = input('Виберіть функцію - ')
