import psycopg2
import config
from data.dialogs import message
import aiogram.utils.markdown as fmt


#  Попытка подключения к серверу Конфигурационный файл config.py
#  !!!Порт по умолчанию!!!
try:
    connection = psycopg2.connect(
        dbname=config.dbname,
        user=config.user,
        password=config.password,
        host=config.host
    )

    with connection.cursor() as cursor:
        cursor.execute(
                f'''INSERT INTO dialogs (lang, greeting) VALUES ('ru', '{message['ru']['greeting']}')'''
            )
        connection.commit()

except Exception as ex:
    print("Ошибка подключения к серверу")

finally:
    if connection:
        connection.close()
        print("Подключение закрыто")