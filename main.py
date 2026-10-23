import os
import asyncio
from flask import Flask
from threading import Thread
import discord
from discord.ext import commands

# 1. Настройка Flask
app = Flask('')

@app.route('/')
def home():
    return "Бот работает!"

def run_web_server():
    port = int(os.environ.get("PORT", 10000))  # Render использует порт 10000 по умолчанию
    app.run(host='0.0.0.0', port=port)

# Функция для запуска Flask в отдельном фоновом потоке
def keep_alive():
    t = Thread(target=run_web_server)
    t.daemon = True
    t.start()

# 2. Настройка Дискорд-бота
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"=== ОТЛИЧНО! БОТ АВТОРИЗОВАН: {bot.user} ===")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# 3. Главная точка входа
if __name__ == "__main__":
    # Сначала запускаем веб-сервер в фоне, чтобы Render был доволен
    keep_alive()
    print("=== Фоновый веб-сервер запущен ===")
    
    # Сразу после этого запускаем Дискорд-бота в основном потоке
    token = os.environ.get("DISCORD_TOKEN")
    if token:
        token = token.strip().replace('"', '').replace("'", "")
        bot.run(token)
    else:
        print("ОШИБКА: Токен не найден в Environment Variables!")
