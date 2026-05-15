import telebot
from telebot import types

# ВСТАВЬ СВОЙ НОВЫЙ ТОКЕН
TOKEN = "8303912304:AAGAxOFve5krAyFILeu2G2yCkacEr6nueJU"

bot = telebot.TeleBot(TOKEN)

# Контакты руководства
CONTACTS_TEXT = (
    "🏛 ВЫСШИЙ СОВЕТ СИНДИКАТА [24 SPB]:\n\n"

    "👑 Tawerqa_Delarosa — Хладнокровный Патриарх\n"
    "Связь: @tawerqagoldenwize\n\n"

    "👑 Kuroko_Mallboro — Архитектор Камбэка\n"
    "Связь: @kuroko_mallboro\n\n"

    "💼 Alexander_Sfitoff — Первый заместитель\n"
    "💼 Jesus_Delarosa — Серый кардинал\n\n"

    "👉 По вопросам вступления и дипломатии писать исключительно Высшему Совету."
)

# История и конституция
HISTORY_TEXT = (
    "🏛 СИНДИКАТ MALLBORO x DELAROSA [24 SPB] 🏛\n\n"

    "📜 ЧАСТЬ I: ИСТОРИЯ JESUS_MALLBORO\n\n"

    "Jesus_Mallboro (Tawerqa_Delarosa) — легендарный мультиоснователь "
    "01 сервера SanTrope RP. Создатель трех брендов: Mallboro, Delarosa "
    "и Goldenwize.\n\n"

    "🤝 ЧАСТЬ II: ИСХОД И БРАТСКИЙ ТЫЛ\n\n"

    "Родной брат Kuroko_Mallboro выступил архитектором великого камбэка.\n\n"

    "👑 ГЛАВА I: ВЫСШИЙ ЗАКОН О ВЕЧНОЙ МУЗЕ\n\n"

    "• Фося официально объявлена Вечной Музой Синдиката.\n"
    "• Любое неуважение запрещено.\n\n"

    "⚔️ ГЛАВА II: ЗАКОНЫ КРОВИ\n\n"

    "• Брат за брата.\n"
    "• Приказы руководства не обсуждаются.\n\n"

    "С нами бог, под нами Питер!"
)

# Приветствие
def get_welcome_text(username):
    return (
        f"🏛 ДОБРО ПОЖАЛОВАТЬ В СИНДИКАТ, @{username}! 🏛\n\n"

        "Ты попал в чат сильнейшего криминального альянса.\n\n"

        "⚠️ Главный закон чата:\n"
        "Уважай руководство и правила синдиката.\n\n"

        "Напиши боту /start для открытия меню."
    )

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):

    if message.chat.type == 'private':

        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            row_width=1
        )

        btn1 = types.KeyboardButton("📜 История и Конституция")
        btn2 = types.KeyboardButton("💼 Контакты Руководства")

        markup.add(btn1, btn2)

        bot.send_message(
            message.chat.id,
            "Приветствую, боец!\n\n"
            "Я официальный бот синдиката Mallboro x Delarosa.\n\n"
            "Выбери пункт меню:",
            reply_markup=markup
        )

# Обработка кнопок
@bot.message_handler(content_types=['text'])
def handle_text(message):

    if message.chat.type == 'private':

        if message.text == "📜 История и Конституция":

            bot.send_message(
                message.chat.id,
                HISTORY_TEXT
            )

        elif message.text == "💼 Контакты Руководства":

            bot.send_message(
                message.chat.id,
                CONTACTS_TEXT
            )

# Запуск бота
print("Бот запущен!")

bot.infinity_polling()