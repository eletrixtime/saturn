import tkinter as tk
from tkinter import filedialog,messagebox
import config, os,shutil
from utils import db_utils

class Select_Path:

    def __init__(self, root):
        self.root = root
        self.select_label = tk.Label(root, text="Please select the path where the .db is located.", font=("Arial", 10))
        self.select_label.pack(pady=10)
        self.btn = tk.Button(root, text="Select", command=self.open_folder_dialog)
        self.btn.pack(pady=20)


    def open_folder_dialog(self):
        path = filedialog.askdirectory()  
        if path:
            for i in os.listdir(path):
                if i == "Innopad_wf.db":
                    from modules import info

                    print(f"[Saturn] : DB Found at : {path}/Innopad_wf.db")
                    config._DB_PATH = path + "/Innopad_wf.db"
                    self.btn.destroy()
                    self.select_label.destroy()
                    print(f"[Saturn] : UnitEID is {db_utils.Find_UnitEID(config._DB_PATH)}")
                    print("[Saturn] : Backuping the DB")
                    shutil.copy(config._DB_PATH,path+"/Innopad_wf.bak")
                    info = info.InfoF(root=self.root)
                    
                    return
            print("[Saturn] : Not DB found")
            messagebox.askokcancel("Error","No DB Found")
            return

        else:
            print("no_folder_selected")

