#!/usr/bin/python3
"""Defines a class BaseModelTest"""


import unittest
from models.base import Base


class TestDoctest(unittest.TestCase):
    """Tests for doctest for models/base.py"""

    def test_docstring(self):
        """Checks if docstring is present"""
        self.assertIsNotNone(Base.__doc__)

        