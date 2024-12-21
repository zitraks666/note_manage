from datetime import *

today_date=input('Введите сегодняшнюю дату(день-месяц-год): ')
today_date=datetime.strptime(today_date, '%d-%m-%Y').date()
def note():
    username = input('Введите имя: ')
    title = input('Введите заголовок: ')
    content = input('Напишите заметку: ')
    created_day=input('Введите дату создания(день-месяц-год): ')
    created_day = datetime.strptime(created_day, '%d-%m-%Y').date()
    issue_date = input('Введите дедлайн(день-месяц-год): ')
    issue_date=datetime.strptime(issue_date, '%d-%m-%Y').date()
    if today_date>issue_date:
        status=' НЕ Актуально'
    else:
        status='Актуально'

    print(status)
note()




