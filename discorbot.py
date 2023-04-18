#coding=utf-8
from __future__ import unicode_literals
import discord
import random
from discord.ext.commands import Bot
from gtts import gTTS
from bs4 import BeautifulSoup
import imgkit
from html.parser import HTMLParser
from selenium import webdriver
from pyvirtualdisplay import Display
import urllib.request
import re
from subprocess import call
import time
import datetime
from collections import deque
import sys

#https
import json
import requests
from selenium.webdriver.common.keys import Keys
#ML
import matplotlib.pylab as pb
import numpy as np
from math import pi
from math import *
from scipy.spatial.distance import cdist
import scipy.optimize as opt
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#from string import maketrans
# import requests
import shutil
import youtube_dl
import asyncio
import threading
import queue
import time
import html5lib
import aiohttp
import os
#import steamapi

from keys import *

from PIL import Image

import base64


import PIL
import PIL.Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw

from natsort import natsorted


import pytesseract
import cv2

import ast

# from watson_developer_cloud import ToneAnalyzerV3

import text_to_image


# watson_url = "https://gateway-syd.watsonplatform.net/tone-analyzer/api"

# tone_analyzer = ToneAnalyzerV3(
# 	version = "2017-09-21",
# 	iam_apikey=tone_key(),
# 	url=watson_url
# 	)

# apx_url = "https://apextab.com/api/search.php?platform=pc&search="
# apx_url_tot = "https://apextab.com/api/playerplayer.php?aid="

# pubgKey = pubg_key()
# #pubgUrl = "https://api.playbattlegrounds.com/shards/" + region + "/players?filter[playerNames]=" + handle
# fortniteKey = fortnite_key()
# riotToken = riot_key()
# #leagueMainUrl = league','https://' + req.session.user.summID.region + '.api.riotgames.com/lol/league/v3/positions/by-summoner/' + req.session.user.summID.id'
# #leagueIDUrl = "https://" + region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + handle
# riotHeader = {'X-Riot-Token' : riotToken}
# #302e9b76-623f-4be8-ad5a-6b3ac3446006
# #steamapi.core.APIConnection(api_key=steam_key(),validate_key=True)
# api = core.PUBGAPI(pubg_core())
html_parser = HTMLParser()
display = Display(visible=0,size=(800,600))
display.start()


async def getTone():
	pass
	# global ServerChan
	# text = ''
	# async for message in my_bot.get_channel(ServerChan).history(limit=100):
	# 	#print(message.content)
	# 	if message.content is not None:
	# 		text = text + message.content + '\n'
	# tone_analysis = tone_analyzer.tone(
 #    {'text': text},
 #    'application/json'
	# ).get_result()
	# jsan = tone_analysis
	# doc = jsan["document_tone"]["tones"]
	# sent = jsan["sentences_tone"]
	# #print(doc)
	# outMsg = "The chat's recent tone: \n"
	# for tone in doc:
	# 	outMsg = outMsg + tone["tone_name"] + " : " + str(tone["score"]) + "\n"
	# await my_bot.get_channel(ServerChan).send(outMsg)
	#print(sent)
	#print(tone_analysis)

	#print(json.dumps(tone_analysis, indent=2))
	
def getSummonerID(region,handle):
	pass
	# global riotHeader
	# leagueExUrlID = "https://" + str(region) + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + str(handle)
	# response = requests.get(leagueExUrlID,headers=riotHeader)
	# data = json.loads(response.content.decode('utf-8'))
	# print(data)
	# return data
#chromedriver = "/usr/local/bin/chromedriver"
#os.environ["webdriver.chrome.driver"] = chromedriver
#browser = webdriver.Firefox()

current_season = '2018-03'
ScreamChamber = 282975292182495232
ServerChan = 125262622508449792
playbackVol = 50
songStart = 0
currentlyPlaying = ''
# Johnny chan id
# 282975292182495232
# Johnny serv id
# global ServerChan
# Johnny text chan id
# 338789467072495627

my_bot = Bot(command_prefix="!")
# ' chan id for general 124619490297249792'
codespls = 'af : Afrikaans  q : Albanian \nar : Arabic   hy : Armenian \nbn : Bengali   ca : Catalan \nzh : Chinese   zh-cn : Chinese (Mandarin/China) \nzh-tw : Chinese (Mandarin/Taiwan)   zh-yue : Chinese (Cantonese) \nhr : Croatian   cs : Czech \nda : Danish   nl : Dutch \nen : English   en-au : English (Australia) \nen-uk : English (United Kingdom)   en-us : English (United States) \neo : Esperanto   fi : Finnish \nfr : French   de : German \nel : Greek   hi : Hindi \nhu : Hungarian   is : Icelandic \nid : Indonesian   it : Italian \nja : Japanese   km : Khmer (Cambodian) \nko : Korean   la : Latin \nlv : Latvian   mk : Macedonian \nno : Norwegian   pl : Polish \npt : Portuguese   ro : Romanian \nru : Russian   sr : Serbian \nsi : Sinhala   sk : Slovak \nes : Spanish   es-es : Spanish (Spain) \nes-us : Spanish (United States)   sw : Swahili \nsv : Swedish   ta : Tamil \nth : Thai   tr : Turkish \nuk : Ukrainian   vi : Vietnamese \ncy : Welsh'
languages = ['af','sq','ar','hy','bn','ca','zh','zh-cn','zh-tw','zh-yue','hr','cs','da','nl','en','en-au','en-uk','en-us','eo','fi','fr','de','el','hi','hu','is','id','it','ja','km','ko','la','lv','mk','no','pl','pt','ro','ru','sr','si','sk','es','es-es','es-us','sw','sv','ta','th','tr','uk','vi','cy']
commands = "List of commands: \nspecify assist and a command keyword to get extra info \nPLAYBACK\n!play, !replay, !pause, !skip, !resume, !loop, !ClearQueue, !find, !findAlt\nPLAYLISTS\n!makePlaylist, !removePlaylist, !playPlaylist, !listPlaylists, !playlistSongs, !addSong, !removeSong \nPICTURES\n!yots, !rxn\nSOUND\n!bitch, !say, !fagin, !anxiety, !mistake, !nope, !pump, !gargle, !job, !muffins, !goblins, !ergh, !meme, !crazy, !bastard, !die, !fishie, !trash, !brand, !dingus, !jokes, !turns, !serenade, !rochefuck, !canada, !soGood, !loser, !warcrime, !earholes, !baba, !fuckYou, !kids, !curse, !santa, !yummy\nGAMEPLAY\n!pubg"

exitFlag = 0  # Currently unused, as bot has no shutdown process
songQueue = queue.Queue(20)  # Songs to play
dlQueue = queue.Queue(20)
instQueue = queue.Queue(10)  # Instructions to process
playerQueue = queue.Queue(1)  # Allows pause/skip commands
announceQueue = queue.Queue(1)  # As above but for the mp3 responses
playing = queue.Queue(1)  # Locks out announce mp3 when playing song
announcing = queue.Queue(1)  # Locks out songs when playing announce mp3
eventQueue = queue.Queue(10)  # Queue for announces
words = queue.Queue(10)
lang = queue.Queue(10)
repeat = queue.Queue(1)
greetQ = queue.Queue(1)
playerDeque = deque()
announceDeque = deque()
rxDict = {}
soundDict = {}
themeDict = {}
MemberDict = {}
BirthDict = {}
RiotDict = {}
PubgDict = {}
HouseRulesDict = {}
Dictate = ''
DictateAns = ''
prepNext = queue.Queue(1)
nextPrepped = queue.Queue(1)

distStat = queue.Queue(1)
playerStat = queue.Queue(1)
announceStat = queue.Queue(1)
greetStat = queue.Queue(1)
dlStat = queue.Queue(1)
fileStat = queue.Queue(1)

currentPoll = ['',{}, None, 0]
#fp.setPreference("webdriver.load.strategy","unstable")
# allclear = queue.Queue(1)

mangoDict = {}

client = discord.Client()


"""

CLASSES


"""


class MyLogger(object):
	def debug(self, msg):
		pass

	def warning(self, msg):
		pass

	def error(self, msg):
		print(msg)


def my_hook(d):
	if d['status'] == 'finished':
		print('Done downloading, now converting ...')


ydl_optsCust = {
	'format': 'bestaudio/best',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
	'noplaylist': True,
	#'outtmpl':'/dir/££' + 'name' + '%(ext)s',
	'logger': MyLogger(),
	'progress_hooks': [my_hook],
}
#with youtube_dl.YoutubeDL(ydl_optsCust) as ydl:
#    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])

class Poll:
	def __init__(self, Qs, opts, message, total , ident):
		self.Qs = Qs
		self.opts = opts
		self.message = message
		self.total = total
		self.ident = ident
		self.next = None
		self.prev = None

	def getNext(self):
		return self.next

	def getPrev(self):
		return self.prev

	def getQs(self):
		return self.Qs

	def getOpts(self):
		return self.opts

	def getMessage(self):
		return self.message

	def getTotal(self):
		return self.total

	def getIdent(self):
		return self.ident

	def setNext(self, Next):
		self.next = Next

	def setPrev(self, Prev):
		self.prev = Prev

	def setQs(self, Qs):
		self.Qs = Qs

	def setOpts(self, opts):
		self.opts = opts

	def setMessage(self, message):
		self.message = message

	def setTotal(self, total):
		self.total = total

	def setIdent(self, ident):
		self.ident = ident

class PollList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def getHead(self):
		return self.head

	def add(self, Qs, opts, message, total, ident=-1):
		if self.head is not None and ident == -1:
			ident = self.head.getIdent() + 1
		elif ident == -1:
			ident = 0
		poll = Poll(Qs, opts, message, total, ident)
		if self.head is not None:
			poll.setNext(self.head.getNext())
			self.head.setNext(poll)
			poll.getNext().setPrev(poll)
			poll.setPrev(self.head)
			self.head = poll
		else:
			poll.setPrev(poll)
			poll.setNext(poll)
			self.head = poll
		self.size = self.size + 1
		return poll

	def remove(self, ident):
		found, ind = self.search(ident)
		if found:
			ind.getNext().setPrev(ind.getPrev())
			ind.getPrev().setNext(ind.getNext())
			if ind is self.head:
				self.head = ind.getPrev()
			if ind is self.tail:
				self.tail = ind.getNext()
			if self.size == 1:
				self.head = None
				self.tail = None
			self.size = self.size - 1
			os.remove('polls/££' + str(ident) + 'tastyPie.png')



	def search(self, ident):
		current = None
		if self.head is not None:
			current = self.head
			found = False
			#print(item)
			while current is not None and not found:
				#print(current.getData())
				if current.getIdent() == ident:
					found = True
				else:
					current = current.getNext()
					if current is self.head:
						break
		else:
			found = False
		return (found, current)

	def writeOut(self):
		file = open("polls/££polls.txt", 'w')
		writtenText = "("
		done = False;
		current = self.head
		while not done:
			if not (current is None):
				qs = current.getQs()
				opts = current.getOpts()
				tot = current.getTotal()
				ident = current.getIdent()
				writtenText = writtenText + "[" + qs + "`" + str(opts) + "`" + str(tot) + "`" + str(ident) + "]/"
				current = current.getNext()
				if(current == self.head or current is None):
					done = True 
			else:
				done = True 
		writtenText = writtenText + ")"          
		file.write(writtenText)
		file.close()



class PlaylistEntry:
	def __init__(self, initname, initurl):
		self.name = initname
		self.url = initurl
		self.next = None
		self.prev = None

	def getUrl(self):
		return self.url

	def getName(self):
		return self.name

	def getNext(self):
		return self.next

	def getPrev(self):
		return self.prev

	def setUrl(self, newurl):
		self.url = newurl

	def setName(self, newname):
		self.name = newname

	def setNext(self, newnext):
		self.next = newnext
 	
	def setPrev(self, newprev):
		self.prev = newprev

class Playlist:
	def __init__(self, initname):
		self.head = None
		self.tail = None
		self.name = initname
		self.next = None
		self.prev = None

	def getName(self):
		return self.name

	def getNext(self):
		return self.next

	def getPrev(self):
		return self.prev

	def setName(self, newname):
		self.name = newname

	def setNext(self, newnext):
		self.next = newnext

	def setPrev(self, newprev):
		self.prev = newprev

	def isEmpty(self):
		return self.head is None

	def getHead(self):
		return self.head

	def add(self, name, url):
		#print( name + " <> " + url)
		if not self.search(name):
			temp = PlaylistEntry(name, url)
			if not os.path.exists('./'+self.name+'/££' + name + '.mp3'):
		   #eyyyyyyy
				print(url)
				downloadSong(self.name,name,url)
				#print('./'+self.name+'/££' + name + '.mp3')
				#print("not found \n")
			if self.head is None:
				self.head = temp
				temp.setNext(self.head)
				temp.setPrev(self.head)
			else:
				temp.setNext(self.head)
				temp.setPrev(self.head.getPrev())
				self.head.getPrev().setNext(temp)
				self.head.setPrev(temp)
				self.head = temp
		else:
			pass

	def size(self):
		current = self.head
		count = 0
		while current is not None:
			count = count + 1
			current = current.getNext()
			if current is self.head:
				break

		return count

	def getEntryUrl(self):
		return self.song.getUrl()

	def getEntryName(self):
		return self.song.getName()

	def search(self, name):
		current = self.head
		found = False
		#print(item)
		while current is not None and not found:
			#print(current.getData())
			if current.getName() == name:
				found = True
			else:
				current = current.getNext()
				if current is self.head:
					break

		return found

	def remove(self, name):
		current = self.head
		previous = None
		found = False
		if not(self.search(name)):
			pass
		else:
			while not found:
				if current.getName() == name:
					found = True
				else:
					previous = current
					current = current.getNext()

			if os.path.exists('./'+self.name+'/££' + name + '.mp3'):
				os.remove('./'+self.name+'/££' + name + '.mp3')
			if current.getNext() == current.getPrev():
				current.getNext().setNext(None)
				current.getPrev().setPrev(None)
				self.head = current.getNext()
			else:
				if previous is None:
					self.head = current.getNext()
					self.head.setPrev(current.getPrev())
					current.getPrev().setNext(self.head)
				else:
					previous.setNext(current.getNext())
					current.getNext().setPrev(previous)
			if current is self.tail:
				self.tail = current.getPrev()



class PlaylistList:

	def __init__(self):
		self.head = None
		self.tail = None

	def isEmpty(self):
		return self.head is None

	def getHead(self):
		return self.head

	def addPlaylist(self, item):
		temp = Playlist(item)
		if self.head is None:
			self.head = temp
			temp.setNext(self.head)
			temp.setPrev(self.head)
		else:
			temp.setNext(self.head)
			temp.setPrev(self.head.getPrev())
			self.head.getPrev().setNext(temp)
			self.head.setPrev(temp)
			self.head = temp

	def appendSong(self, playlistName, songName, songUrl):
		current = self.head
		#previous = None
		found = False
		if not(self.search(playlistName)):
			print("couldnt find")
			pass
		else:
			while not found:
				if current.getName() == playlistName:
					found = True
				else:
					print("cant find")
					previous = current
					current = current.getNext()
			#print("adding song")
			#print(songName + '\n')
			#print(songUrl + '\n')
			current.add(songName, songUrl)


	def size(self):
		current = self.head
		count = 0
		while current is not None:
			count = count + 1
			current = current.getNext()
			if current is self.head:
				break

		return count

	def search(self, item):
		current = self.head
		found = False
		#print(item)
		while current is not None and not found:
			#print(current.getData())
			if current.getName() == item:
				found = True
			else:
				current = current.getNext()
				if current is self.head:
					break

		return found

	def removePlaylist(self, playlistName):
		current = self.head
		previous = None
		found = False
		if not(self.search(playlistName)):
			print("not found")
			pass
		else:
			while not found:
				if current.getName() == playlistName:
					found = True
					print("Found em")
				else:
					previous = current
					current = current.getNext()

			if current.getNext() == current.getPrev():
				current.getNext().setNext(None)
				current.getPrev().setPrev(None)
				self.head = current.getNext()
			else:
				if previous is None:
					self.head = current.getNext()
					self.head.setPrev(current.getPrev())
					current.getPrev().setNext(self.head)
				else:
					previous.setNext(current.getNext())
					current.getNext().setPrev(previous)
			if current is self.tail:
				self.tail = current.getPrev()
			print("removed")
			#writeOut()

	def removeSong(self, playlistName, songName):
		current = self.head
		#previous = None
		found = False
		if not(self.search(playlistName)):
			pass
		else:
			while not found:
				if current.getName() == playlistName:
					found = True
				else:
					previous = current
					current = current.getNext()
			current.remove(songName)

	def writeOut(self):
		#with open("££playlists.txt","w") as file
		file = open("££playlists.txt", 'w')
		writtenText = ""
		done = False;
		current = self.head
		while not done:
			if not (current is None):
				name = current.getName()
				writtenText = writtenText + "<" + name + ";"
				entries = "{"
				miniDone = False
				currentSong = current.getHead()
				if not currentSong is None:
					while not miniDone:
						entries = entries + "<" + currentSong.getName() + "±" + currentSong.getUrl() + ">¬"
						currentSong = currentSong.getNext()
						if(currentSong == current.getHead() or currentSong is None):
							miniDone = True
				entries = entries + "}"
				writtenText = writtenText + entries + ">,"
				current = current.getNext()
				if(current == self.head or current is None):
					done = True 
			else:
				done = True           
		file.write(writtenText)
		file.close()
		



