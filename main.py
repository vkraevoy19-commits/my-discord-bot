import os
import asyncio
from flask import Flask
from threading import Thread
import discord
from discord.ext import commands

# Настройка Flask
app = Flask('')

@app.route('/')
def home():
    return "Бот работает!"

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# Настройка Дискорд-бота
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"=== ОТЛИЧНО! БОТ АВТОРИЗОВАН: {bot.user} ===")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Асинхронный запуск всего вместе
async def main():
    # Запускаем веб-сервер в отдельном потоке
    t = Thread(target=run_web_server)
    t.daemon = True
    t.start()
    print("=== Фоновый веб-сервер запущен ===")
    
    # Берем и очищаем токен
    token = os.environ.get("DISCORD_TOKEN")
    if not token:
        print("ОШИБКА: Токен не найден в Environment Variables!")
        return

    token = token.strip().replace('"', '').replace("'", "")
    
    # Запускаем бота
    try:
        await bot.start(token)
    except Exception as e:
        print(f"Ошибка внутри bot.start: {e}")

if __name__ == "__main__":
    asyncio.run(main())
