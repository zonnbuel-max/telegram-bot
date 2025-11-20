import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7621709259:AAGjv3pC2iFZekJ6D34l50TelvC4cFkdIsM"
bot = telebot.TeleBot(TOKEN)

# ---------------------------------------------
# FOTO + TEXTO
# ---------------------------------------------
FOTO_URL = "https://i.postimg.cc/j55S8JjX/IMG-20251117-WA0033.jpg"

TEXTO_INICIAL = """
🔔 *Bem-vindo ao Bot!*

Clique abaixo para entrar no nosso grupo VIP:
"""

# ---------------------------------------------
# COMANDO /start
# ---------------------------------------------
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("🔥 Entrar no VIP", url="https://t.me/+_m-LuAmz-Gc3Zjdk")
    markup.add(btn)

    bot.send_photo(
        message.chat.id,
        FOTO_URL,
        caption=TEXTO_INICIAL,
        parse_mode="Markdown",
        reply_markup=markup
    )

# ---------------------------------------------
# LOOP DO BOT
# ---------------------------------------------
print("Bot rodando...")
bot.infinity_polling(skip_pending=True)
