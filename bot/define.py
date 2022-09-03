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
                f'''INSERT INTO'''
            )

    except Exception as ex:
        print("Ошибка подключения к серверу")

    finally:
        if connection:
            connection.close()
            print("Подключение закрыто")


def user_data_to_database(user_info):
    try:
        connection = psycopg2.connect(
            dbname=config.dbname,
            user=config.user,
            password=config.password,
            host=config.host
        )

        with connection.cursor() as cursor:
            print(is_exists(table='users', row='id', meaning=user_info.id), 'ответ')
            if is_exists(table='users', row='id', meaning=user_info.id):
                cursor.execute(f'''
                UPDATE
                users
                id = '{user_info.id}',
                is_bot = '{user_info.is_bot}',
                first_name = {user_info.first_name}',
                username = '{user_info.username}',
                language_code = '{user_info.language_code}';
                ''')
                connection.commit()
            else:
                cursor.execute(f'''
                INSERT INTO users 
                (
                id, 
                is_bot, 
                first_name, 
                username, 
                language_code
                ) 
                VALUES 
                (
                '{user_info.id}', 
                '{user_info.is_bot}', 
                '{user_info.first_name}', 
                '{user_info.username}', 
                '{user_info.language_code}');''')
                connection.commit()

    except Exception as ex:
        print("Ошибка подключения к серверу")

    finally:
        if connection:
            connection.close()
            print("Подключение закрыто")


def is_exists(table, row, meaning):
    try:
        connection = psycopg2.connect(
            dbname=config.dbname,
            user=config.user,
            password=config.password,
            host=config.host
        )

        with connection.cursor() as cursor:
            cursor.execute(
                f'''SELECT EXISTS (SELECT * FROM {table} WHERE {row} = '{meaning}');'''
            )
            return cursor.fetchone()[0]


    except Exception as ex:
        print("Ошибка подключения к серверу")

    finally:
        if connection:
            connection.close()
            print("Подключение закрыто")