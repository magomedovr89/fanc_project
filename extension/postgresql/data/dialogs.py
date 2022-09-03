import aiogram.utils.markdown as fmt
from aiogram import Bot, Dispatcher, executor, types


message = {
    'ru': {
        'greeting': f'Приветствую тебя пользователь. Ты запустил бота для сбора информации.',
        'help_information': 'text',
        'work_information': 'text',
        'reference_work': 'text'
    }
}



'''
@dp.message_handler(commands="test4")
async def with_hidden_link(message: types.Message):
    await message.answer(
        f"{fmt.hide_link('https://telegram.org/blog/video-calls/ru')}Кто бы мог подумать, что "
        f"в 2020 году в Telegram появятся видеозвонки!\n\nОбычные голосовые вызовы "
        f"возникли в Telegram лишь в 2017, заметно позже своих конкурентов. А спустя три года, "
        f"когда огромное количество людей на планете приучились работать из дома из-за эпидемии "
        f"коронавируса, команда Павла Дурова не растерялась и сделала качественные "
        f"видеозвонки на WebRTC!\n\nP.S. а ещё ходят слухи про демонстрацию своего экрана :)",
        parse_mode=types.ParseMode.HTML)
    
'''