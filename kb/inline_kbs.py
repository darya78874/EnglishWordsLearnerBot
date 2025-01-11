from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def inline_keyboard():

    keyboard = [

        [InlineKeyboardButton("Добавить слово", callback_data='add_word')],

        [InlineKeyboardButton("Список слов", callback_data='list_words')]

    ]

    return InlineKeyboardMarkup(keyboard)
