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


class EventsCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.source_queue = global_handlers.SOURCEQUEUE
		self.download_queue = global_handlers.DOWNLOADQUEUE
		self.theme_dict = global_handlers.THEMEDICT
		self.logger = global_handlers.GLOBAL_LOGGER
	@commands.Cog.listener(name="on_voice_state_update")
	async def handle_member_movement(self, member, before, after):
		if member.top_role.name == 'Bot Boy':
			self.logger.info("Spotted you botter")
		if ((before.channel is None and after.channel is not None) or (
				before != after)) and member.top_role.name != 'Bot Boy':
			if after.channel is None and \
					before.channel is not None and before.channel.id == global_handlers.SCREAMCHAMBER:
				self.logger.info("Member leaving voice")
				self.source_queue.put((member.display_name, "schlorp"))
			elif before.channel is None or before.channel.id != after.channel.id:
				if after.channel.id == global_handlers.SCREAMCHAMBER:
					self.logger.info("Checking membership")
					self.logger.info(member.id)
					if str(member.id) in self.theme_dict:
						self.logger.info("ThemeTime")
						string = "./themes/££" + str(member.id) + str(self.theme_dict[str(member.id)]) + ".mp3"
						self.source_queue.put((string, "high"))
					else:
						self.download_queue.put((member.id, member.display_name, "theme"))
			else:
				self.logger.warn("Unrecognised voice update")
def setup(bot):
	bot.add_cog(EventsCog(bot))
