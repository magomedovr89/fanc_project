from sqlalchemy import create_engine, select, inspect
from config import DB_NAME, USER_DB, PASSWORD_DB, HOST, SQL_TYPE, PORT_DB
from datetime import datetime

class Database_primary_executor():
    # При инициализации класса происходит автоматическое соединение с сервером с помощью настроек из config

    def __init__(self, sql_type=SQL_TYPE, user=USER_DB, password=PASSWORD_DB, host=HOST, port=PORT_DB, db_name=DB_NAME):

        if True:  # input('Подключится с настройками по умолчанию Y / N (настройки из config) - ').lower() in ('y', 'yes'):
            try:
                self.engine = create_engine((f''
                                             f'{sql_type if sql_type else SQL_TYPE}://'
                                             f'{user if user else USER_DB}:'
                                             f'{password if password else PASSWORD_DB}@'
                                             f'{host if host else HOST}:'
                                             f'{port if port else PORT_DB}/'
                                             f'{db_name if db_name else DB_NAME}'), echo=False)
                print('Подключение успешно.')
            except Exception as ex:
                print("Ошибка подключения, проверьте параметры")
        else:
            try:
                sql_type = input('Введите тип БД (postgresql - по умолчанию) - ')
                user = input('Введите имя пользователя БД (postgres - По умолчанию) - ')
                password = input('Введите пароль (123123 - По умолчанию) - ')
                host = input("Введите хост - (localhost - По умолчанию) - ")
                port = input("Введите порт - (5432 - По умолчанию) - ")
                db_name = input("Введите имя БД - (all - По умолчанию) - ")
                self.engine = create_engine((f''
                                             f'{sql_type if sql_type else SQL_TYPE}://'
                                             f'{user if user else USER_DB}:'
                                             f'{password if password else PASSWORD_DB}@'
                                             f'{host if host else HOST}:'
                                             f'{port if port else PORT_DB}/'
                                             f'{db_name if db_name else DB_NAME}'), echo=False)
                print('Подключение успешно.')
            except Exception as ex:
                print("Ошибка подключения, проверьте параметры")
        self.connected = self.engine.connect()

    def check_db_base(self, table, column):
        inspector = inspect(self.engine)
        print((inspector.get_columns(table, schema='public')[0]['name']))
        return table == (inspector.get_columns(table, schema='public')[0]['name'])

    def extract(self, table, column, column_key, key_value):
        return \
            self.connected.execute(f'SELECT {column} FROM {table} WHERE "{column_key}" = \'{key_value}\'').fetchone()[0]

    def user_check(self, user_id):
        return self.connected.execute(f'SELECT EXISTS (SELECT * FROM users WHERE user_id = {user_id})').fetchone()[0]

    def insert_user_info(self, arr):
        if self.user_check(arr.id):
            self.connected.execute(f'UPDATE users '
                                   f'SET '
                                   f'language_code=\'{arr.language_code}\', '
                                   f'first_name = \'{arr.first_name}\', '
                                   f'username = \'{arr.username}\' '
                                   f'WHERE user_id = \'{arr.id}\'')
        else:
            self.connected.execute(f'INSERT INTO users '
                                   f'(user_id, is_bot, first_name, username, language_code, first_connect) '
                                   f'VALUES '
                                   f'(\'{arr.id}\', '
                                   f'\'{1 if arr.is_bot else 0}\', '
                                   f'\'{arr.first_name}\', '
                                   f'\'{arr.username}\', '
                                   f'\'{arr.language_code}\', '
                                   f'\'{datetime.now()}\')')
