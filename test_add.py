import unittest

from add import add


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
