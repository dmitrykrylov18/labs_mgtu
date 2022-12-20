import unittest
from equetion import get_roots

class TestEquation(unittest.TestCase):
	def test_calculate(self):
		self.assertEqual(get_roots(1.0, -10.0, 9.0), [-3.0, -1.0, 1.0, 3.0])
		self.assertEqual(get_roots(-4.0, 16.0, 0.0), [-2.0, 0.0, 2.0])
		self.assertEqual(get_roots(431.0, -123.0, 665.0), [])

	def test_value(self):
		self.assertRaises(ValueError, get_roots(0.0, 0.0, 9.0))

	def test_type(self):
		self.assertRaises(TypeError, get_roots(12.0, "B", 4.0))

if __name__ == '__main__':
	unittest.main()

