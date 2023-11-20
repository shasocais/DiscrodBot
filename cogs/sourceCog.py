import random
from random import shuffle

import nextcord
from gtts import gTTS
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


def determine_song_location(target: str):
	if "/recent/" in target:
		return "recent"
	elif "./" in target:
		return "local"
	else:
		return "online"


class SourceCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.playlist_dict = global_handlers.PLAYLISTDICT
		self.player_queue = global_handlers.PLAYERQUEUE
		self.download_queue = global_handlers.DOWNLOADQUEUE
		self.source_queue = global_handlers.SOURCEQUEUE
		self.recentSongList = global_handlers.RECENTSONGLIST
		self.exit = None
		self.logger = global_handlers.GLOBAL_LOGGER
		self.source_queue_processor.start()
		self.base_yt_string = 'https://www.youtube.com/'
		options = Options()
		options.headless = True
		self.display = global_handlers.DISPLAY
		self.browser = webdriver.Chrome(options=options)


	ffmpeg_options = {'options': '-vn -sn'}

	"""
	
		SONG ACQUISITION
	
		"""

	# handles looking up youtube search results
	async def yt_lookup(self, arg: str, title: bool) -> List[dict]:
		self.logger.info("Lookup start")
		yt_search_string = self.base_yt_string + "results?search_query=" + arg
		self.logger.info("browser loaded")
		if arg[:2] == "/w" and not title:
			return [{"link": self.base_yt_string + arg, "title": ""}]
		else:
			if arg[:2] == "/w":
				yt_search_string = self.base_yt_string + arg
				self.logger.info(yt_search_string)
				self.logger.info("Browser navigating")
				self.browser.get(yt_search_string)
				self.logger.info("Browser got")
				await asyncio.sleep(2.5)
				link_list = WebDriverWait(self.browser, 3).until(
					EC.presence_of_all_elements_located((By.CLASS_NAME, 'ytd-video-primary-info-renderer')))
				count = 0
				href_title = ''
				for link in link_list:
					self.logger.info(link.text)
					if count > 4:
						href_title = link.text
						break
					count = count + 1
				self.logger.info(href_title)
				return [{"link": "https://www.youtube.com" + arg, "title": href_title}]
			self.logger.info("Browser navigating to site")
			self.browser.get(yt_search_string)
			self.logger.info("Browser got")
			link_list = WebDriverWait(self.browser, 3).until(
				EC.presence_of_all_elements_located((By.ID, 'video-title')))
			if title:
				aug_link_list = [{"link": link.get_attribute('href'), "title": link.get_attribute('title')}
								for link in link_list]
			else:
				aug_link_list = [{"link": link.get_attribute('href'), "title": ""} for link in link_list]
			return aug_link_list

	@tasks.loop(seconds=1)
	async def source_queue_processor(self):
		if not self.source_queue.empty():
			source, priority = self.source_queue.get()
			self.logger.info("song to find: " + str(source))
			if priority == "schlorp":
				self.make_schlorp(source)
				return
			location = determine_song_location(source)
			if location == "online":
				# Get song from YT
				link_list = await self.yt_lookup(source, True)
				song_title = link_list[0].get("title")
				song_href = link_list[0].get("link")
				if not self.recentSongList.contains(song_title):  # If new song
					if self.recentSongList.size == 10:
						os.remove(song_title + '.mp3')
						self.recentSongList.remove(self.recentSongList.tail)
					self.logger.info(f"Adding to recent list => {song_title} : {song_href}")
					self.recentSongList.add(song_title, song_href)
					with yt_dlp.YoutubeDL() as ydl:
						song_info = ydl.extract_info(song_href, download=False)
					url = (song_format["url"] for song_format in song_info['formats']
							if song_format["ext"] == 'webm')
					save_to_recent = priority in ["high", "low"]
					self.download_queue.put((song_href, song_title if save_to_recent else priority + '¬' + source, save_to_recent))
					if not save_to_recent:
						return
					source = next(url)
				else:
					source = './recent/' + song_title + '.mp3'
			source = nextcord.FFmpegPCMAudio(source, **self.ffmpeg_options)
			source = nextcord.PCMVolumeTransformer(source, 1.0)
			source.volume = 0.5
			self.player_queue.put((source, priority))

	def make_schlorp(self, name):
		schlorp_ind = random.randint(1, 2)
		greet = 1#random.randint(1, 3)
		name = name.replace("'", '')
		create_TTS(name, 'schlorp')
		name = name.replace(' ','')
		path = f"./result{name}.mp3"
		start = f"schlorp/schlorp_{str(schlorp_ind)}.mp3"
		middle = f"schlorp/{name}.mp3"
		end = f"schlorp/indi_{str(greet)}.mp3"
		cmd = 'ffmpeg -y -i "concat:' + start + '|' + middle + '|' + end + '" -c copy ' + path
		os.system(cmd)
		self.source_queue.put((path, "high"))

	@commands.command(name='play',
					help=f"play audio from youtube, args are used to search for the result to play",
					brief='play audio from youtube')
	async def play(self, ctx, *args):
		arg_unioned = '+'.join([str(arg) for arg in args])
		self.source_queue.put((arg_unioned, 'low'))

	@commands.command(name='speak',
					  help=f'Make the bot speak. Available langs: {global_handlers.GTTS_LANGS}')
	async def speak(self, ctx, *args):
		lang = 'en-uk'
		if args[-1][0] == '<' and args[-1][-1] == '>':
			lang = args[-1][1:-1]
			args = args[:-1]
		arg_unioned = ' '.join([str(arg) for arg in args])
		if lang in global_handlers.GTTS_LANGS:
			create_TTS(arg_unioned, './', lang, alt_naming_scheme=True)
			self.source_queue.put(('./speak.mp3', 'high'))
		else:
			ctx.send(f"Language {lang} not available")

	@commands.command(name='replay',
					help='play most recently played audio',
					brief='play most recently played audio')
	async def replay(self, ctx):
		recent_song = self.recentSongList.get_recent()
		if recent_song:
			self.source_queue.put((recent_song, "low"))

	@commands.command(name='playPlaylist',
					help='playPlaylist takes one arg playlist name, wipes the song queue, use ClearQueue to stop',
					brief='Play a playlist')
	async def play_playlist(self, ctx, arg):
		if not (arg in self.playlist_dict):
			await ctx.send('Playlist not found')
		else:
			playlist = self.playlist_dict[arg]
			song = playlist.get_head()
			if song is None:
				await ctx.send("Empty playlist")
			else:
				list_of_songs = playlist.to_list()
				shuffle(list_of_songs)
				for song_node in list_of_songs:
					song_name = song_node.get_name()
					self.source_queue.put(('./' + arg + '/££' + song_name + '.mp3', 'low'))

	@commands.command(name='listPlaylists',
					help='list all available playlists',
					brief='list all playlists')
	async def list_playlists(self, ctx):
		embed = nextcord.Embed(title="Playlists", description="List of available playlists and their songs",
		                      color=0x813d9c)
		for playlist in self.playlist_dict:
			self.logger.info(playlist)
			songs = ""
			for song in self.playlist_dict[playlist].to_list():
				if song:
					songs += song.get_name() + "\n"
			embed.add_field(name=playlist, value=songs, inline=False)
		await ctx.send(embed=embed)

	@commands.command(name='addPlaylist',
					help='add new playlist, supplied arg is the playlist name to be made',
					brief='add new playlist')
	async def add_playlist(self, ctx, arg):
		if arg is not None:
			if arg not in self.playlist_dict:
				self.playlist_dict[arg] = helper_classes.SongList()
				global_handlers.FILEQUEUE.put("playlists")
				await ctx.send(f"Playlist with name: {arg} created")
			else:
				await ctx.send(f"Playlist with name: {arg} already exists")
		else:
			await ctx.send(f"Command requires argument")

	@commands.command(name='addSong',
					help='launch interactive modal for adding song to playlists',
					brief='add a song to a playlist')
	async def add_song_to_playlist(self, ctx):
		selector = helper_classes.SongView(self.playlist_dict.keys())
		await ctx.send(view=selector)
		await selector.wait()
		await ctx.send(f"Adding song: {selector.song_to_find} \nTo playlist: {selector.select.values[0]}")
		link_list = await self.yt_lookup(selector.song_to_find, True)
		song_title = link_list[0].get("title")
		song_href = link_list[0].get("link")
		playlist_name = selector.select.values[0]
		self.playlist_dict[playlist_name].add(song_title, song_href)
		print(song_title)
		print(song_href)
		if not os.path.exists(playlist_name + '/££' + song_title + '.mp3'):
			self.download_queue.put((song_href, playlist_name + "¬" + song_title, False))
		global_handlers.FILEQUEUE.put('playlists')
		await ctx.send(f"{song_title} added to playlist {playlist_name}")




def setup(bot):
	bot.add_cog(SourceCog(bot))
