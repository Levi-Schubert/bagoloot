from sys import argv
import os.path
import pickle
from item import Item

class Lootbag():
	
	def __init__(self):
		if os.path.exists("./lootbag.file"):
			with open("./lootbag.file" , "rb") as loot:
				self.items = pickle.load(loot)
		else:
			self.items = []

	def add_toy(self, toy, name):
		index = self.find_existing_index(name)
		if index != -1:
			self.items[index].add_toy(toy)
		else:
			self.items.append(Item(name, toy))
		self.write_to_file()

	def write_to_file(self):
		with open("./lootbag.file", "wb") as loot:
			pickle.dump(self.items, loot, pickle.HIGHEST_PROTOCOL)

	def delete_toy(self, name, toy):
		index = self.find_existing_index(name)
		if index != -1:
			if toy == "all":
				del self.items[index]
			else:
				self.items[index].remove_toy(toy)
		self.write_to_file()

	def find_existing_index(self, name):
		for index in range(0, len(self.items)):
			if name == self.items[index].get_name():
				return index
		return -1

	def list_children(self):
		list = {item.get_name() for item in self.items}
		print(list)

	def list_childs_loot(self, name):
		index = self.find_existing_index(name)
		if index != -1:
			print(self.items[index].stringified())

	def deliver_toy_to_child(self, name):
		index = self.find_existing_index(name)
		if index != -1:
			self.items[index].deliver()
			self.write_to_file()

def main(args, bag):
	if len(args) == 1: 
		print("This program requires command line arguments | type help for available commands")
	else:
		if args[1].upper() == "HELP":
			print("available commands:")
			print("add [toy] [child]    | adds a toy to the bag of loot for the given child")
			print("remove [child] [toy] | removes a toy from the bag for the child specified | [all] can be used instead of toy to remove all toys")
			print("ls                   | prints all a lists of all children currently receiving presents")
			print("ls [child]           | prints the toys in the bag for a specific child")
			print("delivered [child]    | mark a childs toys as delivered")
			print("help                 | prints this list")
		elif args[1].upper() == "ADD":
			if len(args) != 4:
				print('Incorrect arguments | type "help" for correct syntax')
			else:
				bag.add_toy(args[2], args[3])
		elif args[1].upper() == "REMOVE":
			if len(args) != 4:
				print('Incorrect arguments | type "help" for correct syntax')
			else:
				bag.delete_toy(args[2], args[3])
		elif args[1].upper() == "LS":
			if len(args) == 3:
				bag.list_childs_loot(args[2])
			else:
				bag.list_children()
		elif args[1].upper() == "DELIVERED":
			if len(args) != 3:
				print('Incorrect arguments | type "help" for correct syntax')
			else:
				bag.deliver_toy_to_child(args[2])
		else:
			print(f'{args[1]} not a valid command | use "help" for a list of available commands')


main(argv, Lootbag())