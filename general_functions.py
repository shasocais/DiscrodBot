import collections
import itertools
import math

from gtts import gTTS


def s(k,v,a):
	if not v:return '　'
	if a <= v[0]:return k[0]
	return s(k[1:],v[1:],a-v[0])


def create_TTS(text, dir, lang='en', alt_naming_scheme=False, override_name="speak"):
	tts = gTTS(text=text, lang=lang)
	fname = override_name if alt_naming_scheme else text.replace(' ', '')
	tts.save(dir + "/" + fname + ".mp3")
def make_pie_chart(sections, props, rad):
	bigPie = ''
	spacer = chr(65293)
	dia = range(-rad,rad)
	for y in dia:
		pie = ""
		for x in dia:
			if x*x+y*y<rad*rad:
				ang = math.atan2(y, x) / math.pi / 2 + .5
				pie = pie + s(sections, props, ang) + " "
			else:
				pie = pie + f"{spacer} "
		if y != -rad:
			bigPie = bigPie + "`" + pie[2:-1] + "`\n"
	return bigPie

async def setup_pie_chart(poll):
	labels = ""
	sizes = []
	count = 65313
	displayMsg = str(poll.get_ident()) + " : " + poll.get_questions() + "\n"
	for opt in poll.get_opts():
		labels = labels + chr(count)
		count = count + 1
		displayMsg = displayMsg + "{"
		if poll.get_total() > 0:
			sizes.append(round(poll.get_opts()[opt] / poll.get_total(), 2))
			prop = int(poll.get_opts()[opt] / poll.get_total() * 100) // 5
		else:
			prop = 0
			sizes.append(0.00)
		for i in range(prop):
			displayMsg = displayMsg + "+"
		for i in range(prop, 20):
			displayMsg = displayMsg + "×"
		displayMsg = displayMsg + "} "
		displayMsg = displayMsg + opt + ': ' + str(poll.get_opts()[opt]) + "\n"
	pie = make_pie_chart(labels, sizes, 7)
	displayMsg = displayMsg + "\n" + pie
	poll.set_message(displayMsg)


char_offsets = {
	"<circled>": 9301,
	"<base>": 65216,
	"<alt>": -32,
	"<greek>": 816,
	"<bracket>": 9275,
}


def convert_to_unicode_char(char: chr, setting: str = "<base>"):
	return chr(ord(char) + char_offsets[setting])


def sliding_window(iterable, n):
	# sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
	it = iter(iterable)
	window = collections.deque(itertools.islice(it, n), maxlen=n)
	if len(window) == n:
		yield tuple(window)
	for x in it:
		window.append(x)
		yield tuple(window)


def generate_meme_square(text_to_meme: str, setting: str = "<base>"):
	word_len = len(text_to_meme)
	word_list = [convert_to_unicode_char(letter, setting) for letter in text_to_meme.lower()] * 2
	dic = sliding_window(word_list, word_len)
	big_meme = "\n".join("".join(sublist) for sublist in list(dic)[:-1])
	return big_meme