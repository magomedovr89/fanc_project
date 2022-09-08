from extension.postgresql.schema_database import Database_processing


print('''
Запуск первоначальной настройки сервера.
''')
db = Database_processing()
if (input('Запустить процесс заполнения базы данных Y / N - ').lower()) in ('y', 'yes'):
    db.fill_db()
    if (input('Переход к первичной загрузке данных в таблицы Y / N - ').lower()) in ('y', 'yes'):
        db.fill_table()
        print('aaa')
else:
    if input('!!! Базу данных необходимо очистить? !!! Y / N - ').lower() in ('y', 'yes'):
        if input('Вы уверены Y / N - ').lower() in ('y', 'yes'):
            db.clear_all_to_db()