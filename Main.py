import discord
from discord.ext import commands

# Настраиваем доступы
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Событие готовности бота
@bot.event
async def on_ready():
    print(f"Бот {bot.user} успешно запущен!")

# Простая команда !ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Запуск бота (вместо 'ВАШ_ТОКЕН' вставьте скопированный токен из Шага 2)
bot.run('ВАШ_ТОКЕН')
