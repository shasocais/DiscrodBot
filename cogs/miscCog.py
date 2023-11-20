import random
import urllib.request
import imgkit

import nextcord
from nextcord.ext import commands

import global_handlers
from general_functions import char_offsets, generate_meme_square, create_TTS
from helper_classes import PollView, YAView

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class MiscCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.exit = None
		self.logger = global_handlers.GLOBAL_LOGGER
		self.poll_dict = global_handlers.POLLLIST
		options = Options()
		prefs = {'download.default_directory': os.path.abspath("./themes/")}
		options.add_experimental_option('prefs', prefs)
		options.add_argument('ignore-certificate-errors')
		options.headless = True
		self.display = global_handlers.DISPLAY
		self.browser = webdriver.Chrome(options=options)

	@commands.command(name="yahoo_scrape",
					  help="Get Question and top answer from Yahoo Answers archive for related search.",
					  brief="Explore yahoo answers archives")
	async def yahoo_scrape(self, ctx, *args):
		text = " ".join([str(arg) for arg in args])
		if len(text) > 0:
			await self.answers_scrape(text, ctx)
		else:
			ctx.send("Yahoo scrape requires search arguments")

	async def answers_scrape(self, arg, ctx):
		try:
			string = "https://y-answers.com/"
			self.browser.get(string)
			search_field = WebDriverWait(self.browser, 2).until(
				EC.presence_of_element_located((By.ID, 'search_phrase')))
			search_field.send_keys(arg)
			search_field.send_keys(Keys.RETURN)
			nav_list = WebDriverWait(self.browser, 2).until(
				EC.presence_of_all_elements_located((By.CLASS_NAME, 'question-container')))
			index = random.randint(0, len(nav_list) - 1)
			nav_list[index].find_elements(By.XPATH, '*')[1].click()
			qs_element = WebDriverWait(self.browser, 1).until(
				EC.presence_of_element_located((By.CLASS_NAME, 'question-container')))
			header_string = qs_element.find_element(By.CLASS_NAME, 'question-name').text
			questing_string = qs_element.find_element(By.CLASS_NAME, 'question-text').text
			answer_container_element = WebDriverWait(self.browser, 1).until(
				EC.presence_of_element_located((By.CLASS_NAME, 'answer-container')))
			favourite_answer_string = answer_container_element.find_element(By.CLASS_NAME, 'answer-text').text
			if header_string in questing_string:
				header_string = ""
			result = "Question: <br> <br> <h>"\
					+ header_string + "</h> <br>" + questing_string + "<br><br> Answer: <br><br>" + favourite_answer_string
			imgkit.from_string(result, 'answer_out.jpg')
			create_TTS(result.replace('<br>',''),'.',override_name="YAout",alt_naming_scheme=True)
			interactive_view = YAView(global_handlers.SOURCEQUEUE)
			await ctx.send(file=nextcord.File('answer_out.jpg'), view= interactive_view)
		except Exception as e:
			print(e)
			await ctx.send("No such yahoo answers result")

	async def wiki_scrape(self, ctx):
		string = "https://www.wikihow.com/Special:Randomizer"
		self.browser.get(string)

		img_list = WebDriverWait(self.browser, 1).until(
			EC.presence_of_all_elements_located((By.CLASS_NAME, 'whcdn')))
		index = random.randint(0, len(img_list) - 1)
		html = img_list[index].get_attribute('data-src')
		urllib.request.urlretrieve(html, "How.jpg")
		await ctx.send(file=nextcord.File('How.jpg'))

	@commands.command(name="how",
					  help="Displays a random WikiHow image",
					  brief="A taste of WikiHow")
	async def how(self, ctx):
		await self.wiki_scrape(ctx)

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
		interactive_view = PollView(self.poll_dict)
		await ctx.send(view=interactive_view)

	@commands.command(name="polls",
					  help='Opens poll management view',
					  brief='View/Edit polls')
	async def polls(self, ctx):
		await self.print_poll(ctx)


def setup(bot):
	bot.add_cog(MiscCog(bot))
