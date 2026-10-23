import os
import asyncio
from flask import Flask
from threading import Thread
import discord
from discord.ext import commands

# 1. Настройка веб-сервера Flask для Render
app = Flask('')

@app.route('/')
def home():
    return "Бот работает 24/7!"

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_web_server)
    t.daemon = True  # Фоновый поток
    t.start()

# 2. Настройка самого Дискорд-бота
intents = discord.Intents.default()
intents.message_content = True  # Не забудьте включить тумблеры в Discord Developer Portal!
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"=== Успешный запуск! Бот авторизован как {bot.user} ===")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# 3. Главная функция запуска
async def main():
    keep_alive()  # Запускаем сайт-заглушку
    token = os.environ.get("DISCORD_TOKEN")  # Берем токен из настроек Render
    
    if not token:
        print("ОШИБКА: Переменная DISCORD_TOKEN не найдена в настройках Render!")
        return

    try:
        await bot.start(token)
    except Exception as e:
        print(f"Ошибка при запуске Дискорд-бота: {e}")

if __name__ == "__main__":
    asyncio.run(main())
