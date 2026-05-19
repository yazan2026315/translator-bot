import telebot
from deep_translator import GoogleTranslator

TOKEN = "8825769534:AAFlZqpDS042vxE9tjcN_F7YF23tWXpcGvk"

bot = telebot.TeleBot(TOKEN)

languages = {
    "انكليزي": "en",
    "فرنسي": "fr",
    "تركي": "tr",
    "اسباني": "es",
    "الماني": "de",
    "روسي": "ru",
    "ايطالي": "it",
    "عربي": "ar",
    "ياباني": "ja",
    "كوري": "ko",
    "صيني": "zh-CN"
}

user_language = {}

@bot.message_handler(commands=['start'])
def start(message):
    text = """
🌍 أهلاً بك في بوت الترجمة

اختر اللغة:

انكليزي
فرنسي
تركي
اسباني
الماني
روسي
ايطالي
عربي
ياباني
كوري
صيني
"""
    bot.reply_to(message, text)

@bot.message_handler(func=lambda message: message.text.lower() in languages)
def choose_language(message):
    lang = languages[message.text.lower()]
    user_language[message.chat.id] = lang
    bot.reply_to(message, f"✅ تم اختيار {message.text}\n\nأرسل النص للترجمة")

@bot.message_handler(func=lambda message: True)
def translate_text(message):
    try:
        target_lang = user_language.get(message.chat.id)

        if not target_lang:
            bot.reply_to(message, "❌ اختر لغة أولاً عبر /start")
            return

        translated = GoogleTranslator(
            source='auto',
            target=target_lang
        ).translate(message.text)

        bot.reply_to(message, f"🌍 الترجمة:\n\n{translated}")

    except Exception as e:
        bot.reply_to(message, f"❌ خطأ:\n{e}")

print("البوت يعمل...")
bot.infinity_polling()
