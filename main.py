import telebot

# --- अपनी डिटेल्स यहाँ भरें ---
API_TOKEN = '8696081950:AAEBf-VeL_3AiFZ6O3cGYrnrWJKIPdUVY_g'
MY_SITE = 'https://sumitgautamad-rgb.github.io/myplayer/' 
# ---------------------------

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 स्वागत है! मुझे कोई भी TeraBox लिंक भेजें।")

@bot.message_handler(func=lambda m: 'terabox' in m.text or 'nephobox' in m.text)
def handle_link(message):
    user_url = message.text.strip()
    # आपकी वेबसाइट का लिंक जिसमें वीडियो का लिंक जुड़ा होगा
    final_earning_url = f"{MY_SITE}?url={user_url}"
    
    markup = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton("📽️ Play Video Online", url=final_earning_url)
    markup.add(btn)
    
    bot.send_message(message.chat.id, "✅ वीडियो लिंक तैयार है! नीचे क्लिक करें:", reply_markup=markup)

bot.polling()
