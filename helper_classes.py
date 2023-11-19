import os
import random

import nextcord
from typing import List

from general_functions import make_pie_chart


class CustomLinkedListNode:
	def __init__(self):
		self.__next = None
		self.__prev = None
		self.__container = None

	def get_next(self):
		return self.__next

	def get_prev(self):
		return self.__prev

	def get_container(self):
		return self.__container

	def set_next(self, item):
		self.__next = item

	def set_prev(self, item):
		self.__prev = item

	def set_container(self, container):
		self.__container = container


class CustomLinkedList:
	def __init__(self):
		self.__head = None
		self.__tail = None

	def is_empty(self):
		return self.__head is None

	def get_head(self):
		return self.__head

	def set_head(self, head):
		self.__head = head

	def get_tail(self):
		return self.__tail

	def set_tail(self, tail):
		self.__tail = tail

	def size(self):
		current = self.get_head()
		count = 0
		while current is not None:
			count = count + 1
			current = current.get_next()
			if current is self.get_head():
				break
		return count

	def to_list(self):
		output = [self.get_head()]
		while len(output) < self.size():
			output.append(output[-1].get_next())
		return output


class CustomDictonary:
	def __init__(self):
		self.__items = {}

	def exists(self, key):
		return key in self.__items

	def get_cleaned_element(self, element_path):
		return os.path.splitext(os.path.split(element_path)[-1])[0][2:]

	def element_exists(self, key, element):
		if self.exists(key):
			return any(
				element == item for item in [self.get_cleaned_element(file_path) for file_path in self.__items[key]])

	def get_element(self, key, target_element):
		return next((element for element in self.__items[key] if self.get_cleaned_element(element) == target_element),
		            None)

	def random_select(self, key):
		return random.choice(self.__items.get(key))

	def keys(self):
		return list(self.__items.keys())

	def add_entry(self, key):
		if self.__items.get(key) is None:
			self.__items[key] = []

	def remove_entry(self, key):
		if self.__items.get(key) is not None:
			self.__items.pop(key)

	def add_element(self, key, item):
		if self.__items.get(key) is not None:
			self.__items[key].append(item)

	def remove_element(self, key, item):
		if self.__items.get(key) is not None:
			if item in self.__items[key]:
				self.__items[key].remove(item)

	def entry_size(self, key):
		if self.__items.get(key) is not None:
			return len(self.__items.get(key))
		else:
			return 0

	def to_length_dict(self):
		outp_list = []
		for key in self.keys():
			outp_list.append((key, len(self.__items.get(key))))
		return outp_list


class Poll(CustomLinkedListNode):
	def __init__(self, questions, opts, message, total, ident):
		super().__init__()
		self.questions = questions
		self.opts = opts
		self.message = message
		self.total = total
		self.ident = ident

	def add_vote(self, opt):
		if opt in self.opts:
			self.opts[opt] += 1
			self.total += 1
			self.get_container().write_out()

	def add_opt(self, opt):
		if opt not in self.opts:
			self.opts[opt] = 0

	def get_option_labels(self):
		outp_dict = {}
		for opt in self.get_opts():
			label = "{"
			if self.get_total() > 0:
				prop = int(self.get_opts()[opt] / self.get_total() * 100) // 5
			else:
				prop = 0
			for i in range(prop):
				label += "+"
			for i in range(prop, 20):
				label += "×"
			label += f"}} : {str(self.get_opts()[opt])}"
			outp_dict[opt] = label
		return outp_dict

	def get_option_sizes(self):
		sizes = []
		poll_has_votes = self.get_total() > 0
		for opt in self.get_opts():
			if poll_has_votes:
				sizes.append(round(self.get_opts()[opt] / self.get_total(), 2))
			else:
				sizes.append(0.00)
		return sizes

	def get_questions(self):
		return self.questions

	def get_opts(self):
		return self.opts

	def get_message(self):
		return self.message

	def get_total(self):
		return self.total

	def get_ident(self):
		return self.ident

	def set_questions(self, questions):
		self.questions = questions

	def set_opts(self, opts):
		self.opts = opts

	def set_message(self, message):
		self.message = message

	def set_total(self, total):
		self.total = total

	def set_ident(self, ident):
		self.ident = ident


