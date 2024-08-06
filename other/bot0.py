from telegram import Bot
# import os
# from dotenv import load_dotenv

# load_dotenv()
# TELEGRAM_TOKEN = os.getenv('BOT_TOKEN')
# CHAT_ID = os.getenv('chat_id')

# Здесь укажите токен, 
# который вы получили от @Botfather при создании бот-аккаунта
bot = Bot(token='6720493131:AAGZY4_WVxGpQ6xaClVVi-Sdisyp0HfkW1c')
# Укажите id своего аккаунта в Telegram
chat_id = 225735315
text = 'Вам телеграмма!'
# Отправка сообщения
bot.send_message(chat_id, text)
