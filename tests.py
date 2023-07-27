from main import *
import os
import sys
import unittest
sys.path.append(os.getcwd())


class Test1(unittest.TestCase):
    def test_1_returns_integer(self):
        self.assertEqual(nitro_salt(1000), 10)


if __name__ == '__main__':
    unittest.main()