class PollList(CustomLinkedList):
	def __init__(self):
		super().__init__()

	def add(self, questions, opts, message, total, ident=-1):
		if self.get_head() is not None and ident == -1:
			ident = self.get_head().getIdent() + 1
		elif ident == -1:
			ident = 0
		poll = Poll(questions, opts, message, total, ident)
		if self.get_head() is not None:
			poll.set_next(self.get_head().get_next())
			self.get_head().set_next(poll)
			poll.get_next().set_prev(poll)
			poll.set_prev(self.get_head())
			self.set_head(poll)
		else:
			poll.set_prev(poll)
			poll.set_next(poll)
			self.set_head(poll)
		poll.set_container(self)
		return poll

	def remove(self, ident):
		found, ind = self.search(ident)
		if found:
			ind.get_next().set_prev(ind.get_prev())
			ind.get_prev().set_next(ind.get_next())
			if ind is self.get_head():
				self.set_head(ind.get_prev())
			if ind is self.get_tail():
				self.set_tail(ind.get_next())
			os.remove('polls/££' + str(ident) + 'tastyPie.png')

	def search(self, ident):
		current = None
		if self.get_head() is not None:
			current = self.get_head()
			found = False
			while current is not None and not found:
				if current.get_ident() == ident:
					found = True
				else:
					current = current.get_next()
					if current is self.get_head():
						break
		else:
			found = False
		return found, current

	def write_out(self):
		file = open("polls/££polls.txt", 'w')
		written_text = "("
		done = False
		current = self.get_head()
		while not done:
			if not (current is None):
				questions = current.get_questions()
				opts = current.get_opts()
				total = current.get_total()
				ident = current.get_ident()
				written_text = written_text + "[" + questions + "`" + str(opts) + "`" + str(total) + "`" + str(
					ident) + "]/"
				current = current.get_next()
				if current == self.get_head() or current is None:
					done = True
			else:
				done = True
		written_text = written_text + ")"
		file.write(written_text)
		file.close()


class SongNode(CustomLinkedListNode):
	def __init__(self, init_name, init_url):
		super().__init__()
		self.name = init_name
		self.url = init_url

	def get_name(self):
		return self.name

	def get_url(self):
		return self.url

	def set_name(self, new_name):
		self.name = new_name

	def set_url(self, new_url):
		self.url = new_url


class SongList(CustomLinkedList):

	def __init__(self):
		super().__init__()
		self.__recent = None

	def add(self, item_name, item_url):
		temp = SongNode(item_name, item_url)
		if self.get_head() is None:
			self.set_head(temp)
			self.set_tail(temp)
			temp.set_next(self.get_head())
			temp.set_prev(self.get_head())
		else:
			temp.set_next(self.get_head())
			temp.set_prev(self.get_head().get_prev())
			self.get_head().get_prev().set_next(temp)
			self.get_head().set_prev(temp)
			self.set_tail(self.get_head())
			self.set_head(temp)
		self.set_recent(temp)

	def get_recent(self):
		if self.__recent:
			return self.__recent.get_name(), self.__recent.get_url()

	def set_recent(self, item):
		self.__recent = item

	def contains(self, item_name):
		current = self.get_head()
		found = False
		while current is not None and not found:
			if current.get_name() == item_name:
				found = True
				self.set_recent(current)
			else:
				current = current.get_next()
				if current is self.get_head():
					break
		return found

	def retrieve(self, item_name):
		if self.contains(item_name):
			return self.get_recent()

	def remove(self, item_name):
		current = self.get_head()
		previous = None
		found = False
		while not found:
			if current.get_name() is item_name:
				found = True
			else:
				previous = current
				current = current.get_next()
		if previous is None:
			self.set_head(current.get_next())
			self.get_head().set_prev(current.get_prev())
			current.get_prev().set_next(self.get_head())
		else:
			previous.set_next(current.get_next())
			current.get_next().set_prev(previous)
		if current is self.get_tail():
			self.set_tail(current.get_prev())
		os.remove(current.get_name + '.mp3')


class CategorySelect(nextcord.ui.Select["DriveView"]):
	def __init__(self, options_list):
		self.held_options = [nextcord.SelectOption(label=option) for option in options_list]
		super().__init__(options=self.held_options, placeholder="Choose a Category")

	async def callback(self, interaction: nextcord.Interaction):
		assert self.view is not None
		view: DriveView = self.view
		view.wrap_up_selection(self.values[0])


