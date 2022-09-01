import config
import psycopg2
message = {
    'start':
'''Приветствую тебя пользователь.
Ты зашел к боту для сбора фотографий для сервиса анализа заболеваний агрокультур.
Для того чтобы получить дополнительную информацию о моей работе обратить к команде /help ''',

    'help':
'''/info - Для получения информации о ФАНЦ РД
/worker - для получения информации о том как я работаю
/reference - для получения рекомендация о том как нужно фотографировать''',

    'info':
'''Рад приветствовать вас от имени ФГБНУ «Федеральный аграрный научный центр Республики Дагестан». 
Здесь вы можете помочь в сборе материала для дальнейшего исследования заболеваемости агрокультур.
Более подробную информацию о нас вы можете узнать на нашем сайте: fancrd.ru''',

    'worker':
'''Я создан для сбора фотографий зараженной агрокультуры. 
В последующем наша организация будет создаст на основе этих фотографий программу которая по 
фотографии сможет определить болезнь агрокультуры и сможет дать вам рекомендации по решению проблем всязанных с данной болезнью
О том как желательно фотографировать /reference''',

    'reference':
'''
Правила
'''
}


def call_dialog_from_database():
    try:
        connection = psycopg2.connect(
            dbname=config.dbname,
            user=config.user,
            password=config.password,
            host=config.host
        )

        with connection.cursor() as cursor:
            cursor.execute(
                f'''INSERT INTO dialogs (start, help, info, worker, reference) VALUES 
                ('{message['start']}', '{message['help']}', '{message['info']}', '{message['worker']}', '{message['reference']}');''')
            connection.commit()

    except Exception as ex:
        print("Ошибка подключения к серверу")

    finally:
        if connection:
            connection.close()
            print("Подключение закрыто")
print(message['start'])
call_dialog_from_database()