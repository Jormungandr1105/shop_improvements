import time
import json
from Inventory import *



locations = {}



if __name__ == '__main__':
	inv = Inventory()
	inv.load_json("inventory.json")
	inv.save_json("inventory.json")
