import unittest
from htmlgenerator import * 

class TestName(unittest.TestCase):
	def test_name(self):
		self.assertAlmostEqual(check_user_name("Stepan"),1)

