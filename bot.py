from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

tasks = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Vansh! Your PA bot is ready.")

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    task = " ".join(context.args)
    tasks.append(task)
    await update.message.reply_text(f"Added: {task}")

async def tasks_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not tasks:
        await update.message.reply_text("No tasks yet.")
    else:
        await update.message.reply_text("\n".join(tasks))

app = ApplicationBuilder().import os
TOKEN = os.getenv("8235992110:AAF09afU_ExP3lW0ZaIQhSukfGTZEqiR6Ho")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("tasks", tasks_list))

app.run_polling()
