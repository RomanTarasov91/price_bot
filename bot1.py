import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

from parser import parse_price

load_dotenv()

TELEGRAM_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('chat_id')

# Глобальная переменная для хранения сообщения
user_message = ""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Пришли мне ссылку на кингу на admarginem.ru, и я узнаю цену"
    )


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


# Новый обработчик сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global user_message
    # Сохранить текст сообщения в глобальную переменную
    user_message = update.message.text

    price = parse_price(user_message)
    # Ответить пользователю
    await update.message.reply_text(f'Цена книги: {price}')

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