# Structure for the recently played song list(doubly linked list)
class SongNode:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None
		self.prev = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def getPrev(self):
		return self.prev

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext

	def setPrev(self, newprev):
		self.prev = newprev


class RecentSongList:

	def __init__(self):
		self.head = None
		self.tail = None

	def isEmpty(self):
		return self.head is None

	def getHead(self):
		return self.head

	def add(self, item):
		temp = SongNode(item)
		if self.head is None:
			self.head = temp
			temp.setNext(self.head)
			temp.setPrev(self.head)
		else:
			temp.setNext(self.head)
			temp.setPrev(self.head.getPrev())
			self.head.getPrev().setNext(temp)
			self.head.setPrev(temp)
			self.head = temp
		self.recent = temp

	def size(self):
		current = self.head
		count = 0
		while current is not None:
			count = count + 1
			current = current.getNext()
			if current is self.head:
				break

		return count

	def getRecent(self):
		return self.recent.getData()

	def search(self, item):
		current = self.head
		found = False
		#print(item)
		while current is not None and not found:
			#print(current.getData())
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
				if current is self.head:
					break

		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() is item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous is None:
			self.head = current.getNext()
			self.head.setPrev(current.getPrev())
			current.getPrev().setNext(self.head)
		else:
			previous.setNext(current.getNext())
			current.getNext().setPrev(previous)
		if current is self.tail:
			self.tail = current.getPrev()
		os.remove(current.getData + '.mp3')


# global recentSongList
recentSongList = RecentSongList()
playlistList = PlaylistList()
Polls = PollList()

"""


SHORT COMMANDS

"""
'''
gm convert drive/reactions/££anger5.png -geometry 360x360 -thumbnail 360x360 -background transparent -gravity center -extent 360x360 drive/reactions/££anger4.png -geometry 360x360 -thumbnail 360x360 -background transparent -gravity center -extent 360x360 +profile "*"  flipTest/out.gif
'''

'''
OCR isnt good enough
@my_bot.command()
async def ocr(ctx):
	await ctx.message.delete()
	image = cv2.imread("££wolf.jpg")
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	filename = "{}.png".format(os.getpid())
	gray = cv2.medianBlur(gray, 3)
	cv2.imwrite(filename,gray)

	text = pytesseract.image_to_string(Image.open(filename))
	#os.remove(filename)
	print(text)
	#cv2.imshow("Image", image)
	#cv2.imshow("Gray", gray)
	#cv2.waitKey(0)
'''

@my_bot.command()
async def poll(ctx, *args):
	opts = False
	pollQS = ""
	pollDict = {}
	currentEntry = ''
	currentPoll[3] = 0
	for arg in args:
		arg = arg.lower()
		if arg[0] == "{":
			opts = True
			arg = arg[1:]
		elif arg[-1] == "}":
			if len(arg) != 1:
				currentEntry = currentEntry + arg[:-1]
			opts = False
		if opts:
			currentEntry = currentEntry + " " + arg
		elif currentEntry == '':
			pollQS = pollQS + arg + " "
	currentEntry = currentEntry[1:]
	options = currentEntry.split(',')
	if currentEntry != '':
		for opt in options:
			if opt[0] == " ":
				opt = opt[1:]
			pollDict[opt] = 0
	if pollDict == {}:
		pollDict['yes'] = 0
		pollDict['no'] = 0
	await ctx.message.delete()
	instQueue.put(["poll", [pollQS, pollDict]])


async def maintainPoll(Qs, opts, building=False):
	global ServerChan
	global currentPoll		
	displayMsg = "Preparing Poll"
	if building:
		message = await my_bot.get_channel(ServerChan).send(displayMsg)
	else:
		message = None
	#currentPoll[0] = Qs
	#currentPoll[1] = opts
	#currentPoll[2] = message
	head = Polls.getHead()
	poll = Polls.add(Qs, opts, message, 0)
	displayMsg = str(poll.getIdent()) + " : " + Qs + "\n"
	labels = ""
	sizes = []
	count = 65
	for opt in opts:
		labels = labels + chr(count)
		count = count + 1
		displayMsg = displayMsg + "{"
		if poll.getTotal() > 0:
			sizes.append(round(opts[opt]/poll.getTotal(),2))
			prop = int(opts[opt] / poll.getTotal() * 100) // 5
		else:
			sizes.append(0.00)
			prop = 0
		for i in range(prop):
			displayMsg = displayMsg + "+"
		for i in range(prop,20):
			displayMsg = displayMsg + "×"
		displayMsg = displayMsg +  "} "
		displayMsg = displayMsg + opt + ': ' + str(opts[opt]) + "\n"
	if not building:
		pie = await pieIt(labels,sizes,6)
		displayMsg = displayMsg + "\n" + pie
	if building:
		await message.edit(content=displayMsg)
	Polls.writeOut()
	
def s(k,v,a):
	if not v:return ' '
	if a <= v[0]:return k[0]
	return s(k[1:],v[1:],a-v[0])

async def pieIt(sections, props, rad):
	print(props)
	bigPie = ''
	dia = range(-rad,rad)
	for y in dia:
		pie = ""
		for x in dia:
			if x*x+y*y<rad*rad:
				ang = atan2(y,x)/pi/2+.5
				pie = pie + s(sections, props, ang) + " "
			else:
				pie = pie + ". "
		if y != -rad:
			bigPie = bigPie + "`" + pie[2:-1] + "`\n"
		#print(pie)
	return bigPie


@my_bot.command()
async def concerned(ctx,*args):
	instQueue.put(["concerned",'ech'])


async def printPoll(ctx, ident):
	global ServerChan
	global Polls
	f, poll = Polls.search(ident)
	if f:
		labels = ""
		sizes = []
		count = 65
		displayMsg = str(poll.getIdent()) + " : " + poll.getQs() + "\n"
		for opt in poll.getOpts():
			labels = labels + chr(count)
			count = count + 1
			displayMsg = displayMsg + "{"
			if poll.getTotal() > 0:
				sizes.append(round(poll.getOpts()[opt] / poll.getTotal(),2))
				prop = int(poll.getOpts()[opt] / poll.getTotal() * 100) // 5
			else:
				prop = 0
				size.append(0.00)
			for i in range(prop):
				displayMsg = displayMsg + "+"
			for i in range(prop,20):
				displayMsg = displayMsg + "×"
			displayMsg = displayMsg +  "} "
			displayMsg = displayMsg + opt + ': ' + str(poll.getOpts()[opt]) + "\n"
		pie = await pieIt(labels,sizes,6)
		#print(pie)
		displayMsg = displayMsg + "\n" + pie
		message = await my_bot.get_channel(ServerChan).send(displayMsg)
		poll.setMessage(message)
	else:
		await ctx.send("Not an existing poll")

ASCII_CHARS = ['#','&','@','?','%','S','+','*',':','-','.',',',' ']
PIXEL_ON = 0
PIXEL_OFF = 255


@my_bot.command()
async def asciit(ctx, *args):
	extension=''
	if len(ctx.message.attachments) > 0:
		# attached ims
		count = 0
		img = ctx.message.attachments[0]
		filename = img.filename
		name, extension = filename.split('.')
		loc = './ascyyy.' + extension
		await img.save(loc)
		instQueue.put(('asciit',extension))
	else:
		ctx.send("Post a fucking img you degenerate")

async def makeAscii(extension):
	global ServerChan
	if extension == 'gif':
		command = ['gm','convert','-coalesce','ascyyy.' + extension,'+adjoin','splitch/target%d.png']
		call(command)
		asyncio.sleep(5)
		for file in os.listdir('./splitch/'):
			if file != 'subsplitch':
				#print(file)
				name, ext = file.split('.')
				image = Image.open('./splitch/' + file)
				out = await convertToAscii(image)
				f = open('./splitch/' + name + '.txt','w')
				f.write(out)
				f.close()
				im = text_to_im('./splitch/'+name+'.txt')
				im.save('./splitch/subsplitch/' + name + '.png')
				os.remove('./splitch/' + file)
				os.remove('./splitch/'+name+'.txt')
		command = ['gm','convert']
		Biglist = os.listdir('./splitch/subsplitch/')
		Biglist = natsorted(Biglist)
		for file in Biglist:
			command.append('splitch/subsplitch/' + file)
		command = command + ['-delay','5','+profile', '"*"','splitch/splutch.gif']
		call(command)
		await my_bot.get_channel(ServerChan).send(file=discord.File('splitch/splutch.gif'))
		for file in os.listdir('./splitch/subsplitch/'):
			os.remove('./splitch/subsplitch/' + file)
		os.remove('./splitch/splutch.gif')
		

	else:
		image = Image.open('ascyyy.' + extension)
		out = await convertToAscii(image)
		f = open("out.txt",'w')
		f.write(out)
		f.close()
		im = text_to_im('out.txt')
		im.save('res.png')
		await my_bot.get_channel(ServerChan).send(file=discord.File('res.png'))

def scale_im(image, new_width=100):
	(org_width, org_hgt) = image.size
	asp = org_hgt/float(org_width)
	new_hgt = int(asp * new_width)
	new_image = image.resize((new_width, new_hgt))

	return new_image

def convert_to_grayscale(image):
	return image.convert('L')

