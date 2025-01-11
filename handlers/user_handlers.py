from telegram import Update

from telegram.ext import ContextTypes

# Список изучаемых слов (для примера, хранение в памяти)

words = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(

        "Привет! Я бот для изучения английских слов. Используйте /add для добавления слов."

    )

async def add_word(update: Update, context: ContextTypes.DEFAULT_TYPE):

    word = ' '.join(context.args)

    if word:

        words.append(word)

        await update.message.reply_text(f"Слово '{word}' добавлено!")

    else:

        await update.message.reply_text("Пожалуйста, укажите слово.")

async def list_words(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if words:

        await update.message.reply_text("Изучаемые слова: " + ", ".join(words))

    else:

        await update.message.reply_text("Нет изучаемых слов.")

@router.callback_query(F.data == 'cancel_update')
async def cancel_update(callback_query: CallbackQuery):
    keyboard = ease_link_kb()
    await callback_query.message.answer("Цена не была обновлена.", reply_markup=keyboard)
    await callback_query.answer()
