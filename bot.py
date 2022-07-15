import discord
from discord.ext import commands


class MyBot(commands.Bot):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def setup_hook(self):
        await self.load_extension('events')


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
Bot = MyBot(intents=intents, command_prefix='!', help_command=None)
Bot.run('NzYwMzA0NDMxNDA4NjExMzk4.GXNr8T.0qOw-669JiWG7J_1b01zr-6RViO2xozd-r8C5U')
