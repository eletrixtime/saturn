import tkinter as tk
from tkinter import messagebox
import config

class MenuT():
    def about(self):
        messagebox.askyesnocancel(f"Saturn@{config._VERSION}","Saturn is a open-source project, \n available at : ")

    def __init__(self,root):
        menubar = tk.Menu(root) 

        MENU_files = tk.Menu(menubar, tearoff=0)
        MENU_files.add_command(label="Quit", command=lambda:exit())

        menubar.add_cascade(label="Files", menu=MENU_files)

        aide_menu = tk.Menu(menubar, tearoff=0)
        aide_menu.add_command(label="About Saturn", command=self.about)
        menubar.add_cascade(label="Help", menu=aide_menu)
        root.config(menu=menubar)

