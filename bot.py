from telegram import *
from telegram.ext import *
import config
import database
import admin_commands
import user_commands


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.id

    database.cursor.execute(
        "INSERT OR IGNORE INTO users(user_id) VALUES(?)",
        (user,)
    )
    database.conn.commit()

    buttons = []

    for title, link in config.CHANNELS:
        buttons.append([InlineKeyboardButton(title, url=link)])

    buttons.append([InlineKeyboardButton("✅ VERIFY", callback_data="verify")])

    keyboard = InlineKeyboardMarkup(buttons)

    await update.message.reply_photo(
        photo="https://picsum.photos/500/300",
        caption="🎬 Join all channels then press VERIFY",
        reply_markup=keyboard
    )


async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = query.from_user.id

    joined = True

    for title, link in config.CHANNELS:
        channel = link.replace("https://t.me/", "@")

        try:
            member = await context.bot.get_chat_member(channel, user)

            if member.status == "left":
                joined = False

        except:
            joined = False

    if joined:

        menu = [
            ["🔥 Trending", "💎 Exclusive"],
            ["🔗 Invite & Earn", "💰 My Balance"],
            ["💸 Withdraw"]
        ]

        reply = ReplyKeyboardMarkup(menu, resize_keyboard=True)

        await query.message.reply_text(
            "✅ Verified Successfully",
            reply_markup=reply
        )

    else:
        await query.answer("❌ Join all channels first!", show_alert=True)


app = ApplicationBuilder().token(config.TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(verify, pattern="verify"))

app.add_handler(CommandHandler("stats", admin_commands.stats))
app.add_handler(CommandHandler("broadcast", admin_commands.broadcast))

app.add_handler(CommandHandler("balance", user_commands.balance))
app.add_handler(CommandHandler("invite", user_commands.invite))
app.add_handler(CommandHandler("withdraw", user_commands.withdraw))

app.run_polling(drop_pending_updates=True)            ["🔥 Trending", "💎 Exclusive"],
            ["🔗 Invite & Earn", "💰 My Balance"],
            ["💸 Withdraw"]
        ]

        reply = ReplyKeyboardMarkup(menu, resize_keyboard=True)

        await query.message.reply_text(
            "✅ Verified Successfully",
            reply_markup=reply
        )

    else:
        await query.answer("❌ Join all channels first!", show_alert=True)


app = ApplicationBuilder().token(config.TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(verify, pattern="verify"))

app.add_handler(CommandHandler("stats", admin_commands.stats))
app.add_handler(CommandHandler("broadcast", admin_commands.broadcast))

app.add_handler(CommandHandler("balance", user_commands.balance))
app.add_handler(CommandHandler("invite", user_commands.invite))
app.add_handler(CommandHandler("withdraw", user_commands.withdraw))

app.run_polling(drop_pending_updates=True)
    for title, link in config.CHANNELS:
        channel = link.replace("https://t.me/", "@")

        try:
            member = await context.bot.get_chat_member(channel, user)

            if member.status == "left":
                joined = False

        except:
            joined = False

    if joined:

        menu = [
            ["🔥 Trending", "💎 Exclusive"],
            ["🔗 Invite & Earn", "💰 My Balance"],
            ["💸 Withdraw"]
        ]

        reply = ReplyKeyboardMarkup(menu, resize_keyboard=True)

        await query.message.reply_text(
            "✅ Verified Successfully",
            reply_markup=reply
        )

    else:
        await query.answer("❌ Join all channels first!", show_alert=True)


app = ApplicationBuilder().token(config.TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(verify, pattern="verify"))

app.add_handler(CommandHandler("stats", admin_commands.stats))
app.add_handler(CommandHandler("broadcast", admin_commands.broadcast))

app.add_handler(CommandHandler("balance", user_commands.balance))
app.add_handler(CommandHandler("invite", user_commands.invite))
app.add_handler(CommandHandler("withdraw", user_commands.withdraw))

app.run_polling()    query = update.callback_query
    user = query.from_user.id

    joined = True

    for title, link in config.CHANNELS:

        channel = link.replace("https://t.me/", "@")

        try:
            member = await context.bot.get_chat_member(channel, user)

            if member.status == "left":
                joined = False

        except:
            joined = False

    if joined:

        menu = [
            ["🔥 Trending", "💎 Exclusive"],
            ["🔗 Invite & Earn", "💰 My Balance"],
            ["💸 Withdraw"]
        ]

        reply = ReplyKeyboardMarkup(menu, resize_keyboard=True)

        await query.message.reply_text(
            "✅ Verified Successfully",
            reply_markup=reply
        )

    else:
        await query.answer("❌ Join all channels first!", show_alert=True)



app = ApplicationBuilder().token(config.TOKEN).build()


app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(verify, pattern="verify"))

app.add_handler(CommandHandler("stats", admin_commands.stats))
app.add_handler(CommandHandler("broadcast", admin_commands.broadcast))

app.add_handler(CommandHandler("balance", user_commands.balance))
app.add_handler(CommandHandler("invite", user_commands.invite))
app.add_handler(CommandHandler("withdraw", user_commands.withdraw))


app.run_polling(drop_pending_updates=True)
