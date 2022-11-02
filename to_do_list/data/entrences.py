from datetime import datetime
time = datetime(2022, 11, 1, 12, 37)
right_time = time.strftime('%d/%m/%Y %H:%M')
dict_with_affairs = [
    {
        'id' : 1,
        'title' : 'shopping',
        'description' : 'grossery shopping',
        'priority' : 4,
        'due_date' : right_time,
        'done' : False
    }
]
