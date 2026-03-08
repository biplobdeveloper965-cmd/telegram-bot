from telegram import Update
from telegram.ext import ContextTypes
import database
import config


async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user.id

    database.cursor.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user,)
    )

    data = database.cursor.fetchone()

    if data:
        bal = data[0]
    else:
        bal = 0

    await update.message.reply_text(
        f"💰 Your Balance: {bal}"
    )


async def invite(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user.id

    bot_username = context.bot.username

    link = f"https://t.me/{bot_username}?start={user}"

    await update.message.reply_text(
        f"🔗 Your Invite Link:\n\n{link}\n\n"
        f"🎁 Earn {config.REF_BONUS} per referral"
    )


async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user.id

    database.cursor.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user,)
    )

    bal = database.cursor.fetchone()[0]

    if bal < config.MIN_WITHDRAW:

        await update.message.reply_text(
            f"❌ Minimum withdraw is {config.MIN_WITHDRAW}"
        )

        return

    database.cursor.execute(
        "INSERT INTO withdraw VALUES(?,?,?)",
        (user, bal, "pending")
    )

    database.cursor.execute(
        "UPDATE users SET balance=0 WHERE user_id=?",
        (user,)
    )

    database.conn.commit()

    await update.message.reply_text(
        "✅ Withdraw request sent to admin"
  )
