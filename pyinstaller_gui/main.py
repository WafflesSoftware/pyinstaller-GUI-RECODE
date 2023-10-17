from tkinter import filedialog
import customtkinter as ctk
import tkinter as tk
# import pyinstaller
import time
import os

system = None

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.option_1 = None
        self.file = None
        
        self.r = tk.IntVar()
        self.r.set(1)

        self.title("pyinstaller-GUI")
        self.geometry("522x225")
        self.resizable(False, False)

        self.lbl_title = ctk.CTkLabel(self, text="pyinstaller-GUI", font=("Arial", 20))
        self.lbl_title.grid(row=1)

        self.lbl_name = ctk.CTkLabel(self, text="Name:", font=("Arial", 15))
        self.lbl_name.grid(row=2, padx=3, sticky="w")

        self.ent_name = ctk.CTkEntry(self, placeholder_text="Name", height=25)
        self.ent_name.grid(row=2, sticky="w", padx=50, pady=3)

        self.lbox_file = tk.Listbox(self, height=1, width=62, bd=0, state="disabled")
        self.lbox_file.grid(row=3, padx=3, sticky="w")

        self.btn_select_file = ctk.CTkButton(self, text="Select file", command=self.open_file)
        self.btn_select_file.grid(row=3, column=1, pady=3, sticky="w")

        self.file_note = ctk.CTkLabel(self, text="Note: The EXE-file will be generated here as well!", text_color="red")
        self.file_note.grid(row=4, padx=3, sticky="w")

        self.para_lbl = ctk.CTkLabel(self, text="Parameters", font=("Arial", 17))
        self.para_lbl.grid(row=5)

        self.rbtn_onedir = ctk.CTkRadioButton(self, variable=self.r, text="Create a one-folder bundle containing an exec"
                                                            "utable (default)", value=1)
        self.rbtn_onedir.grid(row=6, padx=3, sticky="w")

        self.rbtn_onefile = ctk.CTkRadioButton(self, variable=self.r, text="One-file bundled executable", value=2)
        self.rbtn_onefile.grid(row=7, padx=3, sticky="w")

        self.btn_export = ctk.CTkButton(self, text="Export", command=self.run)
        self.btn_export.grid(row=8, ipadx=30)

    def open_file(self):    
        self.file = filedialog.askopenfilename(title="Select file...")

        self.lbox_file.config(state="normal")
        self.lbox_file.insert(tk.END, self.file)
        self.lbox_file.config(state="disabled")

    def run(self):
        if self.file is None:
            print("You haven't selected any file yet!")
        else:
            pass

        if self.r.get() == 1:
            self.option_1 = "-D"
        elif self.r.get() == 2:
            self.option_1 = "-F"

        os.chdir(os.path.dirname(self.file))
        os.system(f'pyinstaller {self.option_1} -n "{self.ent_name.get()}" {os.path.basename(self.file)}"')


if __name__ == "__main__":
    os.system("check_os.py")

    read_os = open("system", "r")
    system = read_os.read()
    read_os.close()

    if system == "Windows":
        print(f"Operating system supported! ({system})")
    else:
        print(f"Operating system not supported! ({system})")
        print("\nQuitting in 3 seconds!")
        time.sleep(3)
        exit()

    app = App()
    app.mainloop()
