import os
import sys
import json
import datetime


class Inventory(): 

	items = {}
	locations = {}
	families = {}

	def __init__(self) -> None:
		pass

	def load_json(self, json_file):
		# Load json file
		f = open(json_file, "r")
		text = f.read()
		f.close()
		data = json.loads(text)
		self.items = data["items"]
		self.locations = data["locations"]
		self.families = data["families"]

	
	def save_json(self, json_file):
		f = open(json_file, 'w+')
		form_dict = {}
		form_dict["items"] = self.items
		form_dict["locations"] = self.locations
		form_dict["families"] = self.families
		form_text = json.dumps(form_dict, indent=4)
		f.write(form_text)
		f.close()


	def search_item(self, name):
		# Search database for parameter
		if name in self.items:
			return self.items[name]
		else:
			return None

	def move(self, item, new_location):
		name = item["name"]
		location = item["location"]


	def create_item(self, item_name, item_location = "", item_family = "none", item_quantity = 1, quantity_required = 1, desc = ""):

		if item_name in self.items:
			self.items[item_name]["item_quantity"] += item_quantity
		else:
			new_item = {}
			new_item["name"] = item_name
			new_item["location"] = item_location
			new_item["family"] = item_family
			new_item["quantity"] = item_quantity
			new_item["date_mod"] = str(datetime.datetime.utcnow())
			self.items[item_name] = new_item

			if item_location != "":
				self.locations[item_location] = item_name

			if item_family != "":
				if item_family in self.families:
					self.families[item_family].append(item_name)
				else:
					self.families[item_family] = [item_name]

	def delete_item(self, item):
		name = item["name"]
		location = item["location"]
		family = item["family"]

		self.items.pop(name)
		self.locations[location] = ""
		self.families[family].remove(name)
		