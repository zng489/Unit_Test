#https://blog.finxter.com/python-how-to-import-modules-from-another-folder/

import unittest
from files.functions import add
#import sys

#sys.path.append('/.../Uni_Tests_1/files')

#add(10,20)

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 4), 6)


 
