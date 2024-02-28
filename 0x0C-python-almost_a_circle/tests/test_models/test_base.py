#!/usr/bin/python3
"""Defines a class BaseModelTest"""


import unittest
import models.base


class TestDoctest(unittest.TestCase):
    """Tests for doctest for models/base.py"""

    def test_docstring(self):
        """Checks if docstring is present"""
        self.assertIsNotNone(models.base.__doc__)

        