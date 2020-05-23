"""Random testing"""

from generalgui import Page, Button, Label, OptionMenu, Checkbutton, Entry, LabelCheckbutton, LabelEntry, Spreadsheet

import tkinter as tk
import inspect



page = Page()
# page = Page(height=400, width=400)


Label(page, "hello")
OptionMenu(page, ["red", "green", "blue"], "hello")
LabelCheckbutton(page, "yes")
LabelEntry(page, "yes", "write")
Button(page, "Click me", func=page.rainbow)
reset = Button(page, "Reset", func=lambda: page.rainbow(reset=True))
Button(page, "click reset", func=reset.click)


spreadsheet = Spreadsheet(page, cellVSB=True, cellHSB=True)
rows = []
# for _ in range(20):
    # rows.append([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2])
    # rows.append([1, 2, 1, "randoom", 1, 2, 1, 2, 1, 2, 1, 2])


for i in range(20):
    rows.append(["red", "mandera", 9, "red", "mandera", 9, "red", "manderamanderamandera", 9])
    rows.append(["yellow", "nick", 1337, "yellow", "nick", 1337, "yellow", "nick", 1337])

spreadsheet.addRows(rows)

# page.app.widget.update()






# Label(page, "Menu").widget.place(x=100, y=250)

# spreadsheet.headerPage.canvas.widget.xview_scroll(1000, "units")


# page.app.widget.update()
# spreadsheet.syncWidths()


page.show()



