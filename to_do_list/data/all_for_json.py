import os
import json


def file_path():
    cwd = os.getcwd()
    file_line = os.path.join(cwd, 'data', 'tasks.json')
    return file_line


def create_json(task):
    with open(file_path(), 'w') as file:
        json.dump(task, file)
        file.close()

def print_json():
    if os.path.exists(file_path()) is False:
        print('Немає файлa типу .json, перезапустіть программу для його створення')
    else:
        print('Файл успішно збережено')