import random
from random import shuffle

import nextcord
from nextcord.ext import commands
from nextcord.ext import tasks
import yt_dlp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
import logging
import asyncio
import queue

from selenium.webdriver.common.by import By
from typing import List

import global_handlers
import helper_classes
from general_functions import *
import os


class ReactionCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.source_queue = global_handlers.SOURCEQUEUE
		self.sound_dict = global_handlers.SOUNDDICT
		self.reaction_dict = global_handlers.REACTIONDICT
		self.translation_table = global_handlers.TRANSLATION_TABLE

	@commands.command(name="rxn",
					help='send a rxn to the server, arg: rng, a category, or a category+number listing',
					brief='send a rxn to the server')
	async def reaction(self, ctx, arg):
		if arg is None:
			await ctx.send("Please specify a category for reaction")
		else:
			arg = arg.lower()
			if arg == "rng":
				# Random Reaction
				reaction_str = self.reaction_dict.random_select(random.choice(self.reaction_dict.keys()))
			else:
				if self.reaction_dict.exists(arg):
					reaction_str = self.reaction_dict.random_select(arg)
				else:
					translated_arg = arg.translate(self.translation_table)
					if self.reaction_dict.element_exists(translated_arg, arg):
						reaction_str = self.reaction_dict.get_element(translated_arg, arg)
						if reaction_str is None:
							await ctx.send(f"{arg} is not a valid entry")
							return
					else:
						await ctx.send(f"{arg} is not a valid reaction category")
						return
			await ctx.send(file=nextcord.File(reaction_str))

	@commands.command(name="listSounds",
					help='list all available sound reactions',
					brief='list all available sound reactions')
	async def list_sounds(self,ctx):
		user = ctx.message.author
		category_view = helper_classes.CategoryView("Sound Categories", self.sound_dict.to_length_dict())
		await user.send("Catalogue",embed=category_view.embed,view=category_view)


	@commands.command(name="listReactions",
					help='list all available image reactions',
					brief='list all available image reactions')
	async def list_reactions(self,ctx):
		user = ctx.message.author
		category_view = helper_classes.CategoryView("Reaction Categories", self.reaction_dict.to_length_dict())
		await user.send("Catalogue",embed=category_view.embed, view=category_view)
	@commands.command(name="sound",
					help='send a sound to the server, arg: rng, a category, or a category+number listing',
					brief='send a sound to the server')
	async def sound_bite(self,ctx,arg):
		if arg is None:
			await ctx.send("Please specify a category for reaction")
		else:
			arg = arg.lower()
			if arg == "rng":
				# Random Reaction
				reaction_str = self.sound_dict.random_select(random.choice(self.sound_dict.keys()))
			else:
				if self.sound_dict.exists(arg):
					reaction_str = self.sound_dict.random_select(arg)
				else:
					translated_arg = arg.translate(self.translation_table)
					if self.sound_dict.element_exists(translated_arg, arg):
						reaction_str = self.sound_dict.get_element(translated_arg, arg)
						if reaction_str is None:
							await ctx.send(f"{arg} is not a valid entry")
							return
					else:
						await ctx.send(f"{arg} is not a valid sound category")
						return
			self.source_queue.put((reaction_str, 'high'))
def setup(bot):
	bot.add_cog(ReactionCog(bot))
