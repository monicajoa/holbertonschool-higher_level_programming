#!/usr/bin/python3
    """Unittest for 3. Square class
    """
import unittest
import os
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Square(unittest.TestCase):
    """Test Square

    Arguments:
        unittest {[class]} -- class with unittests for Square class
    """
    def test_pep8_style(self):
        """Test PEP8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0)

if __name__ == "__main__":
    unittest.main()
