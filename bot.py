import telebot
from telebot import types

# ----------------------------------------
#  INSIRA SEU TOKEN AQUI:
# ----------------------------------------
TOKEN = "7621709259:AAGjv3pC2iFZekJ6D34l50TelvC4cFkdIsM"

bot = telebot.TeleBot(TOKEN)

# ----------------------------------------
# /start
# ----------------------------------------
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("⚡ Entrar no VIP", callback_data="vip")
    btn2 = types.InlineKeyboardButton("📞 Suporte", url="https://t.me/seu_usuario_aqui")
    markup.add(btn1, btn2)

    bot.send_photo(
        message.chat.id,
        "https://i.imgur.com/0rR7w1C.jpeg",  # FOTO EXEMPLO (PODE TROCAR DEPOIS)
        caption="🔥 *Bem-vindo ao bot oficial!* \nEscolha uma opção abaixo 👇",
        reply_markup=markup,
        parse_mode="Markdown"
    )

# ----------------------------------------
# Botões
# ----------------------------------------
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "vip":
        bot.answer_callback_query(call.id)
        bot.send_message(
            call.message.chat.id,
            "💎 Para entrar no grupo VIP, finalize seu pagamento.\n"
            "Enviei o link pra você!"
        )

# ----------------------------------------
# Mantém o bot rodando
# ----------------------------------------
bot.infinity_polling()
