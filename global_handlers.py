import queue
from keys import SCREAMCHAMBER, SERVERID
import gtts.lang
from pyvirtualdisplay import Display

import helper_classes
from html.parser import HTMLParser
import logging

GTTS_LANGS = gtts.lang.tts_langs()
DISPLAY = Display(visible=False, size=(800, 800))
DISPLAY.start()
logging.basicConfig()
logging.root.setLevel(logging.WARNING)
logging.basicConfig(level=logging.WARNING)
GLOBAL_LOGGER = logging.getLogger("global_logger")
GLOBAL_LOGGER.setLevel(0)
ANNOUNCEQUEUE = queue.Queue()
PLAYERQUEUE = queue.Queue()
DOWNLOADQUEUE = queue.Queue()
SOURCEQUEUE = queue.Queue()
FILEQUEUE = queue.Queue()
PLAYLISTDICT = {}
POLLLIST = helper_classes.PollList()
RECENTSONGLIST = helper_classes.SongList()
SOUNDDICT = helper_classes.CustomDictonary()
REACTIONDICT = helper_classes.CustomDictonary()
THEMEDICT = {}
HTML_PARSER = HTMLParser()
TRANSLATION_TABLE = dict.fromkeys(map(ord, '£1234567890'), None)


