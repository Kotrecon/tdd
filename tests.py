from main import *
import os
import sys
import unittest
sys.path.append(os.getcwd())


class TestNitroSalt(unittest.TestCase):
    def test_nitro_salt_returns_masss(self):
        self.assertEqual(nitro_salt(1000), 10)
        self.assertEqual(nitro_salt(1500), 15)
        self.assertEqual(nitro_salt(8000), 80)

    def test_nitro_salt_returns_integer(self):
        self.assertIsInstance(nitro_salt(1000), int)


if __name__ == '__main__':
    unittest.main()
