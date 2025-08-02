from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes

TOKEN = "7773694762:AAFnHrxyW55UQrIPpmWKB8KMUP_SBWqMue8"
WEB_APP_URL = "https://github.com/Zxcv21star/zxcvDrop.git"  # Замените на реальный URL

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(
            "🎮 Открыть CS:GO Cases", 
            web_app={"url": WEB_APP_URL}
        )]
    ]
    await update.message.reply_text(
        "Добро пожаловать в CS:GO Case Opening Mini App!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()