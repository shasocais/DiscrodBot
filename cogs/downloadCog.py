import random

from nextcord.ext import commands
from nextcord.ext import tasks
import yt_dlp
from yt_dlp.utils import DownloadError
from helper_classes import my_hook
import asyncio
from svgelements import *
from io import StringIO
from textwrap import dedent

from selenium.webdriver.common.by import By

import global_handlers
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display


class DownloadCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.downloadQueue = global_handlers.DOWNLOADQUEUE
		self.playlist_dict = global_handlers.PLAYLISTDICT
		self.sourceQueue = global_handlers.SOURCEQUEUE
		self.recentSongList = global_handlers.RECENTSONGLIST
		self.theme_dict = global_handlers.THEMEDICT
		self.logger = global_handlers.GLOBAL_LOGGER
		self.exit = None
		self.download_queue_processor.start()
		options = Options()
		prefs = {'download.default_directory': os.path.abspath("./themes/")}
		options.add_experimental_option('prefs', prefs)
		options.headless = True
		self.display = global_handlers.DISPLAY
		self.browser = webdriver.Chrome(options=options)

	keyLookup = {
		"sharp": {
			0: {
				'Major': 'C',
				'Minor': 'Am'
			},
			1: {
				'Major': 'G',
				'Minor': 'Em'
			},
			2: {
				'Major': 'D',
				'Minor': 'Bm'
			},
			3: {
				'Major': 'A',
				'Minor': '^Fm'
			},
			4: {
				'Major': 'E',
				'Minor': '^Cm'
			},
			5: {
				'Major': 'B',
				'Minor': '^Gm'
			},
			6: {
				'Major': '^F',
				'Minor': '_Em'
			},
			7: {
				'Major': '^C',
				'Minor': '_Bm'
			}
		},
		"flat": {
			0: {
				'Major': 'C',
				'Minor': 'Am'
			},
			1: {
				'Major': 'F',
				'Minor': 'Dm'
			},
			2: {
				'Major': '_B',
				'Minor': 'Gm'
			},
			3: {
				'Major': '_E',
				'Minor': 'Cm'
			},
			4: {
				'Major': '_A',
				'Minor': 'Fm'
			},
			5: {
				'Major': '_D',
				'Minor': '_Bm'
			},
			6: {
				'Major': '_G',
				'Minor': '_Em'
			},
			7: {
				'Major': '_C',
				'Minor': '^Gm'
			}
		}
	}

	class MyLogger(object):
		def debug(self, msg):
			print(msg)

		def warning(self, msg):
			print(msg)

		def error(self, msg):
			print(msg)

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

	async def download_song(self, dir, songname, songUrl):
		songname = songname.replace("/", '')
		ydl_opts = self.ydl_optsCust
		ydl_opts[
			'outtmpl'] = './recent/' + songname + '.%(ext)s' if dir == "recent" else './' + dir + '/££' + songname + '.%(ext)s'
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			try:
				ydl.download([songUrl])
			except DownloadError:
				self.logger.info("Caught Download Error: ", DownloadError.msg)
				return DownloadError.msg
		return ""

	async def process_svg_into_abc_file(self, svg, major, title):
		key = self.keyLookup['sharp'][0]['Major' if major else 'Minor']
		alto = '''V: Alto clef=treble
        |'''
		bass = '''V: Bass clef=bass middle=d,,
        |'''
		abc_file = dedent(f'''\
        X: 1
        T: {title}
        M: 4/4
        L: 1/8
        Q: 90
        R: key\n''')
		alto_boxes = []
		bass_boxes = []
		processing_alto = True
		svg = SVG.parse(StringIO(svg))
		element_groups = [el for el in svg.elements()]
		for index, element in enumerate(element_groups):
			if isinstance(element, Group) and "data-name" in element.values:
				if element.values['data-name'] == "staff-extra key-signature":
					# Key Found
					group = Group(element)
					sharp = any('sharp' in el.values['data-name'] for el in group)
					key = self.keyLookup['sharp' if sharp else 'flat'][len(group)]['Major' if major else 'Minor']
				elif element.values['data-name'] == "note":
					group = Group(element)
					if any(["sharp" in el.values['data-name'] for el in group if 'data-name' in el.values]):
						accidentals = 2
					else:
						accidentals = 1 if any(
							["flat" in el.values['data-name'] for el in group if 'data-name' in el.values]) else 0
					note_elements = [el for el in group if not any(
						x in el.values['data-name'] for x in ['accidentals', 'dots', 'stem', 'ledger', 'lyric'])]
					note = "".join(note_element.values['data-name'] for note_element in note_elements)
					x_ind = note_elements[0].z_point.x
					(alto_boxes if processing_alto else bass_boxes).append(
						{"note": note, "x": x_ind, 'duration': 2, "slide": False, 'accidental': accidentals,
						 'chord': len(note_elements) > 1})

				elif element.values['data-name'] == "bar":
					if (not processing_alto):
						break
					elif isinstance(element_groups[index + 3], Group):
						processing_alto = False
						continue
					# End of row, process conjunctionselement_groups[index + 3].values
					start_index = index + 3
					end_index = start_index + 1
					tgtElement = element_groups[end_index]
					while (isinstance(tgtElement, Path)):
						end_index += 1
						tgtElement = element_groups[end_index]
					# for each bar section process bar + additional blocks
					for bar_element in [Path(el) for el in element_groups[start_index:end_index]]:
						line_elems = bar_element.as_subpaths()
						for line_elem in line_elems:
							bbox = line_elem.bbox()
							if (bbox[2] - bbox[0] > 10):
								# Bar
								for note in (alto_boxes if processing_alto else bass_boxes):
									if (bbox[2] + 7 > note['x'] > bbox[0] - 7):
										# in Bar
										note["duration"] /= 2
							else:
								# Dingle
								for note in (alto_boxes if processing_alto else bass_boxes):
									if (bbox[2] + 7 > note['x'] > bbox[0] - 7):
										# in Dingle
										note["slide"] = True

					processing_alto = False
		for entry in alto_boxes:
			if (entry['slide']):
				entry['note'] = f">{entry['note']}"
			if (entry['chord']):
				entry['note'] = f"[{entry['note']}]"
			alto += f"{entry['note']}{int(entry['duration'])}{' ' if entry['duration'] > 1 else ''}"
		alto += '|'
		for entry in bass_boxes:
			if (entry['slide']):
				entry['note'] = f">{entry['note']}"
			if (entry['chord']):
				entry['note'] = f"[{entry['note']}]"
			bass += f"{entry['note']}{int(entry['duration'])}{' ' if entry['duration'] > 1 else ''}"
		bass += '|'
		abc_file += dedent(f'''\
        K: {key}
        {alto}
        {bass}''')

		abc_file = dedent(abc_file)

		with open(f"{title}_theme_abc.abc", "w") as file:
			file.write(abc_file)
			file.close()
		return

	@commands.command(name="themeTest")
	@commands.is_owner()
	async def theme_test(self, ctx):
		await self.scrape_musical_name("W1LS0N", 123)

	@commands.command(name="regenTheme")
	async def regen_theme(self, ctx):
		await self.scrape_musical_name(ctx.author.name, ctx.author.id)
		await ctx.send(f"Theme regenerated for {ctx.author.name}")

	async def scrape_musical_name(self, name, id):

		string = "http://www.clarallel.com/"  # "http://kickthejetengine.com/langorhythm/"
		self.browser.get(string)
		print("Browser at site")
		field_list = WebDriverWait(self.browser, 1).until(
			EC.presence_of_all_elements_located((By.TAG_NAME, 'input')))
		button_list = WebDriverWait(self.browser, 1).until(
			EC.presence_of_all_elements_located((By.TAG_NAME, 'button')))
		text_field = field_list[0]
		text_field.send_keys(name)
		major = True
		if True or random.choice([1, 2]) == 1:
			[button for button in button_list if button.accessible_name == "Minor"][0].click()
			major = False
		else:
			[button for button in button_list if button.accessible_name == "Major"][0].click()
		[button for button in button_list if button.accessible_name == "Convert"][0].click()

		svg_list = WebDriverWait(self.browser, 1).until(
			EC.presence_of_all_elements_located((By.TAG_NAME, 'svg')))
		tgtsvg = svg_list[0].get_attribute("outerHTML")
		await self.process_svg_into_abc_file(tgtsvg, major, name)

		cmd = f"abc2midi {name}_theme_abc.abc -o ./themes/{name}_theme.mid"
		os.system(cmd)
		wd = os.getcwd()
		os.chdir("themes")
		await asyncio.sleep(0.2)
		cmd = f"timidity -Ow {name}_theme.mid && ffmpeg -y -i {name}_theme.wav ££{str(id)}50.mp3"  # && rm {name}_theme.mid && rm {name}_theme.wav"
		os.system(cmd)
		os.chdir(wd)
		self.theme_dict[str(id)] = 50

	@tasks.loop(seconds=1)
	async def download_queue_processor(self):
		if not self.downloadQueue.empty():
			source, title, save_to_recent = self.downloadQueue.get()
			print(source, title, save_to_recent)
			if str(save_to_recent) == "theme":
				await self.scrape_musical_name(title, source)
			elif save_to_recent:
				error = await self.download_song("recent", title, source)
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
					if song_node.get_url() != source:
						song_node.set_url(source)
				if self.downloadQueue.empty():
					global_handlers.FILEQUEUE.put("playlists")


def setup(bot):
	bot.add_cog(DownloadCog(bot))
