import os
import random

import nextcord
from typing import List


class CustomLinkedListNode:
	def __init__(self):
		self.__next = None
		self.__prev = None

	def get_next(self):
		return self.__next

	def get_prev(self):
		return self.__prev

	def set_next(self, item):
		self.__next = item

	def set_prev(self, item):
		self.__prev = item


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
	def random_select(self, key):
		return random.choice(self.__items.get(key))

	def keys(self):
		return list(self.__items.keys())
	def add_entry(self, key):
		if not self.__items.get(key):
			self.__items[key] = []

	def remove_entry(self, key):
		if self.__items.get(key):
			self.__items.pop(key)

	def add_element(self, key, item):
		if self.__items.get(key):
			self.__items[key].append(item)

	def remove_element(self, key, item):
		if self.__items.get(key):
			if item in self.__items[key]:
				self.__items[key].remove(item)

	def entry_size(self, key):
		if self.__items.get(key):
			return len(self.__items.get(key))
		else:
			return 0

class Poll(CustomLinkedListNode):
	def __init__(self, questions, opts, message, total, ident):
		super().__init__()
		self.questions = questions
		self.opts = opts
		self.message = message
		self.total = total
		self.ident = ident

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
		super().__init__(options=self.held_options,placeholder="Choose a Category")

	async def callback(self, interaction: nextcord.Interaction):
		assert self.view is not None
		view: DriveView = self.view

		view.remake_selector(self.values[0])


class DriveInputField(nextcord.ui.TextInput["DriveView"]):
	def __init__(self):
		super().__init__(label="Create custom category")

class DriveToggleButton(nextcord.ui.Button["DriveView"]):
	def __init__(self):
		# A label is required, but we don't need one so a zero-width space is used
		# The row parameter tells the View which row to place the button under.
		# A View can only contain up to 5 rows -- each row can only have 5 buttons.
		# Since a Tic Tac Toe grid is 3x3 that means we have 3 rows and 3 columns.
		super().__init__(style=nextcord.ButtonStyle.secondary, label="Custom Category?")

	# This function is called whenever this particular button is pressed
	# This is part of the "meat" of the game logic
	async def callback(self, interaction: nextcord.Interaction):
		assert self.view is not None
		view: DriveView = self.view
		# Fire Custom Category modal
		self.fired_modal = DriveCategoryModal()
		await interaction.response.send_modal(self.fired_modal)
		await self.fired_modal.wait()
		print(self.fired_modal.input_field.value)
		view.remake_selector(self.fired_modal.input_field.value)
class DriveCategoryModal(nextcord.ui.Modal):
	def __init__(self):
		super().__init__(title="Set Custom Category")
		self.input_field = DriveInputField()
		self.add_item(self.input_field)

	async def callback(self, interaction: nextcord.Interaction) -> None:
		response = f"Creating new category {self.input_field.value}"
		await interaction.send(response)
		self.stop()


class DriveView(nextcord.ui.View):
	def __init__(self, options_list : List[str]) -> None:
		super().__init__()
		self.options = options_list
		self.has_opts = len(options_list) > 0
		self.button = DriveToggleButton()
		self.add_item(self.button)
		self.result = ""
		if self.has_opts:
			self.selector_template = CategorySelect(self.options)
			self.add_item(self.selector_template)

	def remake_selector(self, option_to_add : str):
		self.result = option_to_add
		self.stop()