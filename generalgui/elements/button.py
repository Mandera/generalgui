"""Button class that inherits Element"""

import tkinter as tk

from generallibrary.types import strToDynamicType

from generalgui.element import Element


class Button(Element):
    """
    Controls one tkinter Button
    """
    def __init__(self, parentPage, value, func=None, **parameters):
        """
        Create a Button element that controls a button.

        :param generalgui.Page parentPage: Parent page
        :param str value: Text to be displayed
        :param function func: Shortcut for Button.onClick(func)
        """
        super().__init__(parentPage, tk.Button, text=value, cursor="hand2", **parameters)

        self.setBindPropagation("<Button-1>", False)

        self.createStyle("Hover", "<Enter>", "<Leave>", bg="gray90")
        self.createStyle("Click", "<Button-1>", "<ButtonRelease-1>", style="Hover", relief="sunken", fg="gray40")
        self.onClick(func, add=True)

        self.createBind("<Return>", self.click)

    def setValue(self, value):
        """
        Set the value (text) of the button.

        :param str or float or bool or None value:
        """
        self.widget["text"] = str(value)

    def getValue(self):
        """
        Get the value (text) of the button as a dynamic type.
        """
        return strToDynamicType(self.widget["text"])







