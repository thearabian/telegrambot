import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = "8762946008:AAHRp1qgABwPUW9Urx66geTqC8y0xaAt3MI"

# ---------------- COMMANDS ---------------- #

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is running 🚀")

# /data
async def data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    drive_link = "https://drive.google.com/your-link"
    await update.message.reply_text(f"📁 Google Drive:\n{drive_link}")

# /client
async def client(update: Update, context: ContextTypes.DEFAULT_TYPE):
    clients = [
        "chicken man ",
        "zoro gaming house",
        "M4 jeans",
        "ibn cereen",
        "abu sloom motors",
        "mahomoud jado",
        "hommies",
        "WOW market",
        "shwarma yazan",
        "zoom wear",
        "la casa italiano"
        
    ]
    await update.message.reply_text("👥 Clients:\n" + "\n".join(clients))

# /content
async def content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    folder = "content"
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder, file), "rb") as f:
                await update.message.reply_document(f)

# /script
async def script(update: Update, context: ContextTypes.DEFAULT_TYPE):
    folder = "script"
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder, file), "rb") as f:
                await update.message.reply_document(f)

# /schedule (with buttons)
async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Abood", callback_data="abood")],
        [InlineKeyboardButton("Nadaaf", callback_data="nadaaf")],
        [InlineKeyboardButton("Client", callback_data="client_schedule")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("📅 Choose directory:", reply_markup=reply_markup)

# Handle button clicks
async def handle_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    folder_map = {
        "abood": "schedule/abood",
        "nadaaf": "schedule/nadaaf",
        "client_schedule": "schedule/client",
    }

    folder = folder_map.get(query.data)

    if folder and os.path.exists(folder):
        for file in os.listdir(folder):
            if file.endswith(".txt"):
                with open(os.path.join(folder, file), "rb") as f:
                    await query.message.reply_document(f)
    else:
        await query.message.reply_text("No files found.")

# ---------------- RUN BOT ---------------- #

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("data", data))
app.add_handler(CommandHandler("client", client))
app.add_handler(CommandHandler("content", content))
app.add_handler(CommandHandler("script", script))
app.add_handler(CommandHandler("schedule", schedule))

app.add_handler(CallbackQueryHandler(handle_schedule))

print("Bot is running...")
app.run_polling()