def map_pix_to_chars(image, range_width=25):
	pixels = list(image.getdata())
	pix_to_chars = [ASCII_CHARS[pixel_value//range_width] for  pixel_value in pixels]
	return "".join(pix_to_chars)

async def convertToAscii(image, new_width=100):
	image = scale_im(image)
	image = convert_to_grayscale(image)

	pix_to_chars = map_pix_to_chars(image)
	len_pix_to_chars = len(pix_to_chars)

	image_ascii = [pix_to_chars[index: index + new_width] for index in range(0, len_pix_to_chars, new_width)]

	return '\n'.join(image_ascii)

def text_to_im(file):
	with open(file) as text_file:
		text = tuple(l.rstrip() for l in text_file.readlines())

	large = 7
	font = PIL.ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf",size=large)
	#font = PIL.ImageFont.load_default()

	pt2px = lambda pt: int(round(pt * 96.0/ 72))
	max_width_line = max(text, key=lambda s: font.getsize(s)[0])

	max_height = pt2px(font.getsize('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[1])
	max_width = pt2px(font.getsize(max_width_line)[0])
	height = max_height*len(text)
	width = int(round(max_width + 40))
	image = Image.new('L', (width,height), color=PIXEL_OFF)
	draw = PIL.ImageDraw.Draw(image)

	vert = 5
	hoz = 5
	space = int(round(max_height * 0.8))
	for line in text:
		draw.text((hoz, vert),
			line, fill=PIXEL_ON,font=font)
		vert += space

	c_box = PIL.ImageOps.invert(image).getbbox()
	image = image.crop(c_box)
	image = PIL.ImageOps.invert(image)
	return image

@my_bot.command()
async def vote(ctx, *args):
	global Polls
	argu = ''
	ident = None
	for arg in args:
		if arg[0] == "[" and arg[-1] == ']':
			ident = int(arg[1:-1])
		else:
			argu = argu + ' ' + arg
	argu = argu[1:]
	await ctx.message.delete()
	f, poll = Polls.search(ident)
	if f:
		if argu in poll.getOpts():#currentPoll[1]:
			poll.getOpts()[argu] = poll.getOpts()[argu] + 1
			poll.setTotal(poll.getTotal() + 1)
			await updatePoll(ctx, poll)
		elif argu.isdigit():
			index = list(poll.getOpts().keys())[int(argu) - 1]
			poll.getOpts()[index] = poll.getOpts()[index] + 1
			poll.setTotal(poll.getTotal() + 1)
			await updatePoll(ctx, poll)
		else:
			await ctx.send("That isn't an option in that poll")
	else:
		await ctx.send("That isn't an existing poll")

async def updatePoll(ctx, poll):
	global Polls
	displayMsg = str(poll.getIdent()) + " : " + poll.getQs() + "\n"
	labels = ""
	sizes = []
	count = 65
	for opt in poll.getOpts():
		labels = labels + chr(count)
		count = count + 1
		displayMsg = displayMsg + "{"
		if poll.getTotal() > 0:
			sizes.append(round(poll.getOpts()[opt] / poll.getTotal(),2))
			prop = int(poll.getOpts()[opt] / poll.getTotal() * 100) // 5
		else:
			sizes.append(0.00)
			prop = 0
		for i in range(prop):
			displayMsg = displayMsg + "+"
		for i in range(prop,20):
			displayMsg = displayMsg + "×"
		displayMsg = displayMsg +  "} "
		displayMsg = displayMsg + opt + ': ' + str(poll.getOpts()[opt]) + "\n"
	pie = await pieIt(labels,sizes,6)
	displayMsg = displayMsg + "\n" + pie
	if poll.getMessage() is None:
		await ctx.send(content=displayMsg)
	else:
		await poll.getMessage().edit(content=displayMsg)
	Polls.writeOut()

@my_bot.command()
async def addOpt(ctx, *args):
	global Polls
	await ctx.message.delete()
	opt = ''
	ident = None
	for arg in args:
		if arg[0] == "[" and arg[-1] == ']':
			ident = int(arg[1:-1])
		else:
			opt = opt + ' ' + arg
	opt = opt[1:].lower()
	f, poll = Polls.search(ident)
	if f:
		if opt not in poll.getOpts():
			poll.getOpts()[opt] = 0
			await updatePoll(ctx, poll)
		else:
			ctx.send("That option is already in the poll")
	else:
		ctx.send("That isn't an existing poll")


@my_bot.command()
async def pollStatus(ctx, *args):
	await ctx.message.delete()
	ident = None
	for arg in args:
		if arg[0] == "[" and arg[-1] == ']':
			ident = int(arg[1:-1])
	await printPoll(ctx, ident)

@my_bot.command()
async def removePoll(ctx, *args):
	await ctx.message.delete()
	ident = None
	for arg in args:
		if arg[0] == "[" and arg[-1] == ']':
			ident = int(arg[1:-1])
	await remPoll(ctx, ident)

async def remPoll(ctx, ident):
	if ident is None:
		await ctx.send("Not an existing poll")
	else:
		Polls.remove(ident)
		await ctx.send("removing poll")
		Polls.writeOut()

@my_bot.command()
async def darkGif(ctx, *args):
	global ServerChan
	imgs = []
	if len(ctx.message.attachments) > 0:
		# attached ims
		count = 0
		for img in ctx.message.attachments:
			filename = img.filename
			name, extension = filename.split('.')
			loc = './flipTest/atch' + str(count) + extension
			await img.save(loc)
			count = count + 1
			imgs.append(loc[2:])
	await ctx.message.delete()
	wd = os.getcwd()
	os.chdir("drive/reactions/")
	for arg in args:
		print(arg)
		query = '££' + str(arg)+".png"
		query2 = '££' + str(arg)+".jpg"
		query3 = '££' + str(arg)+".gif"
		if os.path.isfile(query):
			print("png")
			imgs.append("drive/reactions/"+ query)
		elif os.path.isfile(query2):
			print("jpg")
			imgs.append("drive/reactions/"+ query2)
		elif os.path.isfile(query3):
			print("gif")
			imgs.append("drive/reactions/"+ query3)
		else:
			print("nooope")
	os.chdir(wd)
	for im in imgs:
		command = ['gm', 'convert']
		command.append(im)
		command = command + ['-geometry', '100x100%', '-thumbnail', '100x100%', '-background', 'black', '-gravity', 'center', '-extent', '100x100%']
		command = command + ['-delay','10', '+profile', '"*"','flipTest/dark.gif']
	#command = ['gm', 'convert', 'drive/reactions/££anger5.png', , 'drive/reactions/££anger4.png', '-geometry', '360x360', '-thumbnail', '360x360', '-background', 'transparent', '-gravity', 'center', '-extent', '360x360','-delay','20', '+profile', '"*"','flipTest/out.gif']
	#print(command)
		call(command)
		await my_bot.get_channel(ServerChan).send(file=discord.File("flipTest/dark.gif"))
	#os.chdir(wd)


@my_bot.command()
async def stitch(ctx, *args):
	global ServerChan
	imgs = []
	if len(ctx.message.attachments) > 0:
		# attached ims
		count = 0
		for img in ctx.message.attachments:
			print("We got atchs")
			filename = img.filename
			name, extension = filename.split('.')
			loc = './flipTest/atch' + str(count) + extension
			await img.save(loc)
			count = count + 1
			imgs.append(loc[2:])
	wd = os.getcwd()
	await ctx.message.delete()
	os.chdir("drive/reactions/")
	for arg in args:
		print(arg)
		query = '££' + str(arg)+".png"
		query2 = '££' + str(arg)+".jpg"
		query3 = '££' + str(arg)+".gif"
		if os.path.isfile(query):
			print("png")
			imgs.append("drive/reactions/"+ query)
		elif os.path.isfile(query2):
			print("jpg")
			imgs.append("drive/reactions/"+ query2)
		elif os.path.isfile(query3):
			print("gif")
			imgs.append("drive/reactions/"+ query3)
		else:
			print("nooope")
	os.chdir(wd)
	command = ['gm', 'convert']
	for im in imgs:
		command.append(im)
		if im[-3:] == 'gif':
			command = command + ['-geometry', '360x360', '-thumbnail', '360x360', '-background', 'transparent', '-gravity', 'center', '-extent', '360x360']
		else:
			command = command + ['-geometry', '360x360', '-thumbnail', '360x360', '-background', 'black', '-gravity', 'center', '-extent', '360x360']
	command = command + ['-delay','20', '+profile', '"*"','flipTest/out.gif']
	#command = ['gm', 'convert', 'drive/reactions/££anger5.png', , 'drive/reactions/££anger4.png', '-geometry', '360x360', '-thumbnail', '360x360', '-background', 'transparent', '-gravity', 'center', '-extent', '360x360','-delay','20', '+profile', '"*"','flipTest/out.gif']
	#print(command)
	call(command)
	await my_bot.get_channel(ServerChan).send(file=discord.File("flipTest/out.gif"))
	#os.chdir(wd)


@my_bot.command(help="Send command descriptions privately",brief="Private version of help")
async def assist(ctx,*args):
	await ctx.message.delete()
	global ServerChan
#	if args is "":
	#print(args)
	user = ctx.message.author
	if not args:
		await user.send(commands)
	else:
		for arg in args:

			argu = str(arg)
			#print(argu)
			if argu == 'say':
				await user.send('!say text <language-code>\nuse !codes to get a list of codes')
				break
			if argu == 'play':
				await user.send('!play youtube video keywords\nyou can then use pause resume and skip to control play')
				break
			if argu == 'find':
				await user.send('!find youtube video by keywords')
				break
			if argu == 'findAlt':
				await user.send('!findAlt youtube video keywords\nreturns 3 videos')
				break
			if argu == 'loop':
				await user.send('!loop repeat plays selection until !skip is used\n')
				break
			if argu == 'yots':
				await user.send('!yots post a yots image\n Can take anger, awe, damn, ehh, hmph, knock, meme, toss, chef, fear, what as args\n')
				break
			if argu == 'makePlaylist':
				await user.send('!makePlaylist takes one arg playlist name')
				break
			if argu == 'removePlaylist':
				await user.send('!removePlaylist takes one arg playlist name')
				break
			if argu == 'playPlaylist':
				await user.send('!playPlaylist takes one arg playlist name, wipes the song queue, use ClearQueue to stop')
				break
			if argu == 'playlistSongs':
				await user.send('!playlistSongs takes one arg playlist name')
				break
			if argu == 'addSong':
				await user.send('!addSong takes two args\n<playlist name> and song name')
				break
			if argu == 'removeSong':
				await user.send('!removeSong takes two args\n<playlist name> and song name')
				break
			if argu == 'pubg':
				await user.send('!pubg takes three args\nskill/stats, stats returns a number of stats, skill just the skill rating \nplayer, must be a steamID\nGamemode, solo, duo or squad')
				break
			if argu == 'rxn':
				mensaje = "!rxn can take an argument from:\n"	
				prevChar = ''
				for keyword in sorted(rxDict):
					if prevChar == '':
						prevChar = keyword[0]
					if prevChar != keyword[0]:
						mensaje = mensaje + '\n'
					mensaje = mensaje + ": " + keyword + " :"
					prevChar = keyword[0]
				await user.send(mensaje)
				break
			if argu == 'sound':
				mensaje = "!sound can take an argument from:\n"	
				prevChar = ''
				for keyword in sorted(soundDict):
					if prevChar == '':
						prevChar = keyword[0]
					if prevChar != keyword[0]:
						mensaje = mensaje + '\n'
					mensaje = mensaje + ": " + keyword + " :"
				await user.send(mensaje)
				break
			await user.send('command cannot take extra args')


@my_bot.command()
async def yummy(ctx):
	await ctx.message.delete()
	eventQueue.put('yummy')

@my_bot.command()
async def bitch(ctx):
	await ctx.message.delete()
	eventQueue.put('bitch')

@my_bot.command()
async def bastard(ctx):
	await ctx.message.delete()
	eventQueue.put('bastard')

@my_bot.command()
async def crazy(ctx):
	await ctx.message.delete()
	eventQueue.put('crazy')

@my_bot.command()
async def die(ctx):
	await ctx.message.delete()
	eventQueue.put('die')

@my_bot.command()
async def brand(ctx):
	await ctx.message.delete()
	eventQueue.put('myBrand')

@my_bot.command()
async def trash(ctx):
	await ctx.message.delete()
	eventQueue.put('trash')

@my_bot.command()
async def fishie(ctx):
	await ctx.message.delete()
	eventQueue.put('fishie')

@my_bot.command()
async def jokes(ctx):
	await ctx.message.delete()
	eventQueue.put('onme')

@my_bot.command()
async def dingus(ctx):
	await ctx.message.delete()
	eventQueue.put('dingus')

@my_bot.command()
async def scienceBitch(ctx):
	await ctx.message.delete()
	eventQueue.put('sciBitch')

@my_bot.command()
async def doktor(ctx):
	await ctx.message.delete()
	eventQueue.put('doktor')

@my_bot.command()
async def serenade(ctx):
	await ctx.message.delete()
	eventQueue.put('serenade')

@my_bot.command()
async def rochefuck(ctx):
	await ctx.message.delete()
	eventQueue.put('rochefuck')

@my_bot.command()
async def canada(ctx):
	await ctx.message.delete()
	eventQueue.put('canada')

@my_bot.command()
async def soGood(ctx):
	await ctx.message.delete()
	eventQueue.put('soGood')

@my_bot.command()
async def loser(ctx):
	await ctx.message.delete()
	eventQueue.put('loser')

@my_bot.command()
async def warcrime(ctx):
	await ctx.message.delete()
	eventQueue.put('warcrime')

@my_bot.command()
async def earholes(ctx):
	await ctx.message.delete()
	eventQueue.put('earholes')

@my_bot.command()
async def baba(ctx):
	await ctx.message.delete()
	eventQueue.put('baba')

@my_bot.command()
async def fuckYou(ctx):
	await ctx.message.delete()
	eventQueue.put('fuckYou')

@my_bot.command()
async def fagin(ctx):
	await ctx.message.delete()
	eventQueue.put('fagin')



@my_bot.command()
async def anxiety(ctx):
	await ctx.message.delete()
	eventQueue.put('anxiety')


@my_bot.command()
async def mistake(ctx):
	await ctx.message.delete()
	eventQueue.put('mistake')


@my_bot.command()
async def nope(ctx):
	await ctx.message.delete()
	eventQueue.put('nope')


@my_bot.command()
async def pump(ctx):
	await ctx.message.delete()
	eventQueue.put('pump')


@my_bot.command()
async def gargle(ctx):
	await ctx.message.delete()
	eventQueue.put('gargle')


@my_bot.command()
async def job(ctx):
	await ctx.message.delete()
	eventQueue.put('jobDone')


@my_bot.command()
async def muffin(ctx):
	await ctx.message.delete()
	eventQueue.put('muffin')


@my_bot.command()
async def goblins(ctx):
	await ctx.message.delete()
	eventQueue.put('goblins')


@my_bot.command()
async def ergh(ctx):
	await ctx.message.delete()
	eventQueue.put('ergh')


@my_bot.command()
async def meme(ctx):
	await ctx.message.delete()
	eventQueue.put('meme')

@my_bot.command()
async def turns(ctx):
	await ctx.message.delete()
	eventQueue.put('turns')

@my_bot.command()
async def kids(ctx):
	await ctx.message.delete()
	eventQueue.put('kids')

@my_bot.command()
async def curse(ctx):
	await ctx.message.delete()
	eventQueue.put('curse')

@my_bot.command()
async def santa(ctx):
	await ctx.message.delete()
	eventQueue.put('santa')


@my_bot.command()
async def memeSquare(ctx,*args):
	argu = ''
	for arg in args:
		argu = argu + arg
	await ctx.message.delete()
	await generateMeme(argu)

"""

PLAYLISTS


"""

@my_bot.command(help='!makePlaylist takes one arg playlist name',brief='Make a playlist')
async def makePlaylist(ctx,arg):
	await ctx.message.delete()
	global ServerChan
	if(playlistList.search(arg)):
		await my_bot.get_channel(ServerChan).send('A playlist with that name already exists')
	else:
		playlistList.addPlaylist(arg)
		if not os.path.exists(arg):
			os.makedirs(arg)
		playlistList.writeOut()

@my_bot.command(help='!removePlaylist takes one arg playlist name',brief='Remove a playlist')
async def removePlaylist(ctx,arg):
	await ctx.message.delete()
	global ServerChan
	if not(playlistList.search(arg)):
		await my_bot.get_channel(ServerChan).send('Playlist not found')
	else:
		playlistList.removePlaylist(arg)
		if os.path.exists(arg):
			shutil.rmtree(arg)
		playlistList.writeOut()

@my_bot.command(help='!playPlaylist takes one arg playlist name, wipes the song queue, use ClearQueue to stop',brief='Play a playlist')
async def playPlaylist(ctx,arg):
	await ctx.message.delete()
	global ServerChan
	if not(playlistList.search(arg)):
		await my_bot.get_channel(ServerChan).send('Playlist not found')
	else:
		current = playlistList.head
		found = False
		while not found:
			if current.getName() == arg:
				found = True
			else:
				previous = current
				current = current.getNext()
		song = current.head
		found = False
		listOfSongs = []
		if song == None:
			print("Empty list")
			await my_bot.get_channel(ServerChan).send("Empty playlist")
		else:
			while not found:
				#print('./'+arg+'/££' + song.name)
				#
				listOfSongs.append(song.name)
				song = song.getNext()
				if(song == current.head):
					found = True
			print(listOfSongs)
			random.shuffle(listOfSongs)
			print(listOfSongs)
			for songName in listOfSongs:
				songQueue.put('./'+arg+'/££' + songName)


@my_bot.command()
async def listPlaylists(ctx):
	await ctx.message.delete()
	global ServerChan
	if(playlistList.isEmpty()):
		await my_bot.get_channel(ServerChan).send('There are no playlists')
	else:
		message = ""
		head = playlistList.getHead()
		done = False
		while not done:
			name = head.getName()
			message = message + "<" + name + "> "
			head = head.getNext()
			if head is playlistList.getHead():
				done = True
		await my_bot.get_channel(ServerChan).send(message)

@my_bot.command()
async def ClearQueue(ctx):
	await ctx.message.delete()
	#with songQueue.mutex:
	#	songQueue.queue.clear()
	global ServerChan
	playerDeque.clear()
	announceDeque.clear()
	my_bot.get_guild(ServerChan).voice_client.stop()

@my_bot.command(help='!playlistSongs takes one arg playlist name',brief='List song in the playlist')
async def playlistSongs(ctx,arg):
	await ctx.message.delete()
	global ServerChan
	if not(playlistList.search(arg)):
		await my_bot.get_channel(ServerChan).send("A playlist with that name doesn't exist")
	else:
		message = arg + ":\n"
		current = playlistList.head
		#previous = None
		found = False
		while not found:
			if current.getName() == arg:
				found = True
			else:
				previous = current
				current = current.getNext()
		song = current.head
		found = False
		while not found:
			message = message + song.getName() + "\n"
			song = song.getNext()
			if(song == current.head):
				found = True
		await my_bot.get_channel(ServerChan).send(message)

@my_bot.command(help='!addSong takes two args\n<playlist name> and song name',brief='Add a song to a playlist')
async def addSong(ctx,*args):
	await ctx.message.delete()
	global ServerChan
	argu = ''
	playlistEx = False
	playlist = ''
	for arg in args:
		arg = str(arg)
		print(arg)
		if arg[0] is '<' and arg[-1:] is '>':
				#playlist choice
				#print(arg)
				arg = arg.replace('<','')
				arg = arg.replace('>','')
				print(arg)
				if (playlistList.search(arg)):
					playlistEx = True
					playlist = arg
		else:
			if argu is '':
				argu = argu + arg
			else:
				argu = argu + '+' +  arg
	argu = argu.replace(':','')
	if(playlistEx):
		#argu = argu.replace('/','')
		current = playlistList.head
		#previous = None
		found = False
		while not found:
			if current.getName() == playlist:
				found = True
			else:
				previous = current
				current = current.getNext()
		if not (current.search(argu)):
			print(argu)
			#print("Adding instruction")
			inst = ['app',(playlist,argu)]
			instQueue.put(inst)
			#await fetchAndAttach(playlist,argu)t
		else:
			await my_bot.get_channel(ServerChan).send("That song already exists in that playlist")    
	else:
		await my_bot.get_channel(ServerChan).send("Please enter a valid existing playlist")  


@my_bot.command(help='!removeSong takes two args\n<playlist name> and song name',brief='Remove a song from a playlist')
async def removeSong(ctx,*args):
	await ctx.message.delete()
	global ServerChan
	argu = ''
	playlistEx = False
	playlist = ''
	for arg in args:
		arg = str(arg)
		if arg[0] is '<' and arg[-1:] is '>':
				#playlist choice
				#print(arg)
				arg = arg.replace('<','')
				arg = arg.replace('>','')
				if (playlistList.search(arg)):
					playlistEx = True
					playlist = arg
		else:
			if argu is '':
				argu = argu + arg
			else:
				argu = argu + ' ' + arg
	if(playlistEx):
		current = playlistList.head
		#previous = None
		found = False
		while not found:
			if current.getName() == playlist:
				found = True
			else:
				previous = current
				current = current.getNext()
		if (current.search(argu)):
			playlistList.removeSong(playlist,argu)
			playlistList.writeOut()
		else:
			await my_bot.get_channel(ServerChan).send("That song doesn't exist in that playlist")    
	else:
		await my_bot.get_channel(ServerChan).send("Please enter a valid existing playlist") 


async def fetchAndAttach(playlist,argu):
	print("fetch and Attach : > " + str(argu))
	linklist = await ytLokupGrab(argu,True)
	if linklist is None:  # Checks for populated results
		pass
	else:
		songFile, songTitle = linklist[0]
		#print(songFile + " : " + playlist + " : " + argu)
		print("fetch and Attach : > " + songFile)
		print("fetch and Attach : > " + songTitle)
		songTitle = songTitle.replace('±','][')
		songTitle = songTitle.replace(';','][')
		songTitle = songTitle.replace('¬','][')
		playlistList.appendSong(playlist,songTitle,songFile)
		#print("song appended")
		playlistList.writeOut()
		print("file written")

def readPlaylists():
	file = open("££playlists.txt",'r')
	stringFile = file.read().replace('\n', '')
	stringFile = stringFile.replace('<','')
	stringFile = stringFile.replace('>','')
	stringFile = stringFile.replace('{','')
	stringFile = stringFile.replace('}','')
	playlists = [i for i in stringFile.split(',')]
	if(len(playlists) > 0):
		for playlist in playlists:
			playlistData = [j for j in playlist.split(';')]
			#print(playlistData)
			if(len(playlistData) > 1):
				playlistList.addPlaylist(playlistData[0])
				if not os.path.exists(playlistData[0]):
					os.makedirs(playlistData[0])
				if(len(playlistData[1]) > 1):
					songs = [k for k in playlistData[1].split('¬')]
					for song in songs:
						songData = [l for l in song.split('±')]
						if(len(songData) > 1):
							playlistList.appendSong(playlistData[0],songData[0],songData[1])


def readPolls():
	file = open("polls/££polls.txt", "r")
	stringfile = file.read().replace('\n', '')
	stringfile = stringfile.replace('(','')
	stringfile = stringfile.replace(')','')
	polls = [i for i in stringfile.split('/')]
	if(len(polls) > 0):
		for poll in polls:
			if poll is not '':
				listo = poll[1:-1].split('`')
				qs, opts, tot, ident = tuple(listo)
				opts = ast.literal_eval(opts)
				tot = int(tot)
				ident = int(ident)
				Polls.add(qs,opts,None,tot,ident)



"""

EVENTS

"""

@my_bot.event
@asyncio.coroutine
def on_member_update(before,after):
	global BirthDict
	now = datetime.datetime.now()
	if before.status.offline and after.status.online:
		if after.id in BirthDict:
			day, month = BirthDict[after.id]
			if int(now.day) == int(day) and int(now.month) == int(month):
				mention =' '
				mention = after.mention
				greetQ.put(mention)


@my_bot.event
@asyncio.coroutine
async def on_voice_state_update(member,before,after):
	global ScreamChamber
	global themeDict
	if member.top_role.name == 'Bot Boy':
		print("Spotted you botter")
	if ((before.channel == None and after.channel != None) or (before != after)) and member.top_role.name != 'Bot Boy':
		#try:
		if before.channel != None:
			if after.channel == None:
				print("Hes blitzing it")
				makeSchlorp(member.display_name)	
			elif before.channel.id != after.channel.id:
				if after.channel.id == ScreamChamber:
					print("Checking membership")
					print(member.id)
					print(themeDict)
					if str(member.id) in themeDict :
						print("ThemeTime")
						string = "themes/££" + str(member.id) + str(themeDict[str(member.id)]) + ".mp3"
						stringlet = 'theme' + string
						eventQueue.put('theme'+string)
					else:
						await musicTheFucker(member.display_name, member.id)
						#Give em the music	
		else:
			#print(before.channel.id)
			#if before.channel.id != after.channel.id:
			if after.channel.id == ScreamChamber:
				print("Checking membership")
				print(member.id)
				print(themeDict)
				if str(member.id) in themeDict :
					print("ThemeTime")
					string = "themes/££" + str(member.id) + str(themeDict[str(member.id)]) + ".mp3"
					stringlet = 'theme' + string
					eventQueue.put('theme'+string)
				else:
					await musicTheFucker(member.display_name, member.id)
					#Give em the music
		#except:
		#	pass
@my_bot.command()
async def echo(ctx):
	await ctx.message.delete()
	#print(themeDict)
	await getTone()

@my_bot.command()
async def musicMe(ctx):
	await ctx.message.delete()
	await musicTheFucker(ctx.message.author.display_name, ctx.message.author.id)

async def musicTheFucker(name, id):
	
	profile = webdriver.ChromeOptions()
	prefs = {'download.default_directory' : '/home/aidan/Documents/Environs/Disc_bot/DiscrodBot/themes'}
	profile.add_experimental_option('prefs', prefs)
	#profile.add_argument("download.default_directory=./Documents/Environs/Disc_bot/DiscrodBot/themes")
	browser = webdriver.Chrome(chrome_options=profile)
	string = "http://www.clarallel.com/"
	browser.get(string)
	print("Browser at site")
	textField = browser.find_element_by_name("original_name")
	textField.send_keys(name)
	print("Text set")
	if random.choice([1,2]) == 1:
		pass
	else:
		browser.find_elements_by_name("mode")[1].click()
	browser.find_element_by_class_name("btn").click()
	print("Stuff submitted")
	browser.find_element_by_link_text("Download MIDI").click()
	wd = os.getcwd()
	os.chdir("themes")
	await asyncio.sleep(1)
	cmd = 'timidity -Ow untitled.midi && ffmpeg -y -i untitled.wav ££' + str(id) + '50.mp3 && rm untitled.midi && rm untitled.wav'
	os.system(cmd)
	os.chdir(wd)
	if str(id) in themeDict:
		themeDict[str(id)] = 50
	else:
		themeDict[str(id)] = 50


"""

BIRTHDAYS


"""

async def sendGreet(mention):
	global ServerChan
	await my_bot.get_channel(ServerChan).send(mention + " happy birthday")


def readBirthdays():
	global BirthDict
	file = open("££birthday.txt",'r')
	stringfile = file.read().replace('\n','')
	stringfile = stringfile.replace('(','')
	stringfile = stringfile.replace(')','')
	birthdays = [i for i in stringfile.split(',')]
	if(len(birthdays) > 0):
		for birthday in birthdays:
			if len(birthday) > 3:
				name, day, month = birthday.split(':')
				BirthDict[name] = (day,month)


async def greetBirthdays():
	global BirthDict
	global ServerChan
	now = datetime.datetime.now()
	#print(now.day)
	#print(now.month)
	for key, value in BirthDict.items():
		day, month = value
		#print(day)
		#print(month)
		if (int(now.day) == int(day) and int(now.month) == int(month)):
			print("Greeting")
			member = my_bot.get_guild(ServerChan).get_member(int(key))
			mention = member.mention
			if not member.status.offline:
				await my_bot.get_channel(ServerChan).send(mention + " happy birthday")


def monthToNumber(argument):
	switcher = {
	'january' : 1,
	'January' : 1,
	'february' : 2,
	'February' : 2,
	'march' : 3,
	'March' : 3,
	'april' : 4,
	'April' : 4,
	'may' : 5,
	'May' : 5,
	'june' : 6,
	'June' : 6,
	'july' : 7,
	'July' : 7,
	'august' : 8,
	'August' : 8,
	'september' : 9,
	'September' : 9,
	'october' : 10,
	'OCtober' : 10,
	'november' : 11,
	'November' : 11,
	'december' : 12,
	'December' : 12,
	}
	return switcher.get(argument,"nothing")

def placementToNumber(argument):
	switcher = {
	'first' : 1,
	'First' : 1,
	'second' : 2,
	'Second' : 2,
	'third' : 3,
	'Third' : 3,
	'fourth' : 4,
	'Fourth' : 4,
	'fifth' : 5,
	'Fifth' : 5,
	'sixth' : 6,
	'Sixth' : 6,
	'seventh' : 7,
	'Seventh' : 7,
	'eigth' : 8,
	'Eigth' : 8,
	'ninth' : 9,
	'Ninth' : 9,
	'tenth' : 10,
	'Tenth' : 10,
	'eleventh' : 11,
	'Eleventh' : 11,
	'twelth' : 12,
	'Twelth' : 12,
	'thirteenth' : 13,
	'Thirteenth' : 13,
	'fourteenth' : 14,
	'Fourteenth' : 14,
	'fifteenth' : 15,
	'Fifteenth' : 15,
	'sixteenth' : 16,
	'Sixteenth' : 16,
	'seventeenth' : 17,
	'Seventeenth' : 17,
	'eighteenth' : 18,
	'Eighteenth' : 18,
	'nineteenth' : 19,
	'Nineteenth' : 19,
	'twenty' : 20,
	'Twenty' : 20,
	'thirty' : 30,
	'Thirty' : 30,
	}
	return switcher.get(argument,"nothing")

@my_bot.command(brief="Tell the bot your birthday",help="Give the bot your birthday and it will greet you on your birthday, Do not include year")
async def setBirthday(ctx, *args):
	global BirthDict
	await ctx.message.delete()
	monthSet = False
	daySet = False
	member = ctx.message.author
	ident = member.id
	month = -1
	day = -1
	for arg in args:
		res = monthToNumber(arg)
		if res != "nothing":
			month = res
			monthSet = True
		else:
			if '/' in arg:
				parts = arg.split('/')
				if parts[0].isdigit():
					day = int(parts[0])
					daySet = True
				if parts[1].isdigit():
					month = int(parts[1])
			elif ':' in arg:
				parts = arg.split(':')
				if parts[0].isdigit():
					day = int(parts[0])
					daySet = True
				if parts[1].isdigit():
					month = int(parts[1])
			elif ('th' in arg or 'st' in arg or 'nd' in arg or 'rd' in arg) and len(arg) < 5:
				if arg is args[0] or monthSet:
					if arg[:2].isdigit():
						day = int(arg[:2])
						daySet = True
				else:
					if arg[:2].isdigit():
						month = int(arg[:2])
			elif 'ty' in arg:
				partA = arg[:arg.find('ty') + 2]
				total = placementToNumber(partA)
				partB = arg[arg.find('ty') + 2:]
				if(len(partB > 1)):
					total += placementToNumber(partB)
				day = total
				daySet = True
			else:
				if not daySet:
					if arg.isdigit():
						day = int(arg)
						daySet = True
					else:	
						temp = placementToNumber(arg)
						if temp != "nothing":
							day = temp
							daySet = True
				else:
					if arg.isdigit():
						month = int(arg)
					else:
						temp = placementToNumber(arg)
						if temp != "nothing":
							month = temp
	if day == -1 or month == -1:
		await my_bot.get_channel(ServerChan).send("Please specify birthday in the correct format")
	else:
		BirthDict[ident] = (day, month)
		file = open("££birthday.txt", 'w')
		writtenText = ""
		done = False;
		for key, value in BirthDict.items():
			day ,month = value
			writtenText = writtenText + "(" + str(key) + ":" + str(day) + ":" + str(month) + "),"
		file.write(writtenText)
		file.close()
		await my_bot.get_channel(ServerChan).send("Birthday set")


"""

Meme Squre

"""
async def generateMeme(memeable):
	global ServerChan
	memeable = memeable.lower()
	bigMeme = ''
	for i in range(len(memeable)):
		meme = ''
		for j in memeable:
			meme = meme + await getChar(j)
		bigMeme = bigMeme +  await charShift(meme, i) + "\n"
	await my_bot.get_channel(ServerChan).send(bigMeme)
	

async def getChar(char):
	ascii = ord(char)
	uniDec = (ascii + 65216)
	uniChar = chr(uniDec)
	return uniChar

async def charShift(inStr, shiftBy):
	newStr = ''
	for i in range(shiftBy):
		newStr = ''
		for j in range((len(inStr)-1)):
			newStr = newStr + inStr[j+1]
		newStr = newStr + inStr[0]
		inStr = newStr
	return inStr
"""

MATHS

"""

async def linearRegress(points,iterations,staged,maxx,minx,w0,w1):
	offset = 1;
	##f(minx < 0):
	#	if(maxx > (minx*-1) and maxx > 1):
	#		offset = maxx
	#	elif minx < -1:
	#		offset = minx
	#else:
	#	if(maxx > minx and maxx > 1):
	#		offset = maxx
	#	elif minx < -1:
	#		offset = minx
	delta = 0.01
	x = np.arange(-1.5, 1.5, delta)
	y = np.arange(-1.5, 1.5, delta)
	X, Y = np.meshgrid(x, y)
	beta = (1/0.3)**2
	forPlot = []
	Sn = None
	Mn = None
	minY = -1
	maxY = 1
	global ServerChan
	for point in range(0,iterations):
		sample = np.random.multivariate_normal([0,0],w1 * np.identity(2))
		sample = np.reshape(sample,(-1,1))
		sample = np.transpose(sample)
		xSamp = [(points[point])/offset,1]
		print(w0)
		print(w1)
		Yi = float(w0)*xSamp[0] + float(w1)
		if Yi < minY:
			minY = Yi
		elif Yi > maxY:
			maxY = Yi
		#print(points[point]/offset)
		forPlot.append((points[point]/offset,Yi))
		xSamp = np.reshape(xSamp,(-1,1))
		res = np.dot(sample, xSamp)
		xSamp = xSamp.T
		Likelihood = mlab.normpdf(X,res,beta)
		if point == 0:
			Sn = np.linalg.inv(np.linalg.inv(w1*np.identity(2)) + beta*xSamp.T.dot(xSamp))
			Mn = Sn.dot(np.linalg.inv(w1*np.identity(2)).dot([0,0]) + beta*xSamp.T.dot([Yi]))
		else:
			Sn = np.linalg.inv(np.linalg.inv([Sn[0,0],Sn[1,1]]*np.identity(2)) + beta*xSamp.T.dot(xSamp))
			Mn = Sn.dot(np.linalg.inv([Sn[0,0],Sn[1,1]]*np.identity(2)).dot(Mn) + beta*xSamp.T.dot([Yi]))

		Posterior = (mlab.bivariate_normal(X,Y,Sn[0,0],Sn[1,1],Mn[0],Mn[1]))
		if staged is True and point is not iterations:
			plt.figure()
			plt.axis([-1,1,minY-1,maxY+1])
			for j in range(0,point):
				newW = np.random.multivariate_normal(Mn,Sn)
				sampY = [newW[0]*(-1) + newW[1],newW[0]*(1) + newW[1]]
				plt.plot([minx-1,1],[sampY[0],sampY[1]])
			for m,n in (forPlot):
				#print("goddamn")
				plt.scatter(m,n)
				#print(m)
				#print(n)
			plt.savefig('££LR' + str(point) + '.png')
			location = '££LR' + str(point) + '.png'
			await my_bot.get_channel(ServerChan).send(file=discord.File(location))
		elif point is iterations-1:
			newW = np.random.multivariate_normal(Mn,Sn)
			sampY = [newW[0]*(-1) + newW[1],newW[0]*(1) + newW[1]]
			plt.figure()
			plt.axis([minx-1,maxx+1,minY-1,maxY+1])
			plt.plot([minx-1,maxx+1],[sampY[0],sampY[1]])
			for m,n in (forPlot):
				#print(m)
				#print(n)
				#print("goddamn")
				plt.scatter(m,n)
			plt.savefig('££LR' + str(point) + '.png')
			location = '££LR' + str(point) + '.png'
			await my_bot.get_channel(ServerChan).send(file=discord.File(location))
	

	
@my_bot.command()
async def LR(ctx,*args):
	minx = -1
	maxx = 1
	switch = False
	pointArray = []
	count = 0;
	w0 = -1.3
	w1 = 0.5
	for arg in args:
		argu = str(arg)
		print("<" + arg + ">")
		if argu == 'True' or argu == 'true':
			print("Goddamn")
			switch = True
		elif argu == 'False' or argu == 'false':
			print("Goddamn")
			switch = False
		elif argu[0] is '<' and argu[-1:] is '>':
			argu = argu[1:]
			argu = argu[:-1]
			w0 = argu
		elif argu[0] is '>' and argu[-1:] is '<':
			argu = argu[1:]
			argu = argu[:-1]
			w1 = float(argu)
		else:
			try:
				print("number")
				arg = float(arg)
				if arg > maxx:
					maxx = arg
				elif arg < minx:
					minx = arg
				count = count + 1
				pointArray.append(arg)
			except:
				global ServerChan
				await my_bot.get_channel(ServerChan).send("Did you mean True or False?")
	await linearRegress(np.array(pointArray),count,switch,maxx,minx,w0,w1)



			


"""

RXN AND SOUNDS AND Custom Pubg Rules 

"""

@my_bot.command(help='!yots post a yots image\n Can take anger, awe, damn, ehh, hmph, knock, meme, toss, chef, fear, what as args\n',brief='Post some yots')
async def yots(ctx,*args):
	await ctx.message.delete()
	global ServerChan
	for arg in args:
		argu = str(arg)
		if argu == 'anger':
			await my_bot.get_channel(ServerChan).send(file=discord.File('img/££yotsanger.jpg'))
			break
		if argu == 'awe':
			await my_bot.get_channel(ServerChan).send(file=discord.File('img/££yotsawe.jpg'))
			break
		if argu == 'damn':
			await my_bot.get_channel(ServerChan).send(file=discord.File('img/££yotsdamn.jpg'))
			break
		if argu == 'ehh':
			await my_bot.get_channel(ServerChan).send(file=discord.File('img/££yotsehhh.jpg'))
			break
		if argu == 'hmph':
			await my_bot.get_channel(ServerChan).send(file=discord.File('img/££yotshmph.jpg'))
			break
		if argu == 'knock':
			await my_bot.get_channel(ServerChan).send(file=discord.File('img/££yotsknock.jpg'))
			break
		if argu == 'meme':
			await my_bot.get_channel(ServerChan).send(file=discord.File('img/££yotsmeme.jpg'))
			break
		if argu == 'toss':
			await my_bot.get_channel(ServerChan).send(file=discord.File('img/££yotstoss.jpg'))
			break
		if argu == 'what':
			await my_bot.get_channel(ServerChan).send(file=discord.File('img/££yotswhat.jpg'))
			break
		if argu == 'chef':
			await my_bot.get_channel(ServerChan).send(file=discord.File('img/££yotschef.png'))
			break
		if argu == 'fear':
			await my_bot.get_channel(ServerChan).send(file=discord.File('img/££yotsfear.png'))
			break


@my_bot.command(help='Like rxn but specific, provide image name',brief='Get that image you want')
async def spec(ctx,arg):
	await ctx.message.delete()
	global ServerChan
	argu = str(arg)
	try:
		await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + argu + '.png'))
	except:
		try:
			await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + argu + '.jpg'))
		except:
			try:
				await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + argu + '.gif'))
			except:
				#print(argu + " " + str(index))
				await my_bot.get_channel(ServerChan).send("No such pic")


