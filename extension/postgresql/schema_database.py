from sqlalchemy import create_engine, Table, MetaData, ForeignKey, Column, Integer, Boolean, String, DateTime, select
from config import DB_NAME, USER_DB, PASSWORD_DB, HOST, SQL_TYPE, PORT_DB
from extension.postgresql.data.dialogs import dialogs_on_language

print('''
Запуск создания базы данных для работы бота и сервера.
При первом запуске необходимо создать таблицы в базе данных.
''')


class Database_processing():
    def __init__(self):
        self.meta = MetaData()

        self.users = Table(
            'users', self.meta,
            Column('user_id', Integer, primary_key=True),
            Column('is_bot', Boolean),
            Column('first_name', String(250)),
            Column('username', String(50)),
            Column('language_code', String(3)),
            Column('first_connect', DateTime)
        )
        self.materials = Table(
            'materials', self.meta,
            Column('user_id', Integer, ForeignKey('users.user_id')),
            Column('id_material', String(250)),
            Column('created_datetime', DateTime),

        )

        self.dialogs_bot = Table(
            'dialogs_bot', self.meta,
            Column('language', String(2), primary_key=True),
            Column('greeting', String(500)),
            Column('reference', String(500)),
            Column('donation', String(500)),
            Column('information', String(500)),
        )

        # print('Таблицы БД сформированы')
        # Организация подлючения к БД

    def connect_to_db(self,
                      sql_type=SQL_TYPE,
                      user=USER_DB,
                      password=PASSWORD_DB,
                      host=HOST,
                      port=PORT_DB,
                      db_name=DB_NAME):

        if input('Подключится с настройками по умолчанию Y / N (настройки из config) - ').lower() in ('y', 'yes'):
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
        self.conn = self.engine.connect()

    def fill_db(self):
        # Загрузка таблицы на сервер
        if input('Сохранить таблицу на сервер Y / N - ').lower() in ('y', 'yes'):
            self.create_all_to_bd()

    def create_all_to_bd(self):
        self.connect_to_db()
        self.meta.create_all(self.engine)
        print("Загрузка таблиц на БД завершена")

    def clear_all_to_db(self):
        self.connect_to_db()
        self.meta.drop_all(self.engine)
        print('База данных очищена')

    def user_check(self, user_id):
        return bool(self.conn.execute(select(self.users).where(self.users.c.user_id == user_id)).fetchall())

    def fill_table(self):

        # fills data on dialogs table
        for lang in dialogs_on_language.keys():
            ins = self.dialogs_bot.insert().values(language=lang,
                                                   greeting=dialogs_on_language[lang]['greeting'],
                                                   reference=dialogs_on_language[lang]['reference'],
                                                   donation=dialogs_on_language[lang]['donation'],
                                                   information=dialogs_on_language[lang]['information'])
            print(ins)
            self.conn.execute(ins)