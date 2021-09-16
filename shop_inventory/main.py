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
	inv.create_item(name, location, family, quantity)


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
	# Daisy Chain of Death
	global inv
	cmd = cmd.lower()
	cmd_array = cmd.split(" ")
	if len(cmd_array) == 1:
		# Step by step
		if cmd == "exit":
			return False
		elif cmd == "create":
			create()
		elif cmd == "delete":
			delete()
		elif cmd == "use":
			use()
		elif cmd == "add":
			pass
		elif cmd == "search":
			pass
		# End if block
	else:
		# Speedy commands
		if cmd_array[0] == "create":
			name = cmd_array[1]
			location = cmd_array[2]
			if len(cmd_array) > 3:
				family = cmd_array[3]
			else:
				family = input("ENTER FAMILY: ").lower()
			if len(cmd_array) > 4:
				quantity = int(cmd_array[4])
			else:
				quantity = int(input("ENTER QUANTITY: "))
			inv.create_item(name, location, family, quantity)

		elif cmd_array[0] == "delete":
			name = cmd_array[1]
			del_item = inv.search_item(name)
			if del_item != None:
				if cmd_array[2] == "-y":
					inv.delete_item(del_item)
				else:
					confirmation = input("CONFIRM DELETE? (y/N): ")
					if confirmation.lower() == "y":
						inv.delete_item(del_item)
					else:
						print("ITEM NOT FOUND")

		elif cmd_array[0] == "search":
			item = inv.search_item(cmd_array[1].lower())
		elif cmd_array[0] == "use":
			pass
		elif cmd_array[0] == "add":
			pass
		elif cmd_array[0] == "move":
			pass
		elif cmd_array[0] == "mod":
			pass

	return True


inv = Inventory()


if __name__ == '__main__':
	inv.load_json("inventory.json")
	cont = True
	while cont:
		cmd = input("Enter Command: ").lower()
		cont = process_command(cmd)

	inv.save_json("inventory.json")