@my_bot.command(help='See assist rxn for a list of categories',brief='React with your favourite images')
async def rxn(ctx,*args):
	await ctx.message.delete()
	global ServerChan
	for arg in args:
		argu = str(arg)
		if(argu == 'rng'):
			result = random.choice(list(rxDict))
			print(result)
			index = rxDict[result]
			await my_bot.get_channel(ServerChan).send(str(result) + str(index))
			if (index is not 1):
				try:
					await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + result + str(index) + '.png'))
				except:
					try:
						await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + result + str(index) + '.jpg'))
					except:
						try:
							await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + result + str(index) + '.gif'))
						except:
							#print(argu + " " + str(index))
							await my_bot.get_channel(ServerChan).send("No such pic")
			else:
				try:
					await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + result  + '1.png'))
				except:
					try:
						await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + result  + '1.jpg'))
					except:
						try:
							await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + result + '1.gif'))
						except:
							#print(argu + " " + str(index))
							await my_bot.get_channel(ServerChan).send("No such pic")
		else:
			if argu in rxDict:
				if(rxDict[argu] is not 1):
					index = random.randint(1,rxDict[argu])
					print(index)
					try:
						await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + argu + str(index) + '.png'))
					except:
						try:
							await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + argu + str(index) + '.jpg'))
						except:
							try:
								await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + argu + str(index) + '.gif'))
							except:
								#print(argu + " " + str(index))
								await my_bot.get_channel(ServerChan).send("No such pic")	
				else:
					print("no rand")
					try:
						await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + argu + '.png'))
					except:
						try:
							await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + argu + '.jpg'))
						except:
							try:
								await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + argu + '.gif'))
							except:
								try:
									await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + argu + '1.png'))
								except:
									try:
										await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + argu + '1.jpg'))
									except:
										try:
											await my_bot.get_channel(ServerChan).send(file=discord.File('drive/reactions/££' + argu + '1.gif'))
										except:
											await my_bot.get_channel(ServerChan).send("No such pic")	


