import warnings, unittest
from src.folder_1.folder_python import add


class SpecialTest(unittest.TestCase):
    def test_add(self):
        result = add(9,6)
        self.assertEqual(result, 18)

