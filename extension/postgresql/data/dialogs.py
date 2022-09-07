from extension.postgresql.config import admin_telegram



message = {
    'ru': {
        'greeting': f'Приветствую тебя пользователь. \nТы запустил бота для сбора информации.',
        'help_information': f'Для получения более подробной информации обратись к администратору @{admin_telegram}',
        'work_information': 'В основном работа не пыльная нужно просто фотографировать агрокультуры (Наша первая задача)',
        'reference_work': 'Все правила которых вы должны придерживаться будут описаны в дальнейшем'
    },
    'en': {
        'greeting': f'Hello new user. \nYou launched a bot to collect information.',
        'help_information': f'For more information contact the administrator @{admin_telegram}',
        'work_information': 'The work is not dusty, you just need to photograph agricultural crops (Our first task)',
        'reference_work': 'Rules that you must adhere to will be described later.'
    }
}