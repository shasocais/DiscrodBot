import collections
import itertools

from nextcord.ext import commands

import global_handlers
from general_functions import make_pie_chart, char_offsets, generate_meme_square, setup_pie_chart
from helper_classes import PollView


class MiscCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.exit = None
		self.logger = global_handlers.GLOBAL_LOGGER
		self.poll_dict = global_handlers.POLLLIST

	@commands.command(name="memeSquare",
					help=f"memeSquare: first argument is text, final argument can be a conversion setting from: {list(char_offsets.keys())}",
					brief='MemeSquare V2 Redux')
	async def meme_square(self, ctx, *args):
		setting = "<base>"
		if args[-1] in char_offsets:
			setting = args[-1]
			args = args[:-1]
		text = "".join([str(arg) for arg in args])
		msg = generate_meme_square(text, setting)
		await ctx.send(msg)

	async def print_poll(self, ctx):
		interactive_view = PollView("test", self.poll_dict)
		await ctx.send(view=interactive_view)

	@commands.command()
	async def pollStatus(self,ctx):
		await self.print_poll(ctx)

def setup(bot):
	bot.add_cog(MiscCog(bot))
