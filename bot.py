import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi mawa 🔥 Send /script to generate shorts idea")


async def script(update: Update, context: ContextTypes.DEFAULT_TYPE):

    prompt = """
5 seconds hook lo 3 shocking lines Telugu lo rayi.
History, mystery, dark vaddu.
Daily use items gurinchi undali.
Tarvatha Fact 1, Fact 2, Fact 3 ani rayaku.
Friendly tone, casual Telugu.
YouTube Shorts ki perfect ga undali.
"""

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
        },
    )

    data = response.json()
    text = data["choices"][0]["message"]["content"]

    await update.message.reply_text(text)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("script", script))

app.run_polling()
