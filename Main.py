import os
from threading import Thread
from flask import Flask
import discord
from discord.ext import commands

# --- БЛОК ДЛЯ RENDER (ЖИЗНЕОБЕСПЕЧЕНИЕ) ---
app = Flask('')

@app.route('/')
def home():
    return "Бот работает!"

def run_web_server():
    # Render автоматически выдает порт в переменные окружения
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_web_server)
    t.start()
# ------------------------------------------

# Настройка Дискорд-бота
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Успешный запуск! Бот авторизован как {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

if __name__ == "__main__":
    keep_alive() # Запускаем веб-сервер в отдельном потоке
    token = os.environ.get("DISCORD_TOKEN") # Токен берем из настроек Render
    bot.run(token)
