import datetime

import nextcord
from nextcord.ext import commands
from nextcord.ext import tasks
import yt_dlp
from selenium import webdriver
from pyvirtualdisplay import Display
import logging
import asyncio
from collections import deque

from selenium.webdriver.common.by import By

import global_handlers
from general_functions import *
import os


class PlayerCog(commands.Cog):
    DC_TIMEOUT = 5
    def __init__(self, bot):
        self.bot = bot
        self.playerQueue = global_handlers.PLAYERQUEUE
        self.scream_chamber_id = global_handlers.SCREAMCHAMBER
        self.exit = None
        self.play_queue_processor.start()
        self.low_prio_queue_processor.start()
        self.high_prio_queue_processor.start()
        self.voice = None
        self.low_prio_queue = deque()
        self.high_prio_queue = deque()
        self.logger = global_handlers.GLOBAL_LOGGER
        self.should_dc = False
        self.volume = 1
        self.pause_timestamp = datetime.datetime.now()

    @tasks.loop(seconds=1)
    async def play_queue_processor(self):
        if not self.playerQueue.empty():
            source, priority = self.playerQueue.get()
            if priority == "low":
                self.low_prio_queue.append(source)
            else:
                self.high_prio_queue.append(source)
        if self.voice and self.voice.is_paused():
            # voice is paused
            if datetime.datetime.now() - self.pause_timestamp > datetime.timedelta(PlayerCog.DC_TIMEOUT,0,0):
                # voice has been paused a long time
                self.low_prio_queue.clear()
                self.high_prio_queue.clear()
                await self.voice.disconnect()

    @tasks.loop(seconds=1)
    async def low_prio_queue_processor(self):
        if not len(self.low_prio_queue) == 0:
            source = self.low_prio_queue.pop()
            while self.voice is not None and (self.voice.is_playing() or self.voice.is_paused()):
                await asyncio.sleep(1)
            await self.play_source(source)

    @tasks.loop(seconds=1)
    async def high_prio_queue_processor(self):
        if not len(self.high_prio_queue) == 0:
            source = self.high_prio_queue.pop()
            if self.voice and (self.voice.is_playing() or self.voice.is_paused()):
                self.voice.pause()
                self.low_prio_queue.appendleft(self.voice.source)
            await self.play_source(source)

    def after_check(self, e):
        if len(self.high_prio_queue) == 0 \
                and len(self.low_prio_queue) == 0:
            self.should_dc = True

    async def play_source(self, source):
        source.volume = self.volume
        if not self.voice or not self.voice.is_connected():
            print("acquiring voice")
            self.voice = await self.bot.get_channel(self.scream_chamber_id).connect()
        try:
            self.voice.play(source, after=lambda e: self.after_check(e))
            while self.voice.is_playing() or self.voice.is_paused():
                await asyncio.sleep(1)
        except Exception as e:
            self.logger.warn(f"Playing file failed {e}")
        if self.should_dc:
            await self.voice.disconnect()

    @commands.command(name='skip',
					help='skip currently playing sound source',
					brief='skip currently playing sound source')
    async def skip(self, ctx):
        if self.voice:
            self.voice.stop()

    @commands.command(name='pause',
					help=f"pause currently playing sound source, if left paused for > {DC_TIMEOUT} minutes",
					brief='pause currently playing sound source')
    async def pause(self, ctx):
        if self.voice:
            self.voice.pause()
            self.pause_timestamp = datetime.datetime.now()

    @commands.command(name='resume',
					help='resume currently playing sound source',
					brief='resume currently playing sound source')
    async def resume(self, ctx):
        if self.voice and self.voice.is_paused():
            self.voice.resume()

    @commands.command(name='volume',
					help='change volume of currently playing sound source, arg 0-100',
					brief='change player volume')
    async def volume(self, ctx, arg):
        volume = float(arg) / 100 if arg.isdecimal() else self.volume
        self.volume = volume
        if self.voice:
            self.voice.source.volume = volume


def setup(bot):
    bot.add_cog(PlayerCog(bot))
