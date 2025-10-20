from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔑 Вставь сюда токен своего бота
TOKEN = "8320766423:AAEzbC6nfEM_GvniBvO_6-kLhf-z6jkSFzE"

# 📌 /start — главное меню
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📩 Предложить", callback_data="offer")],
        [InlineKeyboardButton("❓ Задать вопрос", callback_data="ask_question")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет 👋\nВыбери, что ты хочешь сделать:",
        reply_markup=reply_markup
    )

# 📩 Обработка нажатия на inline-кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # 📩 Предложить
    if query.data == "offer":
        await query.edit_message_text(
            text="У тебя есть предложение? ✉️\nНапиши нам на почту: info@napalabs.ru"
        )

    # ❓ Задать вопрос — показываем второе меню
    elif query.data == "ask_question":
        keyboard = [
            [InlineKeyboardButton("Equila DPI", callback_data="equila")],
            [InlineKeyboardButton("OTIUM ACS", callback_data="otium")],
            [InlineKeyboardButton("Inframirror", callback_data="infra")],
            [InlineKeyboardButton("Задать вопрос специалисту", callback_data="specialist")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="Выбери продукт, по которому хочешь задать вопрос 👇",
            reply_markup=reply_markup
        )

    # Equila DPI
    elif query.data == "equila":
        text = (
            "🌐 *Equila DPI* — система анализа и фильтрации трафика на базе технологии DPI.\n\n"
            "📌 *Сфера применения*: ограничение доступа к запрещённым ресурсам.\n\n"
            "✅ *Преимущества:*\n"
            "- Блокировка доступа к сайтам с незаконным содержанием\n"
            "- Гибкость системы\n"
            "- Статистика трафика\n\n"
            "Подробнее: [napalabs.ru/equila_dpi](https://napalabs.ru/equila_dpi)"
        )
        await query.edit_message_text(text=text, parse_mode="Markdown")

    # OTIUM ACS
    elif query.data == "otium":
        text = (
            "🖥 *OTIUM ACS* — сервер управления клиентским оборудованием.\n\n"
            "📌 Направления использования: бизнес, разработчики IT, операторы связи.\n\n"
            "✅ *Преимущества:*\n"
            "- Оптимизация затрат\n"
            "- Рост эффективности\n"
            "- Лучший клиентский опыт\n\n"
            "🔸 [Демо-доступ](https://otiumacs-demo.napalabs.ru/auth/login?next=/)\n"
            "Подробнее: [napalabs.ru/otium_acs](https://napalabs.ru/otium_acs)"
        )
        await query.edit_message_text(text=text, parse_mode="Markdown")

    # InfraMirror
    elif query.data == "infra":
        text = (
            "🏗 *InfraMirror* — технический учёт инфраструктуры.\n\n"
            "📌 *Направление использования*: ресурсо- и телеком-компании.\n\n"
            "✅ *Преимущества:*\n"
            "- Экономия ресурсов\n"
            "- Оптимизация процессов\n"
            "- Повышение эффективности\n\n"
            "Подробнее: [napalabs.ru/inframirror](https://napalabs.ru/inframirror)"
        )
        await query.edit_message_text(text=text, parse_mode="Markdown")

    # Задать вопрос специалисту
    elif query.data == "specialist":
        await query.edit_message_text(
            text="Хочешь задать вопрос специалисту? 📩\nНапиши 👉 @sevarafoto"
        )

# 🚀 Запуск бота
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("✅ Бот запущен и работает...")
    app.run_polling()

if __name__ == "__main__":
    main()