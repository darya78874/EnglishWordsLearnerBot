from telegram import Update

from telegram.ext import ContextTypes

# Данные пользователя (пока в памяти)

user_data = {}

async def add_user(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.message.from_user.id

    user_data[user_id] = {"words": []}

    await update.message.reply_text("Пользователь добавлен.")

async def delete_user(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.message.from_user.id

    if user_id in user_data:

        del user_data[user_id]

        await update.message.reply_text("Пользователь удалён.")

    else:

        await update.message.reply_text("Пользователя не существует.")

@router.message(F.text == "Выход из админ панели")
async def exit_admin_panel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Вы вышли из админ панели.", reply_markup=main_keyboard())
    await message.answer("Продолжаем работу", reply_markup=ease_link_kb())
