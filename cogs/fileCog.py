import ast
import os
import asyncio
from subprocess import call

import nextcord
from nextcord.ext import commands
from nextcord.ext import tasks
import re
import global_handlers
import helper_classes


class FileCog(commands.Cog):
	def __init__(self, bot):
		self.playlist_dict = global_handlers.PLAYLISTDICT
		self.download_queue = global_handlers.DOWNLOADQUEUE
		self.logger = global_handlers.GLOBAL_LOGGER
		self.file_queue = global_handlers.FILEQUEUE
		self.poll_list = global_handlers.POLLLIST
		self.sound_dict = global_handlers.SOUNDDICT
		self.reaction_dict = global_handlers.REACTIONDICT
		self.server = bot.get_guild(global_handlers.SERVERID)
		self.bot = bot
		self.method_dict = {
			"populate_playlists": self.read_playlists,
			"playlists": self.write_out_playlists,
			"populate_polls": self.read_polls
		}
		self.file_queue_processor.start()
		self.file_queue.put("populate_playlists")
		self.file_queue.put("populate_polls")

	def write_out_playlists(self):
		with open("££playlists.txt", "w") as file:
			written_text = ""
			for playlist_name, song_list in self.playlist_dict.items():
				written_text += "<" + playlist_name + ";"
				song_list = song_list.to_list()
				entries = "{"
				for song in song_list:
					if song:
						entries = entries + "<" + song.get_name() + "±" + song.get_url() + ">¬"
				entries = entries + "}"
				written_text += entries + ">,"
			file.write(written_text)
			file.close()

	@tasks.loop(seconds=1)
	async def file_queue_processor(self):
		if self.server is None:
			self.server = self.bot.get_guild(global_handlers.SERVERID)
		if not self.file_queue.empty():
			self.method_dict[self.file_queue.get()]()

	def read_playlists(self):
		file = open("££playlists.txt", 'r')
		playlists = re.sub('[\n<>{}]', "", file.read(), 0, re.MULTILINE)
		self.logger.info("Reading Playlists")
		for playlist in playlists.split(','):
			playlist_data = [j for j in playlist.split(';')]
			if len(playlist_data) > 1:
				playlist_name = playlist_data[0]
				song_list = playlist_data[1]
				self.playlist_dict[playlist_name] = helper_classes.SongList()
				if not os.path.exists(playlist_name):
					os.makedirs(playlist_name)
				if len(song_list) > 1:
					for song in song_list.split('¬'):
						if len(song) > 0:
							[song_title, song_url] = song.split('±')
							self.playlist_dict[playlist_name].add(song_title, song_url)
							if not os.path.exists(playlist_name + '/££' + song_title + '.mp3'):
								self.download_queue.put((song_url, playlist_name + "¬" + song_title, False))

	def read_polls(self):
		file = open("polls/££polls.txt", "r")
		polls = re.sub('[\n()]', "", file.read(), 0, re.MULTILINE)
		for poll in polls.split('/'):
			if poll != '':
				poll_args = poll[1:-1].split('`')
				qs, opts, tot, ident = tuple(poll_args)
				opts = ast.literal_eval(opts)
				tot = int(tot)
				ident = int(ident)
				self.poll_list.add(qs, opts, None, tot, ident)

	#
	#

	class MyView(nextcord.ui.View):
		@nextcord.ui.select(  # the decorator that lets you specify the properties of the select menu
			placeholder="Choose a Flavor!",  # the placeholder text that will be displayed if nothing is selected
			min_values=1,  # the minimum number of values that must be selected by the users
			max_values=1,  # the maximum number of values that can be selected by the users
			options=[  # the list of options from which users can choose, a required field
				nextcord.SelectOption(
					label="Vanilla",
					description="Pick this if you like vanilla!"
				),
				nextcord.SelectOption(
					label="Chocolate",
					description="Pick this if you like chocolate!"
				),
				nextcord.SelectOption(
					label="Strawberry",
					description="Pick this if you like strawberry!"
				)
			]
		)
		async def select_callback(self, select,
		                          interaction):  # the function called when the user is done selecting options
			await interaction.response.send_message(f"Awesome! I like {select.values[0]} too!")

	@commands.command(name="modalDrive")
	async def add_to_drive_modal(self, ctx):
		# await ctx.message.delete()
		self.logger.info(ctx.message.author)
		if ctx.message.author not in self.server.roles[-1].members:
			await ctx.send("Command limited to admins")
			return
		filename = ctx.message.attachments[0].filename
		name, extension = filename.split('.')
		list_of_options = self.sound_dict.keys() if extension == "mp3" else self.reaction_dict.keys()
		interactive_view = helper_classes.DriveView(options_list=list_of_options)
		await ctx.send("Choose a category",view = interactive_view)
		await interactive_view.wait()
		self.logger.info(f"Category selected => {interactive_view.result}")
		category = interactive_view.result
		if category != "":
			if not self.sound_dict.exists(category) if extension == "mp3" else not self.reaction_dict.exists(category):
				self.sound_dict.add_entry(category) if extension == "mp3" else self.reaction_dict.add_entry(category)
				self.logger.warning(f"Added new Category {category}")
			wd = os.getcwd()
			os.chdir("drive/")
			file_path, entry_index = await self.process_grive_addition(ctx, category, extension)
			call('grive')
			os.chdir(wd)
			if file_path != "":
				await ctx.send(("Sound " if extension == ".mp3" else "Image ") + category + entry_index + " created")
				await ctx.message.delete()

	@commands.command(name="addToDrive")
	async def add_to_drive(self, ctx, arg):
		# await ctx.message.delete()
		self.logger.info(ctx.message.author)
		if ctx.message.author not in self.server.roles[-1].members:
			await ctx.send("Command limited to admins")
			return
		if arg is None:
			await ctx.send("Command requires single arg")
			return
		filename = ctx.message.attachments[0].filename
		name, extension = filename.split('.')
		category = str(arg)
		self.logger.info(name)
		self.logger.info(extension)
		wd = os.getcwd()
		os.chdir("drive/")
		file_path, entry_index = await self.process_grive_addition(ctx, category, extension)
		call('grive')
		os.chdir(wd)
		if file_path != "":
			await ctx.send(("Sound " if extension == ".mp3" else "Image ") + category + entry_index + " created")

	async def process_grive_addition(self, ctx, category, extension):
		def check(m):
			return m.author == ctx.message.author

		if extension in ["png", "jpeg", "jpg", "gif", "bmp", "mp3"]:
			if self.sound_dict.exists(category) and extension == ".mp3":
				# process mp3 request
				entry_index = str(self.sound_dict.entry_size(category) + 1)
				file_path = './BotStorage/sounds/££' + category + entry_index + '.' + extension
				await ctx.message.attachments[0].save(file_path)
				await ctx.message.delete()
				self.sound_dict.add_entry(category, file_path)
			elif self.reaction_dict.exists(category):
				# Process Image Request
				entry_index = str(self.reaction_dict.entry_size(category) + 1)
				file_path = './BotStorage/reactions/££' + category + entry_index + '.' + extension
				await ctx.message.attachments[0].save(file_path)
				await ctx.message.delete()
				self.reaction_dict.add_entry(category, file_path)
			else:
				# New Category
				mention = ctx.message.author.mention
				await ctx.send(
					mention + " no category " + category + ", would you like it created? y/n")
				msg = await self.bot.wait_for('message', timeout=60.0, check=check)
				if msg.content.upper() in ['Y', 'YES']:
					self.logger.info(extension)
					self.sound_dict.add_entry(category) if extension == "mp3" else self.reaction_dict.add_entry(
						category)
					file_path, entry_index = await self.process_grive_addition(ctx, category, extension)
				else:
					await ctx.send("No action taken")
			return file_path, entry_index
		else:
			await ctx.send("Sorry that file type is not available at this time")
			return "", ""


#
#
# @my_bot.command()
# async def resync(ctx):
# 	await ctx.message.delete()
# 	wd = os.getcwd()
# 	os.chdir("drive")
# 	call('grive')
# 	call('grive')
# 	os.chdir(wd)
# 	rewriteDicts()
# 	await my_bot.get_channel(ServerChan).send("Resync complete")


def setup(bot):
	bot.add_cog(FileCog(bot))
