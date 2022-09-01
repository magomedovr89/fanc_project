class telegram_bot():
    def __init__(self, token):
        self.token = token
        self.bot = Bot(token=self.token)
        self.dp = Dispatcher(self.bot)
        logging.basicConfig(level=logging.INFO)