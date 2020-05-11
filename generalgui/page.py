"""App for generalgui, controls Frame"""

from generallibrary.types import typeChecker
import tkinter as tk
from generalgui.shared_methods.element_page_app import Element_Page_App
from generalgui.shared_methods.element_page import Element_Page
from generalgui.shared_methods.page_app import Page_App

class Page(Element_Page, Element_Page_App, Page_App):
    """
    Controls one tkinter Frame and adds a lot of convenient features.
    Hidden by default.
    """
    def __init__(self, parentPage=None, side="top", removeSiblings=False):
        typeChecker(parentPage, (None, Page, App))

        if parentPage is None:
            parentPage = App()
        elif removeSiblings:
            parentPage.removeChildren()

        widget = tk.Frame(parentPage.widget)
        super().__init__(parentPage, widget, side)



from generalgui.app import App


