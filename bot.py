from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7533731133:AAHfTRL39AHagjCMT8ZZ7Xdi0LMgCu6-ues"

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Открыть Чё поесть?", web_app=WebAppInfo(
            url="https://Bip-boop-963.github.io/che-poest-webapp/?v=2"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Выбери что-то вкусное:", reply_markup=reply_markup)

async def button_click(update: Update, context: CallbackContext):
    if update.message.text == "Открыть Чё поесть?":
        await start(update, context)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, button_click))

print("Бот запущен...")
app.run_polling()
