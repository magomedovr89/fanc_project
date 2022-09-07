from sqlalchemy import create_engine, Table, MetaData, ForeignKey, Column, Integer, Boolean, String, DateTime, exists, \
    select
from pprint import pprint


class Database_processing():
    def __init__(self):
        self.meta = MetaData()
        self.users = Table('users', self.meta,
                           Column('user_id', Integer, primary_key=True),
                           Column('is_bot', Boolean),
                           Column('first_name', String(250)),
                           Column('username', String(50)),
                           Column('language_code', String(3)),
                           Column('first_connect', DateTime)
                           )
        self.materials = Table('materials', self.meta,
                               Column('user_id', Integer, ForeignKey('users.user_id')),
                               Column('id_material', String(250)),
                               Column('created_datetime', DateTime),
                               )
        print('Таблицы БД сформированы')
        # Организация подлючения к БД
        if input('Подключится с настройками по умолчанию Y / N (настройки из config) - ').lower() in ('y', 'yes'):
            self.connect_to_db()
        else:
            self.connect_to_db(sql_type=input('Введите тип БД (postgresql - по умолчанию) - '),
                               user=input('Введите имя пользователя БД (postgres - По умолчанию) - '),
                               password=input('Введите пароль (123123 - По умолчанию) - '),
                               host=input("Введите хост - (localhost - По умолчанию) - "),
                               port=input("Введите порт - (5432 - По умолчанию) - "),
                               db_name=input("Введите имя БД - (all - По умолчанию) - "))
        # Загрузка таблицы на сервер
        if input('Сохранить таблицу на сервер Y / N - ').lower() in ('y', 'yes'):
            self.create_all_to_bd()


    def connect_to_db(self,
                      sql_type='postgresql',
                      user='postgres',
                      password='123123',
                      host='localhost',
                      port='5432',
                      db_name='all'):
        try:
            self.conn = self.engine = create_engine((f''
                                                     f'{sql_type if sql_type else "postgresql"}://'
                                                     f'{user if user else "postgres"}:'
                                                     f'{password if password else "123123"}@'
                                                     f'{host if host else "localhost"}:'
                                                     f'{port if port else "5432"}/'
                                                     f'{db_name if db_name else "all"}'), echo=False)
            print('Подключение успешно.')
        except Exception as ex:
            print("Ошибка подключения, проверьте параметры")

    def create_all_to_bd(self):
        self.meta.create_all(self.engine)
        print("Загрузка таблиц на БД завершена")
        # self.conn = self.engine.connect()

    def clear_all_to_db(self):
        self.meta.drop_all(self.engine)
        print('База данных очищена')

    def user_check(self, user_id):
        return bool(self.conn.execute(select(self.users).where(self.users.c.user_id == user_id)).fetchall())


db = Database_processing()


# meta.drop_all(engine)
# ins_first_user = users.insert().values(user_id='1233',
#                                        is_bot=1,
#                                        first_name='Magomedov',
#                                        username='Ruslan',
#                                        language_code='ru',
#                                        first_connect='02.09.1989')
# # conn.execute(ins_first_user)
#
# print('begin')
# def table_exists(name):
#     ret = engine.dialect.has_table(engine, name)
#     print('Table "{}" exists: {}'.format(name, ret))
#     return ret
# print(table_exists(users))
# print('end')


# Запрос на наличие пользователя в базе данных


