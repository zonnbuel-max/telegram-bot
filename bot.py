import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7621709259:AAGjv3pC2iFZekJ6D34l50TelvC4cFkdIsM"  # <-- coloque seu token aqui
bot = telebot.TeleBot(TOKEN)

# -------------------------------------------------------
# FOTO DO BOT
# -------------------------------------------------------
FOTO_URL = "https://i.postimg.cc/j55S8JjX/IMG-20251117-WA0033.jpg"
TEXTO_INICIAL = """
🔔 *Bem-vindo ao Bot!*  
Aqui você recebe avisos e acessa o conteúdo VIP.
"""

# -------------------------------------------------------
# COMANDO /start
# -------------------------------------------------------
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("🔥 Entrar no VIP", url="https://t.me/+SEU_GRUPO_AQUI")
    markup.add(btn)

    bot.send_photo(
        message.chat.id,
        FOTO_URL,
        caption=TEXTO_INICIAL,
        parse_mode="Markdown",
        reply_markup=markup
    )

# -------------------------------------------------------
# LOOP INFINITO DO BOT
# -------------------------------------------------------
print("Bot está rodando corretamente...")
bot.infinity_polling()
