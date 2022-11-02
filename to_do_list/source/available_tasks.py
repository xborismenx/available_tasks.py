import datetime

from to_do_list.data.entrences import dict_with_affairs
from operator import itemgetter
import csv
import os

def priority(priorities):
    '''Перевірка на коректний пріоритет від 1 до 10'''
    while True:
        if 11 > int(priorities) > 0:
            break
        else:
            priorities = int(input('Введіть коректну пріоритетність(1-10) - '))
    return priorities


def right_print(entry):
    '''Print entry of todo list in normal view'''
    print()
    for key in entry:
        print(key,'-', entry[key])
    print()


def part_name():
    '''Знайти назву справи за початком слова'''
    print()
    part_of_name = input('Введіть початкову частину справи - ')
    for dicts in dict_with_affairs:
        for value in dicts.values():
            if str(value).startswith(part_of_name):
                print(dicts)
    else:
        print('Ввід некоректний або немає такої справи')
    print()

def change_on_done_task():
    '''Змінити справу з запланованої на виконану'''
    print()
    find_task = input('Знайти справу по id або назві справи(id/назва) -  ').lower()
    if find_task == 'id':
        find_on_id = int(input('Введіть id - '))
        for task in dict_with_affairs:
            if task['id'] == find_on_id:
                task['done'] = True
    elif find_task == 'назва':
        find_on_name = input('Введіть назву - ').lower()
        for task in dict_with_affairs:
            if task['title'].startswith(find_on_name):
                task['done'] = True
    else:
        print('Помилка вводу,спробуйте ще')
    print()

def change_priority():
    '''Змінити пріоритет у справі'''
    print()
    input_priority = input('Знайти справу по id або назві справи(id/назва) -  ').lower()
    if input_priority == 'id':
        find_on_id = int(input('Введіть id - '))
        for task in dict_with_affairs:
            if task['id'] == find_on_id:
                task['priority'] = priority(input('Введіть пріоритет - '))
    elif input_priority == 'назва':
        find_on_name = input('Введіть назву - ')
        for task in dict_with_affairs:
            if task['title'].startswith(find_on_name):
                task['priority'] = priority(input('Введіть пріоритет - '))
    else:
        print('Помилка вводу,спробуйте ще')
    print()

def delete_task():
    '''Видалити справу'''
    print()
    input_key_task = input('Знайти справу по id або назві справи(id/назва) -  ').lower()
    if input_key_task == 'id':
        input_id = int(input('Введіть id - '))
        for task in dict_with_affairs:
            if task['id'] == input_id:
                task.clear()
    elif input_key_task == 'назва':
        input_name = input('Введіть назву - ')
        for task in dict_with_affairs:
            if task['title'].startswith(input_name):
                task.clear()
    else:
        print('Помилка вводу,спробуйте ще')
    print()

def all_plan_task():
    print()
    for task in dict_with_affairs:
        if task['done'] is False:
            print(task['title'])
    print()


def sorted_plan_task():
    '''Відсортовані за пріорітетом справи(за спаданням)'''
    print()
    sorted_priority = sorted(dict_with_affairs ,  key=lambda d: int(d['priority']),reverse=True)
    for key in sorted_priority:
        print(key['title'])
    print()


def not_complete_task():
    '''Перевірка на ще не виконану справу'''
    print()
    for task in dict_with_affairs:
        if task['done'] is False:
            print(task['title'])
        else:
            print('Немає не виконаних справ')
    print()

def complete_task():
    '''Перевірка на виконану справу'''
    print()
    for task in dict_with_affairs:
        if task['done'] is True:
            print(task['title'])
        else:
            print('Немає виконаних справ')
    print()

def overdue_task():
    print()
    for task in dict_with_affairs:
        if datetime.datetime.strptime(task['due_date'],'%d/%m/%Y %H:%M') <= datetime.datetime.now():
            print(task['title'])
        else:
            print('Немає просрочених справ')
    print()

def statistic():
    print()
    all_task = len(dict_with_affairs)
    not_complete = 0
    complete = 0
    overdue = 0
    for task in dict_with_affairs:
        if task['done'] is False:
            not_complete += 1
        elif task['done'] is True:
            complete += 1
        elif datetime.datetime.strptime(task['due_date'], '%d/%m/%Y %H:%M') <= datetime.datetime.now():
            overdue += 1
    print(f'Кількість усіх справ - {all_task},Виконаних - {complete},Не виконаних - {not_complete},'
          f'Прострочених - {overdue}')
    print()


def test_data():
    print()
    for task in dict_with_affairs:
        for key,data in task.items():
            print(key,'-',data)
        print()


def append_on_csv_file():
    keys = ['id', 'title', 'description', 'priority', 'due_date', 'done']
    cwd = os.getcwd()
    file_line = os.path.join(cwd, 'data', 'tasks.csv')
    with open(file_line, 'w') as file:
        wr = csv.DictWriter(file, fieldnames=keys)
        wr.writeheader()
        wr.writerows(dict_with_affairs)