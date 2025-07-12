'''
SEE LICENSE.MD
'''

from utils import db_utils
import config
import tkinter as tk

from modules import menu
from modules import select_path

root = tk.Tk()
root.title(f"Saturn GUI ~ {config._VERSION}")
root.geometry("600x300")

label = tk.Label(root, text="Welcome to Saturn 🌌", font=("Arial", 16))
label.pack(pady=10)




menu_bar = menu.MenuT(root=root)
select_truc = select_path.Select_Path(root=root)

root.mainloop()
