import tkinter as tk
from .windows import WelcomeWindow


def run_gui():
    root = tk.Tk()
    WelcomeWindow(root)
    root.mainloop()