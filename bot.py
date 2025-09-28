from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler

BOT_TOKEN = "7533731133:AAHfTRL39AHagjCMT8ZZ7Xdi0LMgCu6-ues"

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton(
            "Открыть Чё поесть?", 
            web_app=WebAppInfo(url="https://cubiform-hsiu-egregiously.ngrok-free.dev")
        )]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Нажми на кнопку, чтобы выбрать блюдо:", reply_markup=reply_markup)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    app.run_polling()