@my_bot.command(help='Get a sound played by the bot, specify the filename',brief='Play your favourite sounds')
async def sound(ctx,*args):
	await ctx.message.delete()
	for arg in args:
		argu = str(arg)
		if argu in soundDict:
			eventQueue.put('sounds' + argu)

@my_bot.command(help='Get a pubg custom gamemode',brief='Fun gameplay')
async def houseRules(ctx):
	await ctx.message.delete()
	if not HouseRulesDict:
		print("No Dict")
	else:
		file, count = random.choice(list(HouseRulesDict.items()))
		#print(file)
		eventQueue.put('houseX' + file)
		print("Time for a house rule")

@my_bot.command(help='Get a pubg custom gamemode, with explanation',brief='Fun gameplay')
async def houseRulesVerbose(ctx):
	await ctx.message.delete()
	if not HouseRulesDict:
		print("No Dict")
	else:
		file, count = random.choice(list(HouseRulesDict.items()))
		#print(file)
		eventQueue.put('houseV' + file)
		print("Time for a house rule verbose")


"""

THEMES AND GOODBYES

"""

@my_bot.command()
async def theme(ctx,*args):
	argu = ''
	vol_spec = 0
	for arg in args:
		arg = str(arg)
		if arg[0] is '<' and arg[-1:] is '>':
			vol = arg[1:-1]
			vol_spec = 1
		else:	
			if argu is '':
				argu = argu + arg
			else:
				argu = argu + '+' + arg
	if not vol_spec:
		vol = 50
	user = ctx.message.author
	global themeDict
	if(len(ctx.message.attachments) != 0):
		filename = ctx.message.attachments[0].filename
		name, extension = filename.split('.')
		oldVol = 50
		if str(user) in themeDict:
			oldVol = vol
		if extension == 'mp3':
			print('mp3 theme')
			os.remove('./themes/££' + str(user.id) + str(oldVol) + '.' + extension)
			await ctx.message.attachments[0].save('./themes/££' + str(user.id) + str(vol) + '.' + extension)
			await ctx.message.delete()
		else:
			await user.send("Wrong file format")
			return		
	else:
		print('download theme')
		await ctx.message.delete()
		await downloadTheme(argu,str(user.id) + str(vol))
	if str(user) in themeDict:
		themeDict[str(user.id)] = vol
	else:
		themeDict[str(user.id)] = vol
	await user.send("Theme ready")

@my_bot.command()
async def setTheme(ctx,*args):
	await ctx.message.delete()
	global ServerChan
	targetID = None
	argu = ''
	vol_spec = 0
	found = False
	user = ctx.message.author
	if user in my_bot.get_guild(ServerChan).roles[4].members:
		print("theyre an admin")
		naming = False
		for arg in args:
			arg = str(arg)
			if arg[0] is '<' and arg[-1:] is '>':
				vol = arg[1:-1]
				vol_spec = 1
			elif arg[0] is '(' and arg[-1:] is ')':
				targetName = arg[1:-1]
				print(targetName)
				for member in my_bot.get_guild(ServerChan).members:
					print(member.display_name)
					if member.display_name == targetName:
						targetID = member.id
						found = True
			else:	
				if argu is '':
					argu = argu + arg
				else:
					argu = argu + '+' + arg
		if(targetID == None):
			await user.send("No target provided")
		elif(found == False):
			await user.send("Not a target")
		else:	
			if not vol_spec:
				vol = 50
			global themeDict
			await downloadTheme(argu,str(targetID) + str(vol))
			if str(targetID) in themeDict:
				pass
			else:
				themeDict[str(targetID)] = vol
			await user.send("Theme ready")
	else:
		await user.send("You do not have permission to use this command")



async def downloadTheme(argu,id):
	linklist = await ytLokupGrab(argu,False)
	if linklist is None:  # Checks for populated results
		pass
	else:
		songFile = linklist[0]
		print(str(songFile))
		downloadSong("themes",id,songFile)


def makeSchlorp(name):
	scNum = random.randint(1, 2)
	greet = random.randint(1, 3)
	name = name.replace("'",'')
	createTTS(name, 'schlorp')
	eventQueue.put("schlorp" + str(greet) + str(scNum) + str(name.replace(' ','')))

@my_bot.command(brief="be mean")
async def hate(ctx, *args):
	if ctx.message.mentions is not []:
		for member in ctx.message.mentions:
			print(member.display_name)
			await makeHate(member.display_name)

async def makeHate(name):
	name = name.replace("'",'')
	createTTS(name, 'hate')
	eventQueue.put("hate" + name.replace(' ',''))


"""

GAMES

"""


@my_bot.command(brief="Link a league account to your name",help="links a summoner id to your discord member name")
async def setSummoner(ctx, *args):
	global RiotDict
	#await ctx.message.delete()
	region = 'euw1'
	for arg in args:
		if arg[0] is '<' and arg[-1:] is '>':
			region = arg[1:-1]
		else:
			datas = getSummonerID(region,arg)
			RiotDict[datas['id']] = (str(ctx.message.author.id), region)
			writeOutSummonerFile()
			print(RiotDict)

def loadSummonerFile():
	global RiotDict
	file = open("££gameLinks.txt",'r')
	stringfile = file.read().replace('\n','')
	stringfile = stringfile.replace('(','')
	stringfile = stringfile.replace(')','')
	membersummoners = [i for i in stringfile.split(',')]
	for match in membersummoners:
		summoner, member, region = match.split(':')
		RiotDict[summoner] = (member, region)


@my_bot.command()
async def apex(ctx,arg):
	await ctx.message.delete()
	global ServerChan
	player = arg
	print(apx_url + player)
	data = requests.get(apx_url + player)
	data = json.loads(data.content.decode('utf-8'))
	print(data)
	aid = data['results'][0]['aid']
	stats = requests.get(apx_url_tot + aid)
	stats = json.loads(stats.content.decode('utf-8'))
	print(stats)



@my_bot.command()
async def pubg(ctx,*args):
	await ctx.message.delete()
	global ServerChan
#    Name: xxxxx
#KD : xxx  Win ratio: xx
#Rounds Played : xxx Top ten ratio:xx
#Wins : xxxx Losses : xxxx
#Rating: xx Best Rating : xx
#Avg dmag: xx Move Dist pg: xx
#Revives pg : xx Time survived pg : xx
#Kills: Headshot kills: Headhsot kill rat:xx
#Assists: Suicides: Team kills:
#dist walk: dist ride: 
#longest kill : xx
	inst = ''
	player = ''
	mode = ''
	for arg in args:
		arg = str(arg)
		if arg == 'skill' or arg == 'stats':
			inst = arg
		elif arg == 'solo' or arg == 'duo' or arg == 'squad':
			mode = arg
		else:
			player = arg

	if inst == 'skill':
		try:
			#peep = steamapi.user.SteamUser(userurl=player)
			#print(peep)
			peepNum = peep._id
			#print(peepNum)
			peep = api.player_s(peepNum)
			peep = api.player_skill(peep['Nickname'], game_mode=mode)
			await my_bot.get_channel(ServerChan).send(mode + " pubg skill rating for " + player + ": " + peep['eu'])
		except:
			await my_bot.get_channel(ServerChan).send("No skill rating for that player/mode")
	elif inst == 'stats':
		try:
			#peep = steamapi.user.SteamUser(userurl=player)
			print(peep)
			peepNum = int(peep._id)
			print(peepNum)
			#peep = api.player_s(peepNum)
			#print(peep)
			#print(api.players.get_player(peep),"78c04087-08e7-4666-985e-6bfa6efee086")
			peepums = api.player("Shasocais")#_mode_stats(peep["Nickname"],game_mode=mode,game_region="eu")
			print(peepums)
		except:
			peepums = []
		if not peepums == []:
			for entry in peepums:
				if entry['Season'] == current_season:
					data = entry['Stats']
			if data is not None:
				message = "Name : " + peep['SteamName'] + "\nKD : " + data[0]['displayValue'] + "  Win Ratio : " + data[1]['displayValue'] +"\n"
				message = message + "Wins : " + data[4]['displayValue'] + "  Losses : " + data[8]['displayValue'] +"\n"
				message = message + "Rounds Played : " + data[3]['displayValue'] + "  Top ten ratio : " + data[7]['displayValue'] +"\n"
				message = message + "Rating : " + data[9]['displayValue'] + "  Best Rating : " + data[10]['displayValue'] + "  " + str(data[9]['percentile']) +"th percentile" + "\n"
				message = message + "Damage per game : " + data[12]['displayValue'] + "  Move distance per game : " + data[16]['displayValue'] + "\n"
				message = message + "Revives per game : " + data[17]['displayValue'] + "  Time survived per game : " +  data[20]['displayValue'] +"\n"
				message = message + "Kills : " + data[22]['displayValue'] + "  Headshot kills : " + data[26]['displayValue'] +"  Headshot kill ratio : " + data[27]['displayValue'] + "\n"
				message = message + "Assists : " + data[23]['displayValue'] + "  Suicides : " + data[24]['displayValue'] + "  Team kills : " + data[25]['displayValue'] + "\n"
				message = message + "Distance walked : " + data[40]['displayValue'] + "  Distance ridden : " + data[41]['displayValue'] + "\n"
				message = message + "Longest round : " + data[37]['displayValue'] + "  Longest kill : " + data[45]['displayValue'] + "\n"
			else:
				message = "No data for current season"
			await my_bot.get_channel(ServerChan).send(message)
		else:
			await my_bot.get_channel(ServerChan).send("No stats for that player/mode")    
	else:
		await my_bot.get_channel(ServerChan).send("Please specify a correct command")




"""

TTS

"""


@my_bot.command()
async def codes(ctx):
	await ctx.message.delete()
	global ServerChan
	await my_bot.get_channel(ServerChan).send(codespls)

#format = say text <lang>
@my_bot.command(help='!say text <language-code>\nuse !codes to get a list of codes',brief='Make the bot speak')
async def say(ctx,*args):
	await ctx.message.delete()
	argu = ''
	lang_spec = 0
	for arg in args:
		arg = str(arg)
		#print(arg[0] + " " + arg[-1:])
		if arg[0] is '<' and arg[-1:] is '>':
			if (arg[1] + arg[2]) in languages:
				lang.put(arg[1] + arg[2])
			else:
				lang.put('en-uk')
			lang_spec = 1
		else:
			if argu is '':
				argu = argu + arg
			else:
				argu = argu + ' ' + arg
	if not lang_spec:
		lang.put('en-uk')
	eventQueue.put('say')
	words.put(argu)

@my_bot.command()
async def dictate(ctx):
	global Dictate
	global DictateAns
	await ctx.message.delete()
	lang.put('en-uk')
	print(Dictate)
	if Dictate != '':
		words.put(Dictate)
		Dictate = ''
	else:
		words.put(DictateAns)
		DictateAns = ''
	eventQueue.put('say')


# Function to lookup/create tts mp3 file
async def ttsIt():
	global playbackVol
	text = words.get()
	langu = lang.get()
	#if (len(text) > 200):
	#    text = text[:200]
	langu = langu.replace("'",'')
	langu = langu.replace('"','')
	tts = gTTS(text = text,lang = langu)
	name = text.replace(" ","")
	tts.save("TTS.mp3")
	await playfile("TTS.mp3",playbackVol, False, True)

def createTTS(text, dir):
	tts = gTTS(text=text, lang='en-uk')
	tts.save(dir + "/" + text.replace(' ','') + ".mp3")
	

"""

DRIVE MANIPULATION


"""

@my_bot.command()
async def addToDrive(ctx,arg):
	#await ctx.message.delete()
	global rxDict
	global soundDict
	print(ctx.message.author)
	print(my_bot.get_guild(ServerChan).roles)#[3].members)
	if ctx.message.author not in my_bot.get_guild(ServerChan).roles[4].members:
		await my_bot.get_channel(ServerChan).send("Command limited to admins")
		return
	if arg is None:
		await my_bot.get_channel(ServerChan).send("Command requires single arg")
		return
	filename = ctx.message.attachments[0].filename
	name, extension = filename.split('.')
	cat = str(arg)
	print(name)
	print(extension)
	def check(m):
		return m.author == ctx.message.author
	if(cat in soundDict and (extension != 'png' and extension != 'jpg' and extension != 'gif') ):
		print("mp3 pls")
		if(extension == 'mp3'):
			wd = os.getcwd()
			os.chdir("drive")
			soundDict[cat] += 1
			await ctx.message.attachments[0].save('./sounds/££' + cat + str(soundDict[cat]) + '.' + extension)
			await ctx.message.delete()
			call('grive')
			call('grive')
			os.chdir(wd)
			rewriteDicts()
			await my_bot.get_channel(ServerChan).send("Sound " + cat + str(soundDict[cat]) + " created")
		else:
			await my_bot.get_channel(ServerChan).send("Sorry that file type is not available at this time")
	elif(cat in rxDict and extension != 'mp3'):	
		print('pic pls')
		print(extension)
		print(extension is 'mp3')
		if(extension == 'png' or extension == 'jpg' or extension == 'gif'):
			wd = os.getcwd()
			os.chdir("drive")
			rxDict[cat] += 1
			await ctx.message.attachments[0].save('./reactions/££' + cat + str(rxDict[cat]) + '.' + extension)
			await ctx.message.delete()
			call('grive')
			call('grive')
			os.chdir(wd)
			rewriteDicts()
			await my_bot.get_channel(ServerChan).send("Image " + cat + str(rxDict[cat]) + " created")
		else:
			await my_bot.get_channel(ServerChan).send("Sorry that file type is not available at this time")
	else:
		mention = ctx.message.author.mention
		await my_bot.get_channel(ServerChan).send(mention + " no category " + cat + ", would you like it created? y/n")
		msg = await my_bot.wait_for('message',timeout = 60.0,check=check)
		if msg.content == 'y' or msg.content == 'yes' or msg.content == 'Y' or msg.content == 'Yes':
			print(extension)
			if(extension == 'mp3'):
				wd = os.getcwd()
				os.chdir("drive")
				soundDict[cat] = 1
				await ctx.message.attachments[0].save('./sounds/££' + cat + str(soundDict[cat]) + '.' + extension)
				await ctx.message.delete()
				call('grive')
				call('grive')
				os.chdir(wd)
				rewriteDicts()
				await my_bot.get_channel(ServerChan).send("Category " + cat + " created")
			elif(extension == 'png' or extension == 'jpg' or extension == 'gif'):
				wd = os.getcwd()
				os.chdir("drive")
				rxDict[cat] = 1
				await ctx.message.attachments[0].save('./reactions/££' + cat + str(rxDict[cat]) + '.' + extension)
				await ctx.message.delete()
				call('grive')
				call('grive')
				os.chdir(wd)
				rewriteDicts()
				await my_bot.get_channel(ServerChan).send("Category " + cat + " created")
			else:
				await my_bot.get_channel(ServerChan).send("Sorry that file type is not available at this time")
		else:
			await my_bot.get_channel(ServerChan).send("No action taken")




