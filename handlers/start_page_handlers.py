from telegram import Update

from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(

        "Добро пожаловать в бот для изучения английских слов!\\n"

        "Используйте команды:\\n"

        "/add - Добавить новое слово\\n"

        "/list - Показать изучаемые слова\\n"

        "/help - Получить помощь"

    )

        "Студент 2 курса Магага\n"
        "Основные навыки: Python, работа с библиотеками aiogram"
    )
    await message.answer(developer_info)
