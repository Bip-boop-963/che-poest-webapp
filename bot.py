from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

TOKEN = "7533731133:AAHfTRL39AHagjCMT8ZZ7Xdi0LMgCu6-ues"

async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Открыть Чё поесть?", web_app=WebAppInfo(
            url="https://Bip-boop-963.github.io/che-poest-webapp/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Выбери что-то вкусное:", reply_markup=reply_markup)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Бот запущен...")
app.run_polling()
