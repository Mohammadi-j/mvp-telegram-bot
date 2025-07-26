import os

from telegram.ext import Application, CommandHandler

TOKEN = os.getenv("TELEGRAM_TOKEN")  # به‌صورت امن


async def start(update, context):
    await update.message.reply_text("سلام! من تحلیل‌گر قیمت مسکن هستم.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