class DriveInputField(nextcord.ui.TextInput["DriveView"]):
	def __init__(self):
		super().__init__(label="Create custom category")


class PollInputField(nextcord.ui.TextInput["PollView"]):
	def __init__(self):
		super().__init__(label="Enter Answer Option")


class CustomButton(nextcord.ui.Button):
	def __init__(self, label, tag, primary=False, provided_callback=None):
		# A label is required, but we don't need one so a zero-width space is used
		# The row parameter tells the View which row to place the button under.
		# A View can only contain up to 5 rows -- each row can only have 5 buttons.
		# Since a Tic Tac Toe grid is 3x3 that means we have 3 rows and 3 columns.
		self.provided_callback = provided_callback
		self.tag = tag
		super().__init__(style=nextcord.ButtonStyle.primary if primary else nextcord.ButtonStyle.secondary, label=label)

	async def callback(self, interaction: nextcord.Interaction) -> None:
		if self.provided_callback is not None:
			await self.provided_callback(interaction, self.tag)


class DriveToggleButton(CustomButton):
	def __init__(self):
		super().__init__("Create Category?", -1)
		self.fired_modal = None

	# This function is called whenever this particular button is pressed
	# This is part of the "meat" of the game logic
	async def callback(self, interaction: nextcord.Interaction):
		assert self.view is not None
		view: DriveView = self.view
		# Fire Custom Category modal
		self.fired_modal = DriveCategoryModal()
		await interaction.response.send_modal(self.fired_modal)
		await self.fired_modal.wait()
		view.wrap_up_selection(self.fired_modal.input_field.value)


class DrivePageButton(CustomButton):
	def __init__(self, forward=True):
		super().__init__("-->" if forward else "<--", -1)
		self.forward = forward

	async def callback(self, interaction: nextcord.Interaction) -> None:
		assert self.view is not None
		view: DriveView = self.view

		view.offset += 24 if self.forward else -24
		view.offset = max(0, view.offset)
		view.offset = min(view.offset, len(view.options) - 24)
		await view.remake_select()
		await interaction.response.edit_message(view=self.view)
	# await interaction.edit_original_message(view=self.view)


class CategoryPageButton(CustomButton):
	def __init__(self, forward=True):
		super().__init__("-->" if forward else "<--", -1)
		self.forward = forward

	async def callback(self, interaction: nextcord.Interaction) -> None:
		assert self.view is not None
		view: CategoryView = self.view

		view.embed.offset += 24 if self.forward else -24
		view.embed.offset = max(0, view.embed.offset)
		view.embed.offset = min(view.embed.offset, view.embed.max_offset)
		view.change_paging()
		await interaction.response.edit_message(embed=view.embed, view=self.view)


class PollVoteButton(CustomButton):
	def __init__(self, opt, tag):
		super().__init__(f"{tag} : {opt}", -1)
		self.opt = opt

	async def callback(self, interaction: nextcord.Interaction) -> None:
		assert self.view is not None
		view: PollView = self.view
		view.embed.poll.add_vote(self.opt)
		view.embed.clear_fields()
		view.embed.refresh_poll_display()
		view.embed.setup_fields()
		await interaction.response.edit_message(embed=view.embed, view=self.view)


class SongDiscoverButton(CustomButton):
	def __init__(self):
		super().__init__("Song to find", -1)

	async def callback(self, interaction: nextcord.Interaction):
		assert self.view is not None
		view: SongView = self.view
		# Fire Custom Category modal
		self.fired_modal = SongModal()
		await interaction.response.send_modal(self.fired_modal)
		await self.fired_modal.wait()
		self.label = self.fired_modal.input_field.value
		await interaction.edit_original_message(view=self.view)
		view.storeSongToFind(self.fired_modal.input_field.value)


class DriveCategoryModal(nextcord.ui.Modal):
	def __init__(self):
		super().__init__(title="Set Custom Category")
		self.input_field = DriveInputField()
		self.add_item(self.input_field)

	async def callback(self, interaction: nextcord.Interaction) -> None:
		response = f"Creating new category {self.input_field.value}"
		await interaction.send(response)
		self.stop()


class SongModal(nextcord.ui.Modal):
	def __init__(self):
		super().__init__(title="Song to find")
		self.input_field = nextcord.ui.TextInput(label="Song Search", placeholder="Enter song to find")
		self.add_item(self.input_field)

	async def callback(self, interaction: nextcord.Interaction) -> None:
		self.stop()


