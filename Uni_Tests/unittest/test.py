import unittest
from files.functions import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 4), 6)