@my_bot.command()
async def resync(ctx):
	await ctx.message.delete()
	wd = os.getcwd()
	os.chdir("drive")
	call('grive')
	call('grive')
	os.chdir(wd)
	rewriteDicts()
	await my_bot.get_channel(ServerChan).send("Resync complete")



async def swippity(filename, vol, stream):
	global ServerChan
	global ScreamChamber
	global playerDeque
	global announceDeque
	print("Swippity swooty")
	#await ctx.message.delete()
	server = my_bot.get_guild(ServerChan)
	voice = server.voice_client
	print("voice got")
	if voice is not None:
		print("voice exists")
		if (voice.is_playing() or voice.is_paused()) and announcing.empty():
			print("Free run")
			announcing.put(1)
			heldSource = voice.source
			print(heldSource)
			playerDeque.appendleft(voice.source)
			voice.source = discord.FFmpegPCMAudio(filename)
			#while voice.is_playing() or voice.is_paused():
			#	asyncio.sleep(1)
			#announcing.get()
		else:
			print("blocked")
			announceDeque.append(discord.FFmpegPCMAudio(filename))
			#while not announcing.empty():
			#	await asyncio.sleep(1)
			#announcing.put(1)
			#await playfile(filename, q, vol, strean)
	else:
		print("We empty")
		announcing.put(1)
		await playfile(filename, vol, stream, True)
		#announcing.get()



"""

PLAYER HANDLING


"""


# generic play function
async def play2(argu, voice):
	global playbackVol
	playlist = False
	recent = False
	print("song to find: " + str(argu))
	if argu[:9] == './recent/':
		print("recent song")
		linklist = 1
		playlist = False
		songFile = argu
	elif(argu[:2] == './'):
		print('in list')
		linklist = 1
		songFile = argu
		playlist = True
	else:
		print("looking up")
		linklist = 1
		songFile = argu
		playlist = False
		recent = True
	if linklist is None:  # Checks for populated results
		pass
	else:
		try:
			if not playlist:
				if recent == False:
					print("Playing local mp3")
					await playfile(songFile, playbackVol, False, False)
					
					success = False
				else:
					print("Streaming for first time")
					await playfile(songFile, playbackVol, True, False)
					success = False
			else:
				print('now playing')
				await playfile(songFile + '.mp3',playbackVol, False, False)
				success = False
		except:
			success = False


def afterCheck(e):
	global playerDeque
	global announceDeque
	global ServerChan
	global ScreamChamber
	print("AfterCheck", e)
	server = my_bot.get_guild(ServerChan)
	voice = None
	if server.voice_client is not None:
		voice = server.voice_client
	else:
		voice = my_bot.get_channel(ScreamChamber).connect()
	#voice = server.voice_client
	print(len(playerDeque))
	print(voice)
	if len(announceDeque) is not 0:
		check = announceDeque.popleft()
		if check is not None:
			voice.play(check, after=lambda e: afterCheck(e))
		else:
			print("Done")
	elif len(playerDeque) is not 0:
		if not announcing.empty():
			x = announcing.get()
		check = playerDeque.popleft()
		if check is not None:
			voice.play(check, after=lambda e: afterCheck(e))
		else:
			print("Done")
	else:
		print("Empty")


# Mp3 player
async def playfile(args, volume, streamed, announced):
	global playerDeque
	global announceDeque
	if streamed:
		subOpts = {}
		with youtube_dl.YoutubeDL(subOpts) as ydl:
			song_info = ydl.extract_info(args, download=False)
		args = song_info['formats'][0]['url']		
	source = discord.FFmpegPCMAudio(args)
	source = discord.PCMVolumeTransformer(source)
	volume = int(volume)/100
	source.volume = volume
	if announced:
		announceDeque.append(source)
	else:
		playerDeque.append(source)


"""

PLAYER COMMANDS

"""

@my_bot.command(help='!play youtube video keywords\nyou can then use pause resume and skip to control play',brief='Have the bot play your choice of vids')
async def play(ctx,*args):
	await ctx.message.delete()
	argu = ''
	for arg in args:
		arg = str(arg)
		if argu is '':
			argu = argu + arg
		else:
			argu = argu + '+' + arg
	inst = ["play", argu]
	instQueue.put(inst)


@my_bot.command(help='!loop repeat plays selection until !skip is used\n',brief='loop a video')
async def loop(ctx,*args):
	await ctx.message.delete()
	argu = ''
	for arg in args:
		arg = str(arg)
		if argu is '':
			argu = argu + arg
		else:
			argu = argu + '+' + arg
	inst = ["loop", argu]
	instQueue.put(inst)


@my_bot.command()
async def replay(ctx):
	await ctx.message.delete()
	argu = recentSongList.getRecent()
	argu = argu.replace('#', '?')
	inst = ["play", argu]
	instQueue.put(inst)

@my_bot.command()
async def resume(ctx):
	await ctx.message.delete()
	global ServerChan
	my_bot.get_guild(ServerChan).voice_client.resume()


@my_bot.command()
async def skip(ctx):
	await ctx.message.delete()
	global ServerChan
	my_bot.get_guild(ServerChan).voice_client.stop()

@my_bot.command()
async def volume(ctx,arg):
	await ctx.message.delete()
	global ServerChan
	global playbackVol
	volume = int(arg)/100
	playbackVol = volume
	my_bot.get_guild(ServerChan).voice_client.source.volume = volume


@my_bot.command()
async def pause(ctx):
	await ctx.message.delete()
	global ServerChan
	my_bot.get_guild(ServerChan).voice_client.pause()


"""

SONG ACQUISITION

"""

# handles looking up youtube search results
async def ytLokupGrab(arg,title):
	string = 'https://www.youtube.com/results?search_query='
	string = string + arg
	browser = webdriver.Chrome()#PhantomJS()#Firefox()
	try:
		if arg[:2] == "/w" and not title:
			return ["https://www.youtube.com" + arg]
		else:
			if arg[:2] == "/w":
				string = "https://www.youtube.com" + arg
				print(string)
				print("Browser navigating")
				browser.get(string)
				print("Browser got")
				await asyncio.sleep(2)
				linklist = browser.find_elements_by_class_name('ytd-video-primary-info-renderer')
				count = 0
				auglinklist = ''
				for link in linklist:
					print(link.text)
					if count > 4:
						auglinklist = link.text
						break
					count = count + 1
				print(auglinklist)
				return [[("https://www.youtube.com" + arg), (auglinklist)]]
			print("Browser navigating to site")
			browser.get(string)
			print("Browser got")#
			linklist = browser.find_elements_by_id('video-title')
			if(title):
				auglinklist = [(link.get_attribute('href'),link.get_attribute('title')) for link in linklist]
			else:	
				auglinklist = [(link.get_attribute('href')) for link in linklist]
			print(auglinklist)
			return auglinklist
	except:
		pass
	browser.quit()

# saves recent songs
async def grabSong(url, name):
	name = name.replace("/", '')
	ydl_opts = {
		'outtmpl': name + '.mp3',
		#'format': 'bestaudio/best',
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		}],
		'outtmpl':'./recent/' + name + '.%(ext)s'
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])


def downloadSong(dir,songname,songUrl):
	songname = songname.replace("/", '')
	ydl_optsCust = {
	#'format': 'bestaudio/best',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
	'noplaylist': True,
	'outtmpl':'./' + dir + '/££' + songname + '.%(ext)s',
	'logger': MyLogger(),
	'progress_hooks': [my_hook],
	}
	#print(songname+ '\n')
	#print(songUrl + '\n')
	with youtube_dl.YoutubeDL(ydl_optsCust) as ydl:
		ydl.download([songUrl])



@my_bot.command(help='!findAlt youtube video keywords\nreturns 3 videos',brief='Like find but three')
async def findAlt(ctx,*args):
	await ctx.message.delete()
	argu = ''
	for arg in args:
		arg = str(arg)
		if argu is '':
			argu = argu + arg
		else:
			argu = argu + '+' + arg
	inst = ["findAlt", argu]
	instQueue.put(inst)





@my_bot.command(help='!find youtube video by keywords',brief='youtube keyword search')
async def find(ctx,*args):
	await ctx.message.delete()
	argu = ''
	for arg in args:
		arg = str(arg)
		if argu is '':
			argu = argu + arg
		else:
			argu = argu + '+' + arg
	inst = ["findx", argu]
	instQueue.put(inst)




async def findAlt2(argu):
	global ServerChan
	linklist = await ytLokupGrab(argu,False)
	# print('listing')
	if linklist is None:
		await my_bot.get_channel(ServerChan).send('No results')
	else:
		for x in range(0, 3):
			#print('messaging')
			await my_bot.get_channel(ServerChan).send(
									  linklist[x])


async def find2(argu):
	global ServerChan
	linklist = await ytLokupGrab(argu,False)
	if linklist is None:
		await my_bot.get_channel(ServerChan).send('No results')
	else:
		await my_bot.get_channel(ServerChan).send(
								  linklist[0])


"""

SITE SCRAPING


"""

async def get_site_content(url):
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as resp:
			text = await resp.read()

	return BeautifulSoup(text.decode('utf-8'), 'html5lib')


@my_bot.command()
async def riddleMePiss(ctx,*args):
	await ctx.message.delete()
	global ServerChan
	await riddleScrape()

@my_bot.command()
async def Christ(ctx, *args):
	await ctx.message.delete()
	global ServerChan
	await my_bot.get_channel(ServerChan).send(file=discord.File('££As.jpg'))


async def riddleScrape():
	global ServerChan
	global Dictate
	global DictateAns
	browser = webdriver.Chrome()
	string = "http://www.goodriddlesnow.com/riddles/random"
	await my_bot.get_channel(ServerChan).send("Acquiring riddle")
	browser.get(string)
	button = browser.find_element_by_class_name("riddle-answer-btn")
	button.click()
	Question = browser.find_element_by_class_name('riddle-question')
	#print(Question.find_element_by_xpath("*").text)
	imgkit.from_string(Question.get_attribute('innerHTML'),'££Qs.jpg')
	Answer = browser.find_element_by_class_name('riddle-answer')
	outlet = Question.get_attribute('innerHTML')
	#outlet = outlet.replace("[",'')
	#outlet = outlet.replace("]",'')
	#outlet = outlet.replace("'",'')
	#outlet = outlet.replace('"','')
	#outlet = outlet.replace("<br>",'')
	outlet = outlet.replace("<p>",'')
	outlet = outlet.replace("</p>",'')
	outlet = outlet.replace("<strong>",'')
	outlet = outlet.replace("</strong>",'')
	#outlet = outlet.replace("\\n",'')
	#outlet = outlet.strip()
	#outlet = re.sub("<.+?<","",outlet)
	#outlet = outlet.replace("/a>",'')
	Dictate = outlet
	print(Dictate)
	outlet = Answer.find_elements_by_xpath("*")[1].get_attribute('innerHTML')
	outlet = outlet.replace("<p>",'')
	outlet = outlet.replace("</p>",'')
	outlet = outlet.replace("<strong>",'')
	outlet = outlet.replace("</strong>",'')
	DictateAns = outlet
	imgkit.from_string(Answer.find_elements_by_xpath("*")[1].get_attribute('innerHTML'),'££As.jpg')
	await swippity('drive/sounds/££piss1.mp3',playbackVol, False)
	await my_bot.get_channel(ServerChan).send(file=discord.File('££Qs.jpg'))


@my_bot.command()
async def stackScrape(ctx,*args):
	await ctx.message.delete()
	global ServerChan
	argu = ''
	for arg in args:
		arg = str(arg)
		if argu is '':
			argu = argu + arg
		else:
			argu = argu + '+' + arg
	if argu == '':
		await my_bot.get_channel(ServerChan).send("Please supply an argument")
	else:
		await stackOverflowScrape(argu)

# handles looking up youtube search results
async def stackOverflowScrape(arg):
	global ServerChan
	browser = webdriver.Chrome()#PhantomJS()#Firefox()
	string = 'https://stackexchange.com/search?q='
	arg = html_parser.unescape(arg)
	string = string + arg
	browser.get(string)
	listEl = browser.find_element_by_xpath("//a[contains(@class, 'gs-title')]").get_attribute('href')
	try:
		soup = await get_site_content(listEl)
		answer = soup('div',{'class':'answer'})
		html = answer[0].div.contents
		stringlet = str(html[3].contents[1])
		imgkit.from_string(stringlet,'out.jpg')
		await my_bot.get_channel(ServerChan).send(file=discord.File('out.jpg'))
	except:
		await my_bot.get_channel(ServerChan).send("No such stack exchange result")
	browser.quit()

@my_bot.command()
async def yahooScrape(ctx,*args):
	await ctx.message.delete()
	global ServerChan
	argu = ''
	for arg in args:
		arg = str(arg)
		if argu is '':
			argu = argu + arg
		else:
			argu = argu + '+' + arg
	if argu == '':
		await my_bot.get_channel(ServerChan).send("Please supply an argument")		
	else:
		await answersScrape(argu)

async def answersScrape(arg):
	global ServerChan
	browser = webdriver.Chrome()#PhantomJS()#Firefox()
	string = "https://uk.answers.search.yahoo.com/search?fr=uh3_answers_vert_gs&type=2button&p="
	arg = html_parser.unescape(arg)
	string = string + arg
	browser.get(string)
	await asyncio.sleep(3)
	global Dictate
	try:
		print("Hot Damn")
		print(string)
		listEl = browser.find_elements_by_xpath("//a[contains(@class, 'lh-17')]")#.get_attribute('href')
		print(listEl)
		index = random.randint(1,len(listEl) - 1)
		listEl = listEl[index].get_attribute('href')
		print(listEl)
		print("Found page")
		soup = await get_site_content(listEl)
		header = soup('h1',{'class':'Fz-24'})
		question2 = soup('span',{'class':'ya-q-full-text'})
		question = soup('span',{'class':'ya-q-text'})
		answer = soup('span',{'class':'ya-ba-title'})
		size = len(answer)
		answer = answer[0].parent.contents[5]
		headerString = str(header[0])
		outletH = str(header[0].contents) 
		stringlet = str(question[0])
		stringlet2 = str(question2[0])
		stringlet3 = str(answer)
		if stringlet2 == stringlet3:
			stringlet2 = stringlet
			outletQ = str(question[0].contents)
		else:
			outletQ = str(question2[0].contents)
		outletA = str(answer.contents) 
		outlet = '' + outletH + outletQ + outletA
		result = "Question: <br> <br>" + headerString + "<br>" + stringlet2 + "<br><br> Answer: <br><br>" + stringlet3
		outlet = outlet.replace("[",'')
		outlet = outlet.replace("]",'')
		outlet = outlet.replace("'",'')
		outlet = outlet.replace('"','')
		outlet = outlet.replace("<br>",'')
		outlet = outlet.replace("<br/>",'')
		outlet = outlet.replace("\\n",'')
		outlet = outlet.strip()
		success = True
		while(success):
			temp = outlet
			outlet = re.sub("<.+?<","",outlet)
			if(outlet == temp):
				success = False
		outlet = outlet.replace("/a>",'')
		Dictate = outlet
		imgkit.from_string(result,'out2.jpg')
		await my_bot.get_channel(ServerChan).send(file=discord.File('out2.jpg'))
	except:
		await my_bot.get_channel(ServerChan).send("No such yahoo answers result")
	browser.quit()

@my_bot.command()
async def How(ctx):
	await ctx.message.delete()
	await wikiScrape() 

async def wikiScrape():
	global ServerChan
	browser = webdriver.Chrome()#PhantomJS()#Firefox()
	try:
		string = "https://www.wikihow.com/Special:Randomizer"
		browser.get(string)
		print("navigated")
		listEl = browser.find_elements_by_class_name("whcdn")
		index = random.randint(0,len(listEl) - 1)
		html = listEl[index].get_attribute('data-src')
		urllib.request.urlretrieve(html, "How.jpg")
		print("image got")
		await my_bot.get_channel(ServerChan).send(file=discord.File('How.jpg'))
	except:
		await my_bot.get_channel(ServerChan).send("Whoops, something went wrong")
	browser.quit()		


"""


DICT REWRITES AND FILE CHANGES


"""

