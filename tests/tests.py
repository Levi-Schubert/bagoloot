import unittest
import sys
sys.path.append("../")
from lootbag import Lootbag


class lootTest(unittest.TestCase):
	
	@classmethod
	def test_0_setup_class(self):
		self.lootbag = Lootbag()

	def test_1_list_uncreated_bag(self):
		with self.assertRaises(FileNotFoundError):
			self.lootbag.list_all()



if __name__ == '__main__':
	unittest.main()