#!/usr/bin/python3
import datetime
import json
from Inventory import *

def create():
	global inv
	print("CREATING ITEM")
	name = input("ENTER NAME: ")
	location = input("ENTER LOCATION: ")
	family = input("ENTER FAMILY: ")
	quantity = int(input("ENTER QUANTITY: "))
	quant_need = int(input("ENTER QUANTITY NEEDED: "))
	desc = input("ENTER DESCRIPTION: ")
	inv.create_item(name, location, family, quantity, quant_need, desc)


def delete():
	global inv
	print("DELETING ITEM")
	name = input("ENTER NAME: ")
	del_item = inv.search_item(name)
	if del_item != None:
		confirmation = input("CONFIRM DELETE? (y/N): ")
		if confirmation.lower() == "y":
			inv.delete_item(del_item)
	else:
		print("ITEM NOT FOUND")


def use():
	global inv
	name = input("ENTER NAME: ")
	item = inv.search_item(name)
	if item != None:
		current_amt = item["quantity"]
		print("CURRENT QUANTITY: {0}".format(current_amt))
	number = int(input("ENTER AMT USED: "))


def process_command(cmd):
	global inv
	cmd_array = cmd.split(" ")
	if len(cmd_array) == 1:
		# Step by step
		pass
	else:
		pass
	return 0


inv = Inventory()


if __name__ == '__main__':
	inv.load_json("inventory.json")
	cmd = ""
	#'''
	cont = True
	while cont:
		cmd = input("Enter Command: ")
		# FILL THIS OUT BETTER LATER
		if cmd == "create":
			create()
		elif cmd == "delete":
			delete()
		elif cmd == "use":
			use()
		elif cmd == "add":
			pass
		else:
			cont = process_command(cmd)
		
	#'''
	
	inv.save_json("inventory.json")