def rewriteDicts():
	global soundDict
	global rxDict
	rxDict.clear()
	soundDict.clear()
	HouseRulesDict.clear()
	transtable = dict.fromkeys(map(ord, '£1234567890'), None)
	for filename in os.listdir('./drive/reactions/'):
		query = os.path.splitext("./drive/reactions/" + filename)[0]
		query = str(query)
		query = query[18:]
		query = query.translate(transtable)
		#print(query)
		if query in rxDict:
			rxDict[query] += 1
		else:	
			rxDict[query] = 1
	for filename in os.listdir('./drive/sounds/'):
		query = os.path.splitext("./drive/sounds/" + filename)[0]
		query = str(query)
		query = query[15:]
		query = query.translate(transtable)
		#print(query)
		if query in soundDict:
			soundDict[query] += 1
		else:	
			soundDict[query] = 1
	for filename in os.listdir('./drive/PUBG/Verbose'):
		query = os.path.splitext("./drive/PUBG/Verbose/" + filename)[0]
		query = str(query)
		print(query)
		query = query[21:]
		query = query.translate(transtable)
		#print(query)
		if query in HouseRulesDict:
			HouseRulesDict[query] += 1
		else:	
			HouseRulesDict[query] = 1


def writeOutSummonerFile():
	file = open("££gameLinks.txt", 'w')
	writtenText = ""
	for key, value in RiotDict.items():
		(member, region) = value
		writtenText = writtenText + "(" + str(key) + ":" + str(member) + ":" + str(region) +"),"
	file.write(writtenText)
	file.close()

"""


PROCESS SECTION


"""



@my_bot.command(help='get bot status',brief='bot status command')
async def status(ctx,*args):
	global ServerChan
	await ctx.message.delete()
	insertString = '<text x="50" y="20" font-family="Verdana" font-size="22" fill="black" > Announce</text><text x="50" y="40" font-family="Verdana" font-size="22" fill="black" > Process:</text>'
	print(insertString)
	if announceStat.empty():
		insertString = insertString + '<text x="70" y="65" font-family="Verdana" font-size="22" fill="black" > Alive</text>'
	else:
		insertString = insertString + '<text x="70" y="65" font-family="Verdana" font-size="22" fill="black" > Dead</text>'
	insertString = insertString + '<text x="50" y="90" font-family="Verdana" font-size="22" fill="black" > Player</text><text x="50" y="110" font-family="Verdana" font-size="22" fill="black" > Process:</text>'
	if playerStat.empty():
		insertString = insertString + '<text x="70" y="135" font-family="Verdana" font-size="22" fill="black" > Alive</text>'
	else:
		insertString = insertString + '<text x="70" y="135" font-family="Verdana" font-size="22" fill="black" > Dead</text>'
	insertString = insertString + '<text x="50" y="160" font-family="Verdana" font-size="22" fill="black" > Distribution</text><text x="50" y="180" font-family="Verdana" font-size="22" fill="black" > Process:</text>'
	if distStat.empty():
		insertString = insertString + '<text x="70" y="205" font-family="Verdana" font-size="22" fill="black" > Alive</text>'
	else:
		insertString = insertString + '<text x="70" y="205" font-family="Verdana" font-size="22" fill="black" > Dead</text>'
	insertString = insertString + '<text x="50" y="230" font-family="Verdana" font-size="22" fill="black" > Fileplayer</text><text x="50" y="250" font-family="Verdana" font-size="22" fill="black" > Process:</text>'
	if fileStat.empty():
		insertString = insertString + '<text x="70" y="275" font-family="Verdana" font-size="22" fill="black" > Alive</text>'
	else:
		insertString = insertString + '<text x="70" y="275" font-family="Verdana" font-size="22" fill="black" > Dead</text>'
	insertString = insertString + '<text x="50" y="300" font-family="Verdana" font-size="22" fill="black" > Greet</text><text x="50" y="320" font-family="Verdana" font-size="22" fill="black" > Process:</text>'
	if greetStat.empty():
		insertString = insertString + '<text x="70" y="345" font-family="Verdana" font-size="22" fill="black" > Alive</text>'
	else:
		insertString = insertString + '<text x="70" y="345" font-family="Verdana" font-size="22" fill="black" > Dead</text>'
	insertString = insertString + '<text x="50" y="370" font-family="Verdana" font-size="22" fill="black" > Download</text><text x="50" y="390" font-family="Verdana" font-size="22" fill="black" > Process:</text>'
	if dlStat.empty():
		insertString = insertString + '<text x="70" y="415" font-family="Verdana" font-size="22" fill="black" > Alive</text>'
	else:
		insertString = insertString + '<text x="70" y="415" font-family="Verdana" font-size="22" fill="black" > Dead</text>'
	insertString = insertString + '</g></svg>'
	f = open("££template.svg",'r')
	contents = f.read()
	f.close()
	f = open("status.svg",'w+')
	f.write(contents + insertString)
	f.close()
	os.system("inkscape -z -e status.png -w 1024 -h 1024 status.svg")
	await my_bot.get_channel(ServerChan).send(file=discord.File('status.png'))
	"""
	<text x="50" y="20" font-family="Verdana" font-size="22" fill="black" > Announce</text>
     <text x="50" y="40" font-family="Verdana" font-size="22" fill="black" > Process:</text>
     <text x="70" y="65" font-family="Verdana" font-size="22" fill="black" > Alive</text>
     <text x="50" y="90" font-family="Verdana" font-size="22" fill="black" > Player</text>
     <text x="50" y="110" font-family="Verdana" font-size="22" fill="black" > Process:</text>
     <text x="70" y="135" font-family="Verdana" font-size="22" fill="black" > Dead</text>
     <text x="50" y="160" font-family="Verdana" font-size="22" fill="black" > Player</text>
     <text x="50" y="180" font-family="Verdana" font-size="22" fill="black" > Process:</text>
     <text x="70" y="205" font-family="Verdana" font-size="22" fill="black" > Dead</text>
     <text x="50" y="230" font-family="Verdana" font-size="22" fill="black" > Player</text>
     <text x="50" y="250" font-family="Verdana" font-size="22" fill="black" > Process:</text>
     <text x="70" y="275" font-family="Verdana" font-size="22" fill="black" > Dead</text>
     <text x="50" y="300" font-family="Verdana" font-size="22" fill="black" > Player</text>
     <text x="50" y="320" font-family="Verdana" font-size="22" fill="black" > Process:</text>
     <text x="70" y="345" font-family="Verdana" font-size="22" fill="black" > Dead</text>
     <text x="50" y="370" font-family="Verdana" font-size="22" fill="black" > Player</text>
     <text x="50" y="390" font-family="Verdana" font-size="22" fill="black" > Process:</text>
     <text x="70" y="415" font-family="Verdana" font-size="22" fill="black" > Dead</text>
</g>
</svg>
	"""

async def dlConc():
	string = "https://web.archive.org/web/20120511210730im_/http://www.hlcomic.com/comics/concerned00"
	browser = webdriver.Chrome()#PhantomJS()#Firefox()	
	await asyncio.sleep(3)
	for x in range(0,206):
		if x < 10:
			stringl = string + str(x) + ".jpg"
		elif x < 100:
			stringl = string[:-1] + str(x) + '.jpg'
		else:
			stringl = string[:-2] + str(x) + '.jpg'
		#print(stringl)
		#browser.get(stringl)
		#print("navved")
		#listEl = browser.find_element_by_xpath("//img[1]")
		#print(listEl)
		#html = listEl.get_attribute('data-src')
		#print(html)
		urllib.request.urlretrieve(stringl, "concerned/" + str(x) + '.jpg')

@my_bot.command()
async def mango(ctx, *args):
	if args[0].lower() == 'list':
		instQueue.put(["mango_list",ctx])
		pass
	elif args[0].lower() == 'mine':
		instQueue.put(["mango_mine",ctx])
		pass
	elif args[0].lower() == 'add':
		instQueue.put(["mango_add",ctx])
		pass
	elif args[0].lower() == 'remove':
		instQueue.put(["mango_rem",ctx])
		pass
	elif args[0].lower() == 'next':
		instQueue.put(["mango_next",ctx])
	elif args[0].lower() == 'prev':
		instQueue.put(["mango_prev",ctx])
	elif args[0].lower() == 'request':
		terms = ''
		if len(args) < 1:
			ctx.send("Please specify search terms")
		else:	
			for arg in args[1:]:
				terms = terms + ' ' + arg
			terms = terms[1:]
			instQueue.put(["mango_req",(ctx,terms)])	
	else:
		ctx.send("Please use one of the keywords, list, mine, add or remove")


async def mango_list(ctx):
	global mangoDict
	content = ''
	for entry in mangoDict.get('me'):
		content = content + entry +'\n'
	await ctx.send(content)

async def mango_mine(ctx):
	global mangoDict
	if str(ctx.message.author) in mangoDict:
		print(ctx.message.author)
		content = ''
		print(mangoDict.get(str(ctx.message.author)))
		for entry, prog in mangoDict.get(str(ctx.message.author))[0].items():
			content = content + entry + " : chapter " + str(prog) + "\n"
		await ctx.send(content)
		def check(m):
			return m.author == ctx.message.author
		await ctx.send("Would you like to read a mango? Y/N")
		msg = await my_bot.wait_for('message',timeout = 60.0,check=check)
		if msg.content.lower() == 'y':
			await ctx.send("Which mango would you like to read?")
			msg = await my_bot.wait_for('message',timeout = 60.0,check=check)
			if msg.content in mangoDict[str(ctx.message.author)][0]:
				await ctx.send(file=discord.File('mangos/' + msg.content + '/' + str(mangoDict[str(ctx.message.author)][0][msg.content])))
				mangoDict[str(ctx.message.author)][1] = msg.content
			else:
				await ctx.send("You do not have that mango")


async def mango_add(ctx):
	global mangoDict
	def check(m):
		return m.author == ctx.message.author
	if str(ctx.message.author) not in mangoDict:
		mangoDict[ctx.message.author] = [{},'']
	await ctx.send("Which mango would you like to add to your list?")
	msg = await my_bot.wait_for('message',timeout = 60.0,check=check)
	if msg.content in mangoDict.get('me'):
		if msg.content not in mangoDict.get(ctx.message.author)[0]:
			mangoDict.get(ctx.message.author)[0][msg.content] = '1_1.jpg'
			mangoDict.get(ctx.message.author)[1] = msg.content
			await ctx.send("Mango added")
			await update_mango()
		else:
			await ctx.send("you already have that mango, you greedy mango pig")



async def mango_rem(ctx):
	pass

async def mango_request(arg):
	global mangoDict
	(ctx,terms) = arg
	print("questing")
	def check(m):
		return m.author == ctx.message.author
	mango_search = "https://www.mangareader.net"
	browser = webdriver.Chrome()#PhantomJS()#Firefox()	
	browser.get(mango_search)
	print("navved")
	await asyncio.sleep(3)
	listEl = browser.find_element_by_id("searchbox")
	listEl.send_keys(terms)
	await asyncio.sleep(2)
	try:
		title = browser.find_elements_by_class_name("ac_even")[0].find_elements_by_tag_name("div")[1].get_attribute('title')
	except:
		await ctx.send("no results found")
	#print(browser.current_url)
	await ctx.send("Is " + title + " the mango you're looking for? Y/N")
	msg = await my_bot.wait_for('message',timeout = 60.0,check=check)
	if msg.content.lower() == 'y':
		title = title.lower()
		titleb = title.replace(' ','-')
		print(title)
		if os.path.isdir("./mangos/" + titleb):
			await ctx.send("That mango is already available")
		else:
			await ctx.send("Preparing")
			wd = os.getcwd()
			os.chdir("mangos")
			title2 = titleb.replace('!','')
			title2 = title2.encode('ascii','ignore').decode('utf-8')
			call(['mkdir',title2])
			os.chdir(title2)
			print(mango_search + '/' + title2)
			browser.get(mango_search + '/' + title2)
			#try:
			await asyncio.sleep(2)
			chapNum = browser.find_element_by_class_name("chico_manga").find_element_by_xpath("..").find_element_by_tag_name("a").text
			chapNum = chapNum[len(titleb)+1:]
			mangoDict['me'][title] = mango_search + '/' + title2
			await getMango(0,chapNum,mango_search + '/' + title2)
			# for chapter in range(1,int(chapNum) + 1):
			# 	page = 1
			# 	browser.get(mango_search + '/' + title2 + '/' +str(chapter))
			# 	maxPage = int(''.join(c for c in browser.find_element_by_id('selectpage').text.split('of')[1] if c.isdigit()))
			# 	img = browser.find_element_by_id('img').get_attribute('src')
			# 	imdata = requests.get(img)
			# 	with open(str(chapter)+'_'+str(page) + '.jpg','wb') as writer:
			# 		writer.write(imdata.content)
			# 	await asyncio.sleep(1)
			# 	for page in range(2,maxPage+1):
			# 		browser.get(mango_search + '/' + title2 + '/' +str(chapter) + '/' + str(page))
			# 		img = browser.find_element_by_id('img').get_attribute('src')
			# 		imdata = requests.get(img)
			# 		with open(str(chapter)+'_'+str(page) + '.jpg','wb') as writer:
			# 			writer.write(imdata.content)
			await ctx.send("Mango loaded")
			os.chdir(wd)
			await update_mango()
			#except:
			#	print("whooops")


	else:
		await ctx.send("aborting")
	pass

async def prepMango(title):
	title = title.lower()
	title = title.replace(' ','-')
	title = title.replace('!','')
	title = title.replace("'",'')
	title = title.encode('ascii','ignore').decode('utf-8')
	return title

async def getMango(begin,chapNum,url):
	browser = webdriver.Chrome()
	for chapter in range(begin+1,int(chapNum) + 1):
				page = 1
				browser.get(url + '/' + str(chapter))
				#print("navved")
				try:
					maxPage = int(''.join(c for c in browser.find_element_by_id('selectpage').text.split('of')[1] if c.isdigit()))
					img = browser.find_element_by_id('img').get_attribute('src')
					imdata = requests.get(img)
					with open(str(chapter)+'_'+str(page) + '.jpg','wb') as writer:
						writer.write(imdata.content)
					await asyncio.sleep(1)
					for page in range(2,maxPage+1):
						browser.get(url + '/' + str(chapter) + '/' + str(page))
						img = browser.find_element_by_id('img').get_attribute('src')
						imdata = requests.get(img)
						with open(str(chapter)+'_'+str(page) + '.jpg','wb') as writer:
							writer.write(imdata.content)
				except Exception as e:
					print("Hollow page " + str(e)) 


async def update_mango():
	global mangoDict
	file = open("mangos/lists.txt",'w')
	file.write(str(mangoDict))
	file.close()

def read_mango():
	global mangoDict
	file = open("mangos/lists.txt",'r')
	content = file.read().replace('\n', '')
	#print(content)
	mangoDict = ast.literal_eval(content)
	file.close()
	#print(mangoDict.get('me'))
	#print(mangoDict.get('me').get('concerned'))

def extract_number(f):
	s = re.findall("\d+(?=_)",f)
	return(int(s[0]) if s else -1,f)

def extract_number2(f):
	s = re.findall("\d+(?=\.)",f)
	return(int(s[0]) if s else -1,f)	

async def check_mango():
	global mangoDict
	wd = os.getcwd()
	browser = webdriver.Chrome()
	os.chdir('mangos')
	for mango, url in mangoDict['me'].items():
		if mango != 'concerned':
			#print(url)
			browser.get(url)
			dire = await prepMango(mango)
			os.chdir(dire)
			chapNum = browser.find_element_by_class_name("chico_manga").find_element_by_xpath("..").find_element_by_tag_name("a").text
			chapNum = int(chapNum[len(mango)+1:])
			if not os.path.isfile('./mangos/' + dire + '/' + str(chapNum) + "_1.jpg"):
				dirList = os.listdir('./')
				if len(dirList) < 1:
					start = 0
				else:
					start = int(max(dirList,key=extract_number).split('_')[0])
				#print(str(start))
				await getMango(start,chapNum,url)
			os.chdir('..')
	os.chdir(wd)

async def mango_next(ctx):
	global mangoDict
	if str(ctx.message.author) in mangoDict:
		current = mangoDict.get(str(ctx.message.author))[1]
		dire = await prepMango(current)
		chpList = os.listdir('./mangos/' + dire + '/')
		# print(chpList)
		# chpList.sort(key=extract_number2)
		# print(chpList)
		# chpList.sort(key=extract_number)
		# print(chpList)
		chpList = natsorted(chpList)
		#print(chpList)
		currentIn = chpList.index(str(mangoDict.get(str(ctx.message.author))[0][current]))
		if currentIn != len(chpList) - 1:
			mangoDict.get(str(ctx.message.author))[0][current] = chpList[currentIn + 1]
			await ctx.send(file=discord.File('mangos/' + current + '/' + str(mangoDict[str(ctx.message.author)][0][current])))
		else:
			await ctx.send("You've read all of that mango")
			print("RIP")
		await update_mango()

