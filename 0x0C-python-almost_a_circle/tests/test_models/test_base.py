#!/usr/bin/python3
"""Unittest for 1. Base class
    """
import unittest
import os
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """Test Base

    Arguments:
        unittest {[class]} -- class with unittests for Base class
    """

    def test_pep8_style(self):
        """Test PEP8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base.py"])
        self.assertEqual(result.total_errors, 0)


if __name__ == "__main__":
    unittest.main()
