# -*- coding: UTF-8 -*-
"""
  Author:  Jacek Kotlarski --<szumak@virthost.pl>
  Created: 08.05.2023

  Purpose:
"""

import unittest
import inspect

from raisetool.formatter import Raise


class TestRaise(unittest.TestCase):
    """Tests for Raise class."""

    def test_create_class_instance(self):
        """Test nr 1."""
        obj = Raise()
        self.assertTrue(obj, Raise)

    def test_returning_message_from_instance(self):
        """Test nr 2."""
        obj = Raise()
        self.assertEqual(obj.message("test"), "test")
        self.assertEqual(
            obj.message("test", self.__class__.__name__), "TestRaise: test"
        )
        self.assertEqual(
            obj.message(
                "test",
                class_name=self.__class__.__name__,
                currentframe=inspect.currentframe(),
            ),
            "TestRaise.test_returning_message_from_instance [line:31]: test",
        )

    def test_returning_message_from_class(self):
        """Test nr 3."""
        self.assertEqual(Raise.message("test"), "test")
        self.assertEqual(
            Raise.message("test", self.__class__.__name__), "TestRaise: test"
        )
        self.assertEqual(
            Raise.message(
                "test",
                class_name=self.__class__.__name__,
                currentframe=inspect.currentframe(),
            ),
            "TestRaise.test_returning_message_from_class [line:46]: test",
        )

    def test_returning_attribute_error(self):
        """Test nr 4."""
        self.assertIsInstance(Raise.attribute_error("test"), AttributeError)


# #[EOF]#######################################################################
