import psycopg2
import config


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
        for table in config.table_dict:
            print(table)
            cursor.execute(
                f'''DROP TABLE {table}'''
            )
            connection.commit()

except Exception as ex:
    print("Ошибка подключения к серверу")

finally:
    if connection:
        connection.close()
        print("Подключение закрыто")