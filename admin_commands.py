from telegram import Update
from telegram.ext import ContextTypes
import database
import config

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id not in config.ADMIN_IDS:
        return

    database.cursor.execute("SELECT COUNT(*) FROM users")
    users = database.cursor.fetchone()[0]

    text = f"👥 Total Users: {users}"

    await update.message.reply_text(text)


async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id not in config.ADMIN_IDS:
        return

    msg = " ".join(context.args)

    database.cursor.execute("SELECT user_id FROM users")
    users = database.cursor.fetchall()

    sent = 0

    for user in users:

        try:
            await context.bot.send_message(user[0], msg)
            sent += 1
        except:
            pass

    await update.message.reply_text(f"✅ Sent to {sent} users")
