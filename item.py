
class Item():
	def __init__(self, name, toy):
		self.child = name
		self.toys = []
		self.toys.append(toy)
		self.delivered = False

	def add_toy(self, toy):
		if(self.find_toy(toy) == -1):
			self.toys.append(toy)

	def remove_toy(self, toy):
		index = self.find_toy(toy)
		if(index != -1):
			del self.toys[index]
		else:
			print("Toy does not exist | nothing removed.")
	
	def find_toy(self, find):
		for index, toy in enumerate(self.toys):
			if toy == find:
				return index
		return -1

	def deliver(self):
		self.delivered = True

	def get_name(self):
		return self.child

	def stringified(self):
		if(self.delivered):
			return f'{self.child} has received: {str(self.toys)}'
		else:
			return f'{self.child} is receiving: {str(self.toys)}'

	def __str__(self):
		return (f'{self.child} is receiving: {str(self.toys)}')
				