import os
import sys
import json

from Item import *


class Inventory(): 

	items = {}
	locations = {}

	def __init__(self) -> None:
		pass

	def load_json(self, json_file):
		# Load json file
		f = open(json_file, "r")
		text = f.read()
		f.close()
		print(text)
		data = json.loads(text)
		print(data)
		self.items = data["items"]
		self.locations = data["locations"]

	
	def save_json(self, json_file):
		self.items["m8_20"] = "L4"
		self.locations["L4"] = "m8_20"
		f = open(json_file, 'w+')
		form_dict = {}
		form_dict["items"] = self.items
		form_dict["locations"] = self.locations
		form_text = json.dumps(form_dict, indent=4)
		f.write(form_text)
		f.close()


	def search(self, text):
		# Search database for parameter
		pass

	def move(self, item):
		pass
