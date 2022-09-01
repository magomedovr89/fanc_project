from bot.config import *
import psycopg2


try:
    connection  = psycopg2.connect(dbname=dbname,
                            user=user,
                            password=password,
                            host=host)
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
            id serial PRIMARY KEY,
            is_bot boolean,
            first_name varchar(50), 
            username varchar(50), 
            language_code varchar(3), 
            is_premium boolean);"""
        )
        print('asdf')
        connection.commit()


except Exception as ex:
    print("Ошибка подключения к серверу")
finally:
    if connection:
        connection.close()
        print("Подключение закрыто")