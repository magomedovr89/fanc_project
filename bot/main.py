from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    print(message.from_user)
    await message.reply(ms['start'])


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
    await message.reply(ms['reference'])

@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: types.input_media):
    unique_id = (message.photo[-1]['file_id'])
    id_user = (message['from']['id'])
    pprint(message)
    await message.photo[-1].download(f'media/{id_user}/{unique_id}.jpg')


executor.start_polling(dp)



