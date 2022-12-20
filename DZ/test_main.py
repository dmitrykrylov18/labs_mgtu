import unittest
from main import fibonacci
import unittest
import main

class TestEquation(unittest.TestCase):

    def test_get_roots(self):
        self.assertEqual(list(fibonacci(5)),[0, 1, 1, 2, 3])

    def test_value(self):
        self.assertEqual(list(fibonacci(7)),[0, 1, 1, 2, 3, 5, 8])

    def test_name(self):
        self.assertEqual(list(fibonacci(10000000)), ['Параметр слишком большой! (> 1000000)'])

if __name__ == '__main__':
    assert (list(main.fibonacci(3)) == [0, 1, 1])
    assert (list(fibonacci(4)) == [0, 1, 1, 2])
    assert (list(fibonacci(5)) == [0, 1, 1, 2, 3])
    unittest.main()
