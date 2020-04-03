import discord
from discord.ext import commands

TOKEN = 'Njk1NDQyNjAwNDU0Mzg5ODQw.Xod7xg.Ro8Q_k0CUSM9a372tqyZT2qykAk'
bot = commands.Bot(command_prefix='.')


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def BrendUser(ctx, arg):  # создаем асинхронную функцию бота
    await ctx.send(arg)  # отправляем обратно аргумент


bot.run(TOKEN)