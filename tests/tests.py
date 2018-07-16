import unittest
import sys
sys.path.append("../")
from lootbag import Lootbag


class lootTest(unittest.TestCase):
	
	@classmethod
	def test_0_setup_class(self):
		self.lootbag = Lootbag()

	def test_1_list_children_bag(self):
		self.assertEqual(set(), self.lootbag.list_children())

	def test_2_add_toy(self):
		self.lootbag.add_toy("ball", "matt")
		self.assertEqual("matt is receiving: ['ball']", self.lootbag.list_childs_loot("matt"))

	def test_3_list_children(self):
		self.assertEqual(set(["matt"]), self.lootbag.list_children())

	def test_4_list_null_childs_loot(self):
		self.assertEqual(None, self.lootbag.list_childs_loot("lucy"))
		
	def test_5_remove_child_toy(self):
		self.lootbag.delete_toy("matt", "ball")
		self.assertEqual(set(["matt"]), self.lootbag.list_children())

	def test_6_remove_all_toys(self):
		self.lootbag.add_toy("ball", "matt")
		self.lootbag.add_toy("legos", "matt")
		self.lootbag.delete_toy("matt", "all")
		self.assertEqual(None, self.lootbag.list_childs_loot("matt"))


if __name__ == '__main__':
	unittest.main()