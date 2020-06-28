"""
Unit test for add module
"""

import unittest

from add import add


class AddTestCase(unittest.TestCase):
    """
        Test case for add function
    """
    def test_add(self):
        """
        Check a simple addition with add function
        """
        self.assertEqual(add(2, 2), 5)


if __name__ == '__main__':
    unittest.main()
