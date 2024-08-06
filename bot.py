import os
from dotenv import load_dotenv
from telegram import Bot, ReplyKeyboardMarkup, Update
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler, CallbackQueryHandler, CallbackContext

load_dotenv()
TELEGRAM_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('chat_id')


# def wake_up(update, context):
#     chat = update.effective_chat

#     context.bot.send_message(chat_id=chat.id,
#                              text='Привет! я бот для тестирования поисковика по гугл-таблице 🦀',
#                              )


def main():
    """Основная логика работы"""
    bot = Bot(token=TELEGRAM_TOKEN)
    chat_id = CHAT_ID
    text = 'Вам телеграмма!'
    bot.send_message(chat_id, text)

    # updater = Updater(token=TELEGRAM_TOKEN)
    # dp = updater.dispatcher

    # dp.add_handler(CommandHandler('start', wake_up))


if __name__ == "__main__":
    main()
