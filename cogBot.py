import nextcord
from nextcord.ext import commands

from os import listdir
from os.path import isfile, join
import asyncio
import sys, traceback
from keys import *
import global_handlers


def get_prefix(bot, message):
	prefixes = ['!']
	if not message.guild:
		return '?'

	return commands.when_mentioned_or(*prefixes)(bot,message)


# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
# This is the directory all are located in.
cogs_dir = "cogs"

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix=get_prefix, description='A modular bot', intents=intents)

# Here we load our extensions(cogs) that are located in the cogs directory. Any file in here attempts to load.

def load_extensions():
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            bot.load_extension(cogs_dir + "." + extension)
        except (nextcord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()

@bot.event
async def on_ready():
    """http://nextcordpy.readthedocs.io/en/rewrite/api.html#nextcord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {nextcord.__version__}\n')
    print(f'Successfully logged in and booted...!')

if __name__ == '__main__':
    load_extensions()
bot.run(bot_key(), reconnect=True)