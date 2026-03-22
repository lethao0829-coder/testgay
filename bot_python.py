import random 
import discord
import asyncio
from flask import Flask
import threading

app = Flash(_name_)

@app.route("/")
def home():
  return "Bot đang chạy!"

def run_web():
  app.run(host="0.0.0.0",port=8080)

#Chạy Flask song song
threading.Thread(target=run_web).start()
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "?",intents = intents)

token = 'MTQ3OTA3ODExNTY1NjQ2NjUxNQ.GaGKdz.nSTQsZMu69VSdTlGF3b6jaW1NfXjWZaonY_3Dk'
@bot.event
async def on_ready():
    print("The bot is ready!")

@bot.command(pass_context = True)
async def testgay(ctx):
    import random
    gay = (random.randint(0,101))

    if gay < 25:
        text = "xứng đáng có ny"
        embed = discord.Embed(title = "🌈 ━━━ GAY TEST ━━━ 🌈", description = "độ gay của bạn là: %.1f%%"% gay,color = ( 0xe91e63))
        embed.add_field(name = text  ,value=":DD")
        embed.set_image(url = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3BsZnFlbHl1aGtlZHNsbXBib2swZ2hkeXZ5NDcwODlkZ3Bma2sxdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YJ0ab2jLaAKHv6vIca/giphy.gif")
        await ctx.send(embed = embed )
    elif gay > 25 and gay <= 50:
        text = "ko phải là 36 thì bạn còn ok chán"
        embed = discord.Embed(title = "🌈 ━━━ GAY TEST ━━━ 🌈", description = "độ gay của bạn là: %.1f%%"% gay,color = ( 0x0000ff))
        embed.add_field(name = text  ,value=":))")
        embed.set_image(url = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExem9vZ2J6cDFkN3ZpMGMyMnhpM2NjZ3Y1aGF6b2p4YnJ2c3RzNDR3MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Y5GlGjo5ut42cMEapq/giphy.gif")
        await ctx.send(embed = embed )
    elif gay > 50 and gay <= 80 :
        text = "U ar gay no denying it"
        embed = discord.Embed(title = "🌈 ━━━ GAY TEST ━━━ 🌈", description = "độ gay của bạn là: %.1f%%"% gay,color = ( 0xffc0cb))
        embed.add_field(name = text  ,value="🤨")
        embed.set_image(url = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3BwM3BkZm02cG9jYXk3MzU1YnVvcjUxNmxlZXE4ZnZueXg5MXU2dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FTn2XaLKldiN2CjTRp/giphy.gif")
        await ctx.send(embed = embed )
    elif gay > 80 :
        text = "GAY THÌ CÚT"
        embed = discord.Embed(title = "🌈 ━━━ GAY TEST ━━━ 🌈", description = "độ gay của bạn là: %.1f%%"% gay,color = ( 0xff0000))
        embed.add_field(name = text  ,value="😡")
        embed.set_image(url = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHJ2ZTdnZm11aHh1OGx6dXhqejdhbzd5YWRudnRyaWFhdGNoNm52biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/0OiW6qNfNN4AuhfbYv/giphy.gif")
        await ctx.send(embed = embed )
bot.run(token)    