async def mango_prev(ctx):
	global mangoDict
	if str(ctx.message.author) in mangoDict:
		current = mangoDict.get(str(ctx.message.author))[1]
		dire = await prepMango(current)
		chpList = os.listdir('./mangos/' + dire + '/')
		chpList = natsorted(chpList)
		# chpList.sort(key=extract_number2)
		# chpList.sort(key=extract_number)
		currentIn = chpList.index(str(mangoDict.get(str(ctx.message.author))[0][current]))
		if currentIn != 0:
			mangoDict.get(str(ctx.message.author))[0][current] = chpList[currentIn - 1]
			await ctx.send(file=discord.File('mangos/' + current + '/' + str(mangoDict[str(ctx.message.author)][0][current])))
		else:
			await ctx.send("You're reading the first page of that mango")
			print("RIP")
		await update_mango()

async def playfile_process():
	global ScreamChamber
	global ServerChan
	global currentlyPlaying
	global songStart
	global playerDeque
	global announceDeque
	await my_bot.wait_until_ready()
	print('playfile_process start')
	try:
		while True:
			source = None
			#print(len(playerDeque))
			#print(len(announceDeque))
			if len(announceDeque) > 0:
				source = announceDeque.popleft()
				print("announce found")
			elif len(playerDeque) > 0:
				if not announcing.empty():
					announcing.get()
				source = playerDeque.popleft()
				print("Song found")
			if source is not None:
				print("We have noise")
				had_to_join = False
				channel = my_bot.get_channel(ScreamChamber)
				server = my_bot.get_guild(ServerChan)
				print("Beginning checks")
				voice = None
				if server.voice_client is not None:
					print("Voice is connected")
					voice = server.voice_client
					had_to_join = False
				else:
					print("Manufacturing voice")
					voice = await my_bot.get_channel(ScreamChamber).connect()
					had_to_join = True
				print("Create file player")
				voice.play(source,after=lambda e: afterCheck(e))
				while voice.is_playing() or voice.is_paused():
					#print("PLAAYING")
					await asyncio.sleep(1)
				print("play queue done")
				if (had_to_join) and not (voice.is_playing() or voice.is_paused()):
					print("What the fuck nintendo")
					await voice.disconnect()
				print(had_to_join)
				print(voice.is_playing())
				print(voice.is_paused())
				if len(announceDeque) < 1 and len(playerDeque) < 1 and not (voice.is_playing() or voice.is_paused()):
					if not announcing.empty():
						announcing.get()
					await voice.disconnect()
			await asyncio.sleep(1)
	except:
		fileStat.put(1)
		print("Playfile process dead")


# Process that handles mp3 announces
async def announce_process(q):
	await my_bot.wait_until_ready()
	global playbackVol
	global soundDict
	print('announce_process start')
	#tts = gTTS(text='meme', lang='pt')
	#tts.save("bites/££meme.mp3")
	try:
		while not exitFlag:
			if not q.empty():
				event = q.get()
				if str(event[:7]) == 'schlorp':
					if event[7]  == '1':
						start = 'schlorp/schlorp_' + event[8] + '.mp3'
						middle = 'schlorp/' + event[9:] + '.mp3'
						end = 'schlorp/indi_' + event[7] + '.mp3'
						cmd = 'ffmpeg -y -i "concat:' + start + '|' + middle + '|' + end + '" -c copy result' + event[9:] + '.mp3'
						os.system(cmd)
						await swippity("result" + event[9:] + ".mp3",playbackVol, False)
						print("Swippitied")
					else:
						start = 'schlorp/schlorp_' + event[8] + '.mp3'
						end = 'schlorp/' + event[9:] + '.mp3'
						middle = 'schlorp/indi_' + event[7] + '.mp3'
						cmd = 'ffmpeg -y -i "concat:' + start + '|' + middle + '|' + end + '" -c copy result' + event[9:] + '.mp3'
						os.system(cmd)
						await swippity("result" + event[9:] + ".mp3",playbackVol, False)
						print("Swooppitied")
				if str(event[:4]) == 'hate':
					start = 'hate/hate.mp3'
					end = 'hate/' + event[4:] + '.mp3'
					cmd = 'ffmpeg -y -i "concat:' + start + '|' + end + '" -c copy hate/result' + event[4:] + '.mp3'
					os.system(cmd)
					await swippity('hate/result' + event[4:] + '.mp3', playbackVol, False)
				if str(event[:6]) == 'sounds':
					if(soundDict[event[6:]] is not 1):
						index = random.randint(1,soundDict[argu])
						await swippity('drive/sounds/££' + event[6:] + str(index) + '.mp3',playbackVol, False)
					else:
						await swippity('drive/sounds/££' + event[6:] + '1.mp3',playbackVol, False)
				if str(event[:5]) == 'house':
					if event[5] == 'V':
						await swippity("drive/PUBG/Verbose/" + event[6:] + '.mp3',150, False)
					else:
						await swippity("drive/PUBG/Name/" + event[6:] + '.mp3',150, False)
				if str(event[:5]) == 'theme':
					print("Theme time")
					print(str(event[-6:-4]))
					await swippity(event[5:] ,event[-6:-4], False)
				if event is 'goblins':
					await swippity('bites/££gablins.mp3',playbackVol, False)
				if event is 'sciBitch':
					await swippity('bites/££possible.mp3',playbackVol, False)
				if event is 'doktor':
					await swippity('bites/££memeinhib.mp3',playbackVol, False)
				if event is 'muffin':
					await swippity('bites/££muffin.mp3',playbackVol, False)
				if event is 'gargle':
					await swippity('bites/££gargle.mp3',playbackVol, False)
				if event is 'ergh':
					await swippity('bites/££euuurgh.mp3',playbackVol, False)
				if event is 'meme':
					await swippity('bites/££meme.mp3',playbackVol, False)
				if event is 'jobDone':
					await swippity('bites/££jobDone.mp3',playbackVol, False)
				if event is 'bitch':
					await swippity('bites/££stpdbitch.mp3',playbackVol, False)
				if event is 'mistake':
					await swippity('bites/££mistake.mp3',playbackVol, False)
				if event is 'nope':
					await swippity('bites/££fuckthis.mp3',playbackVol, False)
				if event is 'pump':
					await swippity('bites/££pump.mp3',playbackVol, False)
				if event is 'anxiety':
					await swippity('bites/££social.mp3',playbackVol, False)
				if event is 'fagin':
					await swippity('bites/££fagin.mp3',playbackVol, False)
				if event is 'say':
					await ttsIt()
				if event is 'bastard':
					await swippity('bites/££bastard.mp3',playbackVol, False)
				if event is 'crazy':
					await swippity('bites/££crazy.mp3',playbackVol, False)
				if event is 'myBrand':
					await swippity('bites/££myBrand.mp3',playbackVol, False)
				if event is 'die':
					await swippity('bites/££die.mp3',playbackVol, False)
				if event is 'trash':
					await swippity('bites/££trash.mp3',playbackVol, False)
				if event is 'fishie':
					await swippity('bites/££fishie.mp3',playbackVol, False)
				if event is 'onme':
					await swippity('bites/££jokesonme.mp3',playbackVol, False)
				if event is 'dingus':
					await swippity('bites/££dingus.mp3',playbackVol, False)
				if event is 'turns':
					await swippity('bites/££dead.mp3',playbackVol, False)
				if event is 'serenade':
					await swippity('bites/££serenade.mp3',playbackVol, False)
				if event is 'rochefuck':
					await swippity('bites/££rochefuck.mp3',playbackVol, False)
				if event is 'canada':
					await swippity('bites/££canada.mp3',playbackVol, False)
				if event is 'soGood':
					await swippity('bites/££goood.mp3',playbackVol, False)
				if event is 'loser':
					await swippity('bites/££whataloser.mp3',playbackVol, False)
				if event is 'warcrime':
					await swippity('bites/££warcrime.mp3',playbackVol, False)
				if event is 'earholes':
					await swippity('bites/££earholes.mp3',playbackVol, False)
				if event is 'baba':
					await swippity('bites/££baba.mp3',playbackVol, False)
				if event is 'fuckYou':
					await swippity('bites/££fuckYou.mp3',playbackVol, False)
				if event is 'kids':
					await swippity('bites/££twoKids.mp3',playbackVol, False)
				if event is 'curse':
					await swippity('bites/££bigInsult.mp3',playbackVol, False)
				if event is 'santa':
					await swippity('bites/££santa.mp3',playbackVol, False)
				if event is 'yummy':
					await swippity('bites/££yummy.mp3',playbackVol, False)
				#x = announcing.get()
			else:
				pass

			await asyncio.sleep(1)
	except:
		announceStat.put(1)
		print("Announce process dead")


# The process which takes in instructions and distributes/execs them
async def dist_process(q, pq):
	await my_bot.wait_until_ready()
	print('dist_process start')
	#try:
	while not exitFlag:
		if not q.empty():
			[inst, argu] = q.get()  # Get instruction
			#print(inst)
			if inst is 'findAlt':  # Find 3 results
				await asyncio.ensure_future(findAlt2(argu))
			if inst is 'findx':  # Find 1 result
				await find2(argu)
			if inst is 'play':  # Play no. 1 result
				pq.put(argu)
			if inst is 'loop': #Loop play#
				#print("shit")
				if(repeat.empty()):
					repeat.put(1)
					if str(argu) != '':
						pq.put(argu)
				else:
					repeat.get()
			if inst is 'app':
				await asyncio.ensure_future(fetchAndAttach(argu[0],argu[1]))
			if inst is 'poll':
				await asyncio.ensure_future(maintainPoll(argu[0],argu[1], True))
			if inst is 'asciit':
				await asyncio.ensure_future(makeAscii(argu))
			if inst is 'concerned':
				await asyncio.ensure_future(dlConc())
			if inst is 'mango_list':
				await asyncio.ensure_future(mango_list(argu))
			if inst is 'mango_mine':
				await asyncio.ensure_future(mango_mine(argu))
			if inst is 'mango_add':
				await asyncio.ensure_future(mango_add(argu))
			if inst is 'mango_rem':
				await asyncio.ensure_future(mango_rem(argu))
			if inst is 'mango_next':
				await asyncio.ensure_future(mango_next(argu))
			if inst is 'mango_prev':
				await asyncio.ensure_future(mango_prev(argu))
			if inst is 'mango_req':
				await asyncio.ensure_future(mango_request(argu))	
		else:
			pass
		await asyncio.sleep(1)
	#except:
	#	distStat.put(1)
	#	print("Dist process dead")


async def greet_process(q):
	await my_bot.wait_until_ready()
	print('greet_process start')
	try:
		while not exitFlag:
			if not q.empty():
				mention = q.get()
				await sendGreet(mention)
			else:
				pass
			await asyncio.sleep(1)
	except:
		greetStat.put(1)
		print("Greet process dead")

# Process which handles playing things queued in the song queue
async def player_process(q,prepNext,nextPrepped):
	await my_bot.wait_until_ready()
	print('player_process start')
	global ServerChan
	global ScreamChamber
	global playbackVol
	server = my_bot.get_guild(ServerChan)
	current_time = 0
	prev_time = 0
	ring = True
	success = True
	try:
		while not exitFlag:
			if ring is not True:  # Boolean for the you called sound
				current_time = time.time()
			if prev_time == 0 or (current_time - prev_time) > 3600:
				ring = True
			if not q.empty():
				prev_time = time.time()
				# Get song from queue(removes the item from the queue)
				song = q.get()
				success = True
				# Handles voice continued connection vs joining
				while(success):
					try:
						if server.voice_client is not None:
							print("Acquiring voice\n")
							voice = server.voice_client
							print(voice)
							if voice is None:
								print("No voice")
						else:
							print("Manufacturing voice\n")
							channel = my_bot.get_channel(282975292182495232)
							voice = await my_bot.get_channel(ScreamChamber).connect()
							if ring is True:
								#playing.put(1)
								await playfile('££yourang.mp3',playbackVol, False, True)
								#playing.get()
								ring = False
						#while not announcing.empty():
						#	await asyncio.sleep(1)
						#playing.put(1)
						try:
							await play2(song, voice)
						except:
							pass
						while not repeat.empty():
							try:
								await play2(song, voice)
							except:
								pass
							await asyncio.sleep(1)
						#x = playing.get()
						success = False
					except:
						success = False
			else:
				# Disconnects voice if still connected without songs in queue
					#if server.voice_client is not None:
					#	if announcing.empty():
					#		voice = server.voice_client
					#		await voice.disconnect()
					#	else:
					#		pass
					#else:
				pass
			await asyncio.sleep(1)
	except:
		playerStat.put(1)
		print("Player process dead")

async def dl_process(q,playQ):
	await my_bot.wait_until_ready()
	print('dl_process start')
	try:
		while not exitFlag:
			if not q.empty():
				song = q.get()
				linklist = await ytLokupGrab(song,True)
				if linklist is None:  # Checks for populated results
					pass
				else:
					try:
						songFile, songTitle = linklist[0]
						#songFile = songFile[24:]
						print(songTitle)
						#songFile = songFile.replace('?', '#')
						if not recentSongList.search(songTitle):  # If new song
							if recentSongList.size is not 10:
								#playQ.put(songFile)
								try:
									recentSongList.add(songTitle)
									await grabSong(songFile, songTitle)
									playQ.put('./recent/' + songTitle + '.mp3')
								except:
									print("Failed to DL")
							else:
								try:
									os.remove(songTitle + '.mp3')
									recentSongList.remove(recentSongList.tail)
									recentSongList.add(songTitle)
									await grabSong(songFile, songTitle)
									playQ.put('./recent/' + songTitle + '.mp3')
								except:
									print("Failed to DL")
						else:
							print("We got em")
							playQ.put('./recent/' + songTitle + '.mp3')
					except:
						print("Well shit")
			await asyncio.sleep(1)
	except:
		dlStat.put(1)
		print("DL process dead")


async def mango_get_process():
	print("Checking mangos")
	await check_mango()

"""


LAUNCH SECTION


"""

# On bot ready
@my_bot.event
async def on_ready():
	discord.opus.load_opus
	print("Client logged in")
	await greetBirthdays()

# Spawns the different process threads
def spawn_processes():
	my_bot.loop.create_task(dist_process(instQueue, dlQueue))
	my_bot.loop.create_task(player_process(songQueue,prepNext,nextPrepped))
	my_bot.loop.create_task(announce_process(eventQueue))
	my_bot.loop.create_task(greet_process(greetQ))
	my_bot.loop.create_task(dl_process(dlQueue,songQueue))
	my_bot.loop.create_task(playfile_process())
	my_bot.loop.create_task(mango_get_process())
	# my_bot.loop.create_task(hail_process(eventQueue))

print("remember to grive sync for reactions")
spawn_processes()
readPlaylists()
readPolls()
for filename in os.listdir("."):
	if not filename.endswith(".py") and filename[:2] != '££' and not filename.endswith(".git") and os.path.isfile(os.path.join('.', filename)):
		os.remove(filename)
for filename in os.listdir('./recent/'):
	os.remove('./recent/' + filename)

transtable = dict.fromkeys(map(ord, '£1234567890'), None)
branstable = dict.fromkeys(map(ord, '£'), None)
#transtable = table["",None]
for filename in os.listdir('./drive/reactions/'):
	query = os.path.splitext("./drive/reactions/" + filename)[0]
	query = str(query)
	query = query[18:]
	query = query.translate(transtable)
	#print(query)
	if query in rxDict:
		rxDict[query] += 1
	else:	
		rxDict[query] = 1
for filename in os.listdir('./drive/sounds/'):
	query = os.path.splitext("./drive/sounds/" + filename)[0]
	query = str(query)
	query = query[15:]
	query = query.translate(transtable)
	#print(query)
	if query in soundDict:
		soundDict[query] += 1
	else:	
		soundDict[query] = 1
for filename in os.listdir('./drive/PUBG/Verbose'):
	query = os.path.splitext("./drive/PUBG/Verbose/" + filename)[0]
	query = str(query)
	query = query[21:]
	query = query.translate(transtable)
	#print(query)
	if query in HouseRulesDict:
		HouseRulesDict[query] += 1
	else:	
		HouseRulesDict[query] = 1
for filename in os.listdir('./themes/'):
	query = os.path.splitext("./themes/" + filename)[0]
	query = str(query)
	query = query[9:]
	query = query.translate(branstable)
	vol = query[-2:]
	query = query[:-2]
	if query in themeDict:
		themeDict[query] = vol
	else:	
		themeDict[query] = vol

readBirthdays()
read_mango()
#(Shasocais:274),

my_bot.run(bot_key(),reconnect=True)
if(my_bot.is_closed()):
	print("DEAD BOT")
	my_bot.run(bot_key(),reconnect=True)



#https://stackoverflow.com/search?q=
