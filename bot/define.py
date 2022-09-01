import psycopg2
import config


def call_dialog_from_database(command):
    try:
        connection = psycopg2.connect(
            dbname=config.dbname,
            user=config.user,
            password=config.password,
            host=config.host
        )

        with connection.cursor() as cursor:
            return cursor.execute(
                f'''INSERT INTO {}'''
            )

    except Exception as ex:
        print("Ошибка подключения к серверу")

    finally:
        if connection:
            connection.close()
            print("Подключение закрыто")

print(call_dialog_from_database('start'))