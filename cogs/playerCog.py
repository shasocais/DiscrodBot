import nextcord
from nextcord.ext import commands
from nextcord.ext import tasks
import youtube_dl
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
        self.should_dc = False
        self.volume = 50

    @tasks.loop(seconds=1)
    async def play_queue_processor(self):
        if not self.playerQueue.empty():
            source, priority = self.playerQueue.get()
            if priority == "low":
                self.low_prio_queue.append(source)
            else:
                self.high_prio_queue.append(source)

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
        if not self.voice:
            print("acquiring voice")
            self.voice = await self.bot.get_channel(self.scream_chamber_id).connect()
        self.voice.play(source, after=lambda e: self.after_check(e))
        while self.voice.is_playing() or self.voice.is_paused():
            await asyncio.sleep(1)
        if self.should_dc:
            await self.voice.disconnect()

    @commands.command(name='skip')
    async def skip(self, ctx):
        if self.voice:
            self.voice.stop()

    @commands.command(name='pause')
    async def pause(self, ctx):
        if self.voice:
            self.voice.pause()

    @commands.command(name='resume')
    async def resume(self, ctx):
        if self.voice and self.voice.is_paused():
            self.voice.resume()

    @commands.command(name='volume')
    async def volume(self, ctx, arg):
        volume = float(arg) / 100 if arg.isdecimal() else self.volume
        self.volume = volume
        if self.voice:
            self.voice.source.volume = volume


def setup(bot):
    bot.add_cog(PlayerCog(bot))
