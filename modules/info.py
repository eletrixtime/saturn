import tkinter as tk
from tkinter import filedialog, messagebox
import config,os
from utils import db_utils

class InfoF:

    def __init__(self, root):
        self.root = root
        
        self.title_hb = tk.Entry()
        self.title_hb.insert(0,"My very cool homebrew")

        self.path_on_sd = tk.Entry()
        self.path_on_sd.insert(0,"/vp_mnt/sd/YOURPATH")

        self.title_hb.pack(pady=5)
        self.path_on_sd.pack(pady=3)

        self.applybtn = tk.Button(text="Apply",command=self.apply)
        self.applybtn.pack()

        
        # ====

        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        self.uniteid_label = tk.Label(self.bottom_frame,text=f"UnitEID: {db_utils.Find_UnitEID(config._DB_PATH)}")
        self.uniteid_label.pack(side=tk.LEFT)


    def apply(self):
        hb_tt = self.title_hb.get()
        config.TEMP["l_title"] = hb_tt
        config.TEMP["l_path"] = self.path_on_sd.get()
        db_utils.add_homebrew(config.TEMP["l_path"],db_utils.Find_UnitEID(config._DB_PATH),config.TEMP["l_title"])
