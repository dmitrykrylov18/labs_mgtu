import unittest
from main2 import *

task1_result = [('MacOs-ов', 'Игровой компьютер'), ('Harmony-ов', 'Рабочий компьютер'), ('(Linux) Kali-ов', 'Офисный ноутбук')]
task2_result = [('Игровой компьютер', 28000), ('Рабочий компьютер', 26500), ('Офисный ноутбук', 16000)]
task3_result = {'Игровой компьютер': ['MacOs-ов', 'Windows']}

class TestEquation(unittest.TestCase):
	def test_check_task1(self):
		self.assertEqual(task1_result, task1())

	def test_check_task2(self):
		self.assertEqual(task2_result, task2())

	def test_check_task3(self):
		self.assertEqual(task3_result, task3())

if __name__ == '__main__':
	unittest.main()


