import os
import asyncio
from flask import Flask
from threading import Thread
import discord
from discord.ext import commands

# 1. Веб-сервер "заглушка" для Render
app = Flask('')

@app.route('/')
def home():
    return "Бот запущен!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# 2. Настройка Дискорд-бота
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"=== БОТ УСПЕШНО В СЕТИ: {bot.user} ===")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# 3. Чистый запуск в правильном порядке
def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

if __name__ == "__main__":
    keep_alive()  # Сначала включаем веб-сервер
    
    # Берем токен из настроек Render
    token = os.environ.get("DISCORD_TOKEN")
    
    if token:
        # Убираем возможные случайные пробелы и кавычки из переменной окружения
        token = token.strip().replace('"', '').replace("'", "")
        bot.run(token)
    else:
        print("КРИТИЧЕСКАЯ ОШИБКА: Токен не найден в Environment Variables!")
