"""Tests for Button"""
import tkinter as tk
import unittest

from generalgui import Page, Button


class ButtonTest(unittest.TestCase):
    def test_button(self):
        for page in Page(), Page(width=200):
            button = Button(page, "hello", lambda: 5)
            self.assertEqual(button.parentPage, page)
            self.assertIs(button.widget.element, button)
            self.assertFalse(button.isShown())

            button.show(mainloop=False)
            self.assertTrue(button.isShown())

            self.assertEqual(button.click(), 5)

            page.app.remove()
            self.assertRaises(tk.TclError, button.isShown)

    def test_value(self):
        button = Button(Page(), "start")
        self.assertEqual("start", button.getValue())

        button.setValue("changed")
        self.assertEqual("changed", button.getValue())

        button.setValue("")
        self.assertEqual("", button.getValue())

        button.setValue(True)
        self.assertIs(True, button.getValue())

        button.setValue(None)
        self.assertIs(None, button.getValue())



