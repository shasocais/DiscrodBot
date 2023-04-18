import nextcord
from nextcord.ext import commands
from nextcord.ext import tasks
import yt_dlp
from yt_dlp.utils import DownloadError
from selenium import webdriver
from pyvirtualdisplay import Display
import logging
import asyncio
import queue

from selenium.webdriver.common.by import By
from typing import List

import global_handlers
from general_functions import *
import os


class DownloadCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.downloadQueue = global_handlers.DOWNLOADQUEUE
		self.playlist_dict = global_handlers.PLAYLISTDICT
		self.sourceQueue = global_handlers.SOURCEQUEUE
		self.recentSongList = global_handlers.RECENTSONGLIST
		self.logger = global_handlers.GLOBAL_LOGGER
		self.exit = None
		self.download_queue_processor.start()

	class MyLogger(object):
		def debug(self, msg):
			print(msg)

		def warning(self, msg):
			print(msg)

		def error(self, msg):
			print(msg)

	def my_hook(self, d):
		if d['status'] == 'finished':
			self.logger.info('Done downloading, now converting ...')

	ydl_optsCust = {
		'format': 'bestaudio/best',
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
		'noplaylist': True,
		'logger': MyLogger(),
		'progress_hooks': [my_hook],
	}

	"""

		SONG ACQUISITION

		"""

	# saves recent songs
	async def grab_song(self, url, name):
		name = name.replace("/", '')
		ydl_opts = self.ydl_optsCust
		ydl_opts['outtmpl'] = './recent/' + name + '.%(ext)s'
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])

	async def download_song(self, dir, songname, songUrl):
		songname = songname.replace("/", '')
		ydl_optsCust = {
			# 'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192',
			}],
			'noplaylist': True,
			'outtmpl': './' + dir + '/££' + songname + '.%(ext)s',
			'logger': self.MyLogger(),
			'progress_hooks': [self.my_hook],
		}
		with yt_dlp.YoutubeDL(ydl_optsCust) as ydl:
			try:
				ydl.download([songUrl])
			except DownloadError:
				self.logger.info("Caught Download Error: ", DownloadError.msg)
				return DownloadError.msg
		return ""

	@tasks.loop(seconds=1)
	async def download_queue_processor(self):
		if not self.downloadQueue.empty():
			source, title, save_to_recent = self.downloadQueue.get()
			if save_to_recent:
				await self.grab_song(source, title)
			else:
				# save to dir
				[directory, song_title] = title.split('¬')
				result = await self.download_song(directory, song_title, source)
				if result != "":
					# Download failed look for alternative
					self.sourceQueue.put((song_title, directory))
					return
				# successfuly downloaded, ensure playlist href matches
				if self.playlist_dict.get(directory) and self.playlist_dict[directory].contains(song_title):
					song_node = self.playlist_dict[directory].retrieve(song_title)
					if song_node.get_url != source:
						song_node.set_url(source)
				if self.downloadQueue.empty():
					global_handlers.FILEQUEUE.put("playlists")


def setup(bot):
	bot.add_cog(DownloadCog(bot))