class DriveView(nextcord.ui.View):
	def __init__(self, options_list: List[str]) -> None:
		super().__init__()
		self.options = options_list
		self.offset = 0
		self.has_opts = len(options_list) > 0
		self.button = DriveToggleButton()
		self.add_item(self.button)
		self.result = ""
		if self.has_opts:
			self.selector_template = CategorySelect(self.options[self.offset:min(len(self.options), self.offset + 24)])
			self.add_item(self.selector_template)
			self.add_item(DrivePageButton(False))
			self.add_item(DrivePageButton(True))

	def wrap_up_selection(self, option_to_add: str):
		self.result = option_to_add
		self.stop()

	async def remake_select(self):
		options_list = self.options[self.offset:min(len(self.options), self.offset + 24)]
		self.selector_template.options = [nextcord.SelectOption(label=option) for option in options_list]


class SongView(nextcord.ui.View):
	def __init__(self, playlist_list: List[str]) -> None:
		super().__init__()
		self.song_to_find = ""
		self.searchbtn = SongDiscoverButton()
		self.btn = CustomButton(label="Submit", primary=True, provided_callback=self.submit)
		self.select = nextcord.ui.Select(placeholder="Playlist to add to",
		                                 options=[nextcord.SelectOption(label=option) for option in playlist_list])
		self.add_item(self.searchbtn)
		self.add_item(self.select)
		self.add_item(self.btn)

	def storeSongToFind(self, song_to_find: str):
		self.song_to_find = song_to_find

	async def submit(self, Interaction):
		if self.select.values[0] and self.song_to_find != "":
			self.stop()


class CategoryEmbed(nextcord.Embed):
	def __init__(self, title, categories):
		super().__init__(title=title, description="Category : Element Count pairs")
		self.offset = 0
		self.max_offset = len(categories) - 24
		self.categories = categories
		self.setup_fields()

	def setup_fields(self):
		upper_offset = min(self.offset + 24, self.max_offset)
		display_categories = self.categories[self.offset:upper_offset]
		for category in display_categories:
			self.add_field(name=category[0], value=f"Element Count: {category[1]}")


class PollEmbed(nextcord.Embed):
	def __init__(self, title, poll: Poll):
		super().__init__(title=title)
		self.poll = poll
		self.refresh_poll_display()
		self.setup_fields()

	def setup_fields(self):
		for index, opt in enumerate(self.poll.get_opts()):
			label = f"{self.char_map[index]}: {opt}"
			value = f"{int(self.poll.get_opts()[opt] / max(1, self.poll.get_total()) * 100)}%"
			self.add_field(name=label, value=value)
		self.add_field(name="Poll Status", value=make_pie_chart(self.char_map, self.sizes, 8), inline=False)

	def refresh_poll_display(self):
		self.sizes = self.poll.get_option_sizes()
		self.char_map = "".join([chr(c) for c in range(65313, 65313 + len(self.sizes))])


class CategoryView(nextcord.ui.View):
	def __init__(self, title, categories):
		super().__init__()
		self.embed = CategoryEmbed(title, categories)
		self.add_item(CategoryPageButton(False))
		self.add_item(CategoryPageButton(True))

	def change_paging(self):
		self.embed.clear_fields()
		self.embed.setup_fields()


class PollView(nextcord.ui.View):
	def __init__(self, title, poll_list: PollList):
		super().__init__(timeout=None)
		self.poll_list = poll_list
		self.setup_fields()

	def setup_fields(self):
		for poll in self.poll_list.to_list():
			self.add_item(
				CustomButton(label=poll.get_questions(), tag=poll.get_ident(), provided_callback=self.callback))

	def poll_selected(self, poll: Poll):
		self.poll_labels = poll.get_option_labels()
		count = 65313
		for opt in self.poll_labels:
			self.add_item(PollVoteButton(opt, chr(count)))
			count += 1
		self.embed = PollEmbed("ECH", poll)

	async def callback(self, interaction: nextcord.Interaction) -> None:

		await interaction.response.edit_message(view=self)
	# await interaction.edit_original_message(view=self.view)


def my_hook(d):
	if d['status'] == 'finished':
		print("Done Downloading, now converting")
