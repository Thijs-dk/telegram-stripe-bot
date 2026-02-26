import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ["BOT_TOKEN"]
STRIPE_TRIAL_URL = os.environ["STRIPE_TRIAL_URL"]
STRIPE_MONTH_URL = os.environ["STRIPE_MONTH_URL"]
STRIPE_YEAR_URL = os.environ["STRIPE_YEAR_URL"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Welcome 👋\n\n"
        "Here you can access free previews.\n\n"
        "Unlock full Premium access to receive:\n"
        "• Exclusive predictions\n"
        "• Faster updates\n"
        "• VIP content\n\n"
        "Choose your plan below:"
    )

    keyboard = [
        [InlineKeyboardButton("🔓 3 Day Trial", url=STRIPE_TRIAL_URL)],
        [InlineKeyboardButton("⭐ 1 Month Premium", url=STRIPE_MONTH_URL)],
        [InlineKeyboardButton("💎 1 Year Premium", url=STRIPE_YEAR_URL)],
    ]

    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
