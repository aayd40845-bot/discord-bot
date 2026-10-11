import os
import discord
from discord.ext import commands

# إعداد البوت مع الصلاحيات المطلوبة
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# قاموس بسيط لتخزين أرصدة الأعضاء مؤقتاً
balances = {}

@bot.event
async def on_ready():
    print(f"تم تسجيل الدخول بنجاح كـ {bot.user}")

@bot.command(name="رصيد")
async def check_balance(ctx):
    user_id = ctx.author.id
    bal = balances.get(user_id, 100) # يمنح العضو 100 عملة افتراضية عند البداية
    await ctx.send(f"👤 {ctx.author.mention}, رصيدك الحالي هو: **{bal}** عملة 💰")

@bot.command(name="راتب")
async def daily_salary(ctx):
    user_id = ctx.author.id
    current_bal = balances.get(user_id, 100)
    balances[user_id] = current_bal + 50
    await ctx.send(f"🎁 {ctx.author.mention}, استلمت راتبك اليومي بنجاح! رصيدك الآن: **{balances[user_id]}** عملة 💰")

# تشغيل البوت باستخدام التوكن السري
TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)