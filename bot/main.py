from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType
import aiogram.utils.markdown as fmt
from define import user_data_to_database





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
        cursor.execute(
            f'''SELECT greeting FROM dialogs WHERE lang = 'ru' '''
        )

        xxx = cursor.fetchall()

except Exception as ex:
    print("Ошибка подключения к серверу")

finally:
    if connection:
        connection.close()
        print("Подключение закрыто")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    print(message.from_user)
    user_data_to_database(message.from_user)
    await message.reply(xxx[0][0])


@dp.message_handler(commands="help")
async def cmd_test1(message: types.Message):
    await message.reply(ms['help'])


@dp.message_handler(commands="info")
async def cmd_test1(message: types.Message):
    await message.reply(ms['info'])


@dp.message_handler(commands="worker")
async def cmd_test1(message: types.Message):
    await message.reply(ms['worker'])


@dp.message_handler(commands="reference")
async def cmd_reference(message: types.Message):
    await message.answer(
        f"{fmt.hide_link('https://telegram.org/blog/video-calls/ru')}Кто бы мог подумать, что "
        f"в 2020 году в Telegram появятся видеозвонки!\n\nОбычные голосовые вызовы "
        f"возникли в Telegram лишь в 2017, заметно позже своих конкурентов. А спустя три года, "
        f"когда огромное количество людей на планете приучились работать из дома из-за эпидемии "
        f"коронавируса, команда Павла Дурова не растерялась и сделала качественные "
        f"видеозвонки на WebRTC!\n\nP.S. а ещё ходят слухи про демонстрацию своего экрана :)",
        parse_mode=types.ParseMode.HTML)

@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: types.input_media):
    unique_id = (message.photo[-1]['file_id'])
    id_user = (message['from']['id'])
    pprint(message)
    await message.photo[-1].download(f'media/{id_user}/{unique_id}.jpg')


executor.start_polling(dp)


