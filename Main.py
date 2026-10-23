import discord
from discord.ext import commands
import os

# Налаштовуємо права (intents) для бота
intents = discord.Intents.default()
intents.message_content = True  # Щоб бот міг читати повідомлення

# Створюємо самого бота з префіксом "!" (можеш змінити на будь-який інший)
bot = commands.Bot(command_prefix="!", intents=intents)

# Проста подія, яка покаже в логах Render, що бот увімкнувся
@bot.event
async def on_ready():
    print(f"Бот {bot.user.name} успішно запущений і готовий до роботи!")

# Тестова команда: якщо написати !hello, бот відповість
@bot.command()
async def hello(ctx):
    await ctx.send("Привіт! Я працюю на Render!")

# Запуск бота через твій токен
token = os.environ.get("DISCORD_TOKEN")
if token:
    bot.run(token)
else:
    print("Помилка: DISCORD_TOKEN не знайдено в налаштуваннях Render!")
