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
		self.playerQueue = global_handlers.PLAYERQUEUE
		self.downloadQueue = global_handlers.DOWNLOADQUEUE
		self.sourceQueue = global_handlers.SOURCEQUEUE
		self.recentSongList = global_handlers.RECENTSONGLIST
		self.exit = None
		self.logger = global_handlers.GLOBAL_LOGGER
		self.source_queue_processor.start()
		self.base_yt_string = 'https://www.youtube.com/'
		options = Options()
		options.headless = True
		self.browser = webdriver.Chrome(options=options)
		self.display = Display(visible=False, size=(800, 600))
		self.display.start()

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
		if not self.sourceQueue.empty():
			source, priority = self.sourceQueue.get()
			self.logger.info("song to find: " + str(source))
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
					self.recentSongList.add(song_title, song_href)
					with yt_dlp.YoutubeDL() as ydl:
						song_info = ydl.extract_info(song_href, download=False)
					url = (song_format["url"] for song_format in song_info['formats']
							if song_format["ext"] == 'webm')
					save_to_recent = priority in ["high", "low"]
					self.downloadQueue.put((song_href, song_title if save_to_recent else priority + '¬' + source, save_to_recent))
					if not save_to_recent:
						return
					source = next(url)
				else:
					source = './recent/' + song_title + '.mp3'
			source = nextcord.FFmpegPCMAudio(source, **self.ffmpeg_options)
			source = nextcord.PCMVolumeTransformer(source, 1.0)
			source.volume = 0.5
			self.playerQueue.put((source, priority))

	@commands.command(name='play')
	async def play(self, ctx, *args):
		arg_unioned = '+'.join([str(arg) for arg in args])
		self.sourceQueue.put((arg_unioned, 'low'))

	@commands.command(name='play2')
	async def play2(self, ctx, *args):
		arg_unioned = '+'.join([str(arg) for arg in args])
		self.sourceQueue.put((arg_unioned, 'high'))

	@commands.command(name='replay')
	async def replay(self, ctx):
		recent_song = self.recentSongList.get_recent()
		if recent_song:
			self.sourceQueue.put((recent_song, "low"))

	@commands.command(name='playPlaylist',
					help='!playPlaylist takes one arg playlist name, wipes the song queue, use ClearQueue to stop',
					brief='Play a playlist')
	async def play_playlist(self, ctx, arg):
		if not (arg in self.playlist_dict):
			await ctx.send('Playlist not found')
		else:
			playlist = self.playlist_dict[arg]
			song = playlist.head
			if song is None:
				await ctx.send("Empty playlist")
			else:
				list_of_songs = playlist.to_list()
				shuffle(list_of_songs)
				for song_node in list_of_songs:
					song_name = song_node.get_data()["Title"]
					self.sourceQueue.put(('./' + arg + '/££' + song_name, 'low'))


def setup(bot):
	bot.add_cog(SourceCog(bot))
