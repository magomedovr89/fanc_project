import psycopg2
import extension.postgresql.config as config


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
        if input('База данных будет очищена. Вы уверены? (Y / N) ').lower() in ('y', 'yes', 'да', 'д'):
            for table in config.table_dict:
                cursor.execute(f'''DROP TABLE {table}''')
                connection.commit()
                print(f'Таблица {table} удалена')
            print('База данных полностью очищена')
        else:
            print('Операция отменена')

except Exception as ex:
    print("Ошибка подключения к серверу")

finally:
    if connection:
        connection.close()
        print("Подключение закрыто")