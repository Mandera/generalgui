"""Element for generalgui, controls a widget that's not App or Page"""

import tkinter as tk
import inspect
from generallibrary.types import typeChecker
from generallibrary.iterables import addToListInDict
from generalgui.shared_methods.element_page import Element_Page
from generalgui.shared_methods.element_page_app import Element_Page_App

class Element(Element_Page, Element_Page_App):
    """
    Element is inherited by all tkinter widgets exluding App and Page.
    Shown by default. So when it's page is shown then all of page's children are shown automatically.
    """
    def __init__(self, parentPage, widget, side="top"):
        typeChecker(parentPage, Page)

        super().__init__(parentPage, widget, side)

        self.pack()
        self.events = {}

    def _bind(self, key, func, add):
        """
        Binds a key to a function using tkinter's bind function.
        Not used directly.

        :param str key: A key from https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        :param function func: A function to be called
        :param bool add: Add to existing binds instead of overwriting
        :return:
        """
        if func is None:
            self.widget.unbind("<Button-1>")
            if key in self.events:
                del self.events[key]
        else:
            eventParameter = False
            for _, value in inspect.signature(func).parameters.items():
                if value.default is inspect.Parameter.empty:
                    eventParameter = True
                break
            if not eventParameter:
                oldFunc = func
                func = lambda _: oldFunc()

            if add:
                addToListInDict(self.events, key, func)
            else:
                self.events[key] = [func]
            self.widget.bind(key, func, add=add)

    def _callBind(self, key):
        """
        Calls a binded key's function(s) manually.
        Not used directly.

        :param str key: A key from https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        :return: Function's return value or functions' return values in tuple in the order they were binded.
        """
        if key not in self.events:
            return None

        # Event is None when calling manually
        results = tuple(func(None) for func in self.events[key])
        if len(results) == 1:
            return results[0]
        else:
            return results

    def onClick(self, func, add=False):
        """
        Call a function when this element is left clicked.

        :param function or None func: Any function or None to unbind
        :param add: Whether to add to functions list or replace all
        """
        self._bind("<Button-1>", func, add)
    def click(self):
        """Manually call the function that is called when this element is left clicked."""
        return self._callBind("<Button-1>")

    def onRightClick(self, func, add=False):
        """
        Call a function when this element is right clicked.

        :param function or None func: Any function or None to unbind
        :param add: Whether to add to functions list or replace all
        """
        self._bind("<Button-3>", func, add)
    def rightClick(self):
        """Manually call the function that is called when this element is right clicked."""
        return self._callBind("<Button-3>")

class Text(Element):
    """Controls one tkinter Label"""
    def __init__(self, page, text):
        """
        Create a Text element that controls a label.

        :param Page page: Parent page
        :param str text: Text to be displayed
        """
        typeChecker(page, Page)

        self.text = text
        widget = tk.Label(page.widget, text=text)

        super().__init__(page, widget)

class Button(Element):
    """
    Controls one tkinter Button
    """
    def __init__(self, page, text, func=None):
        """
        Create a Button element that controls a button.

        :param Page page: Parent page
        :param str text: Text to be displayed
        :param function func: Shortcut for Button.onClick(func)
        """
        typeChecker(page, Page)

        self.text = text
        widget = tk.Button(page.widget, text=text)

        super().__init__(page, widget)

        self.onClick(func)


from generalgui.page import Page
































