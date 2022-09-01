#  Конфигурация сервера данных
dbname = 'all'
user = 'postgres'
password = '123123'
host = '127.0.0.1'


#  Создадим словарь для генерации запроса создания таблиц

table_dict = {
    'users':
        {
            'id': 'serial PRIMARY KEY',
            'is_bot': 'boolean',
            'first_name': 'varchar(50)',
            'username': 'varchar(50)',
            'language_code': 'varchar(3)',
            'is_premium': 'boolean'
        },
    'dialogs':
        {
            'start': 'text',
            'help': 'text',
            'info': 'text',
            'worker': 'text',
            'reference': 'text'
        }
}