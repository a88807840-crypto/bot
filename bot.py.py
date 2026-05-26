from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8997990938:AAFPLxBresbVnvfB9W9GT8u2cCYE5lXe83o"

CHANNEL_LINK = "https://t.me/+VMqKOgXMT3pjNTU0"

TEXT = f"""
⚡ CODE CHECKER | SHOPIFY  ⚡

Fast, accurate, and hits gateways like a beast. From zero to billions.

💳 CREDITS & PLANS:

• 5K Credits ➔ $8
• 10K Credits ➔ $15
• 15K Credits ➔ $20
• 20K Credits ➔ $25
• 30K Credits ➔ $30
• 👑 Monthly Unlimited ➔ $80

🔍 FREE TEST AVAILABLE:

• Max 100 Credits for serious buyers only.

⚠️ Note: Prices include everything. No refunds.

📢 Join Our Channel:
{https://t.me/+vpnzr1kskCIyODI0}

🤖 Bot: @Xchecker7_bot
📥 Buy Here: @A017gw1 & @ndu_65
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(TEXT)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot Running...")
app.run_polling()