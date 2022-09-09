from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType
import aiogram.utils.markdown as fmt
from extension.postgresql.primary_executor import Database_primary_executor


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
db = Database_primary_executor()


@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    db.insert_user_info(message.from_user)
    await message.reply(db.extract(table='dialogs_bot', column='greeting', column_key='language', key_value='ru'))


@dp.message_handler(commands="help")
async def cmd_test1(message: types.Message):
    await message.reply(db.extract(table='dialogs_bot', column='greeting', column_key='language', key_value='ru'))


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
