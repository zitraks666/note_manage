
def note():
    username = input('Введите имя: ')
    title = input('Введите заголовок: ')
    content = input('Напишите заметку: ')
    created_day=input('Введите дату создания(день-месяц-год): ')
    temp_created_date=created_day[0:5]
    issue_date = input('Введите дедлайн(день-месяц-год): ')
    temp_issue_date=created_day[0:5]
    print(f'\nВаше имя: {username} \nЗаголовок заметки: {title} \n аметка: {content} \nДата создания:{temp_created_date} \nДедлайн:{temp_issue_date}', sep='\n')
note()





