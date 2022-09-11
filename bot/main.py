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
async def cmd_start(message: types.Message):
    db.insert_user_info(message.from_user)
    await message.reply(db.extract(message.from_user, 'greeting'))


@dp.message_handler(commands="info")
async def cmd_info(message: types.Message):
    await message.reply(db.extract(message.from_user, 'information'))


@dp.message_handler(commands="reference")
async def cmd_reference(message: types.Message):
    await message.answer(db.extract(message.from_user, 'reference'))


@dp.message_handler(commands="donation")
async def cmd_reference(message: types.Message):
    await message.answer(db.extract(message.from_user, 'donation'))


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: types.input_media):
    db.write_materials(message.from_user, message.photo[-1])
    await message.photo[-1].download(f'media/{message.from_user.id}/{message.photo[-1].file_unique_id}.jpg')


executor.start_polling(dp, skip_updates=True)