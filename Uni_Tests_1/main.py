'''
#https://blog.finxter.com/python-how-to-import-modules-from-another-folder/

import unittest
from files.functions import add
#import sys

#sys.path.append('/.../Uni_Tests_1/files')
if __name__ == '__main__':
    print(add(10,20))
    unittest.main()

python -m unittest test.py    
'''