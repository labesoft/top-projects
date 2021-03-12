"""Tests of the address book
-----------------------------

About this module
-----------------
This module test the main functionalities of the address book application
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-09"
__copyright__ = "Copyright 2021, Benoit Lapointe"
__version__ = "1.0.0"

from unittest import TestCase
from unittest.mock import MagicMock, call, patch

import addbook
from addbook.__main__ import (
    add_contact, contactlist, delete, edit, get_selection_index,
    reset, select_set, view
)


class TestAddBook(TestCase):
    def setUp(self) -> None:
        addbook.__main__.name = MagicMock()
        addbook.__main__.number = MagicMock()
        addbook.__main__.select = MagicMock()
        self.selection = contactlist[0]

    def test_add_contact(self):
        """Test if the test contact was added"""
        # Prepare test
        addbook.__main__.name.get.return_value = self._testMethodName
        addbook.__main__.number.get.return_value = self._testMethodName

        # Run test
        add_contact()

        # Evaluate test
        self.assertIn([self._testMethodName, self._testMethodName], contactlist)

    @patch("addbook.__main__.get_selection_index", return_value=0)
    def test_delete(self, gsi):
        """Test if the selection was edited"""
        # Run test
        delete()

        # Evaluate test
        self.assertNotIn(self.selection, contactlist)

    @patch("addbook.__main__.get_selection_index", return_value=0)
    def test_edit(self, gsi):
        """Test if the selection was edited"""
        # Prepare test
        addbook.__main__.name.get.return_value = self._testMethodName
        addbook.__main__.number.get.return_value = self._testMethodName
        previous_contact = contactlist[0]

        # Run test
        edit()

        # Evaluate test
        self.assertNotIn(previous_contact, contactlist)
        self.assertIn([self._testMethodName, self._testMethodName], contactlist)

    def test_reset(self):
        """Test is the field reset to empty string"""
        # Run test
        reset()

        # Evaluate test
        calls = [
            call.set("")
        ]
        addbook.__main__.name.assert_has_calls(calls)
        addbook.__main__.number.assert_has_calls(calls)


    def test_select_set(self):
        """Test if the select set is sorted"""
        # Run test
        select_set()

        # Evaluate test
        self.assertEqual(sorted(contactlist), contactlist)

    def test_selection_index(self):
        # Run test
        selection_index = get_selection_index()

        # Evaluate test
        self.assertEqual(1, selection_index)

    def test_view(self):
        # Run test
        view()

        # Evaluate test
        calls = [
            call.set(contactlist[1][0])
        ]
        addbook.__main__.name.assert_has_calls(calls)
        calls = [
            call.set(contactlist[1][1])
        ]
        addbook.__main__.number.assert_has_calls(calls)
