import re
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
name_label = ttk.Label(frame, text="Введите имя")
name_label.pack(anchor=NW)

name_entry = ttk.Entry(frame)
name_entry.pack(anchor=NW)

frame.pack(anchor=NW, fill=X, padx=5, pady=5)

root.mainloop()