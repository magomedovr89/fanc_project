#  Данный файл необходимо запустить для первоначальной настройки базы данных
#  Описание таблиц:



#  В данной таблице хранится информация о конфигурации веб сервера и бота
#  configs:
#  telegramm_token - Токен бота в телеграмме
#


#  users:
#  id - Хранит в себе уникальный идентификатор пользователя в телеграмм
#  is_bot - Хранит информацию о том что пользователь не является ботом (Логический)
#  first_name - Хранит информацию о фамилии пользователя (Симовльный 50)
#  username - Хранит имя пользователя (Симовльный 50)
#  language_code varchar(3) - Хранит информацию о стране польхзователя (Симыольный 3)
#  is_premium Премиум статус польхователя (Логический)

#  rating:
#  !!! Данная таблица в разработке !!!
#  В данной таблицке планируется создания на основе результатов
#  работы пользователя создать талицу с рейтингом.

#  dialog
#  !!! Данная таблица в разработке !!!
#  В данной таблице планируется сохранить диалоги с пользователями.
#  В данной таблице создаем ключевой столбец с названием языка пользователя
#  кроме этого нужно дать возможность выбора языка пользователем.


#  materials
#  !!! Данная таблица в разработке !!!
#  id_user --> users.id - Идентификатор пользователя который сделал фото
#  id_photo - уникальный идентификатор фотографии (Имя файла)
#  is_processing - Произведен ли анализ данной фотографии (Логический)
#  is_actual - Параметр который указывает на актулаьнойсть данной фотографии (Логический)


#  Кроме данных таблиц нужно еще подумать над тем какие данные будут необходимы для сайта.
#  Еще надо не забыть про пользователей которые будут являтся теми кто будет верифицировать фотографии.
#  Необходимо продумать таблицу в кторой будет хранится информация о агрокультурах!!!


import psycopg2
import config
import define


#  Попытка подключения к серверу Конфигурационный файл config.py
#  !!!Порт по умолчанию!!!
requests_list = define.create_request(config.table_dict)
try:
    connection = psycopg2.connect(
        dbname=config.dbname,
        user=config.user,
        password=config.password,
        host=config.host
    )

    with connection.cursor() as cursor:
        for req in requests_list:
            cursor.execute(req)
            connection.commit()

except Exception as ex:
    print("Ошибка подключения к серверу")

finally:
    if connection:
        connection.close()
        print("Подключение закрыто")