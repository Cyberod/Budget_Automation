import tkinter as tk
from tkinter import ttk, font

import sys


def run_gui():
    root = tk.Tk()
    root.title("Budget Automation System")
    root.geometry("600x400")

    # Centers the window on screen
    window_width = 600
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Welcome Message
    welcome_frame = ttk.Frame(root, padding="20")
    welcome_frame.pack(expand=True, fill='both')

    title_label = ttk.Label(
        welcome_frame,
        text = "💰 Welcome to the Budget Automation System! 💰",
        font = ('Arial', 16, 'bold')
    )
    title_label.pack(pady=20)

    # Interface selection buttons
    button_frame = ttk.Frame(welcome_frame)
    button_frame.pack(pady=20)

    gui_btn = ttk.Button(
        button_frame,
        text="Graphical User Interface",
        command=lambda: start_gui(root)
    )
    gui_btn.pack(pady=10)

    cli_btn = ttk.Button(
        button_frame,
        text="Command Line Interface",
        command=lambda: switch_to_cli(root)
    )
    cli_btn.pack(pady=10)

    root.mainloop()

def start_gui(root):
    # Clear the welcome screen
    for widget in root.winfo_children():
        widget.destroy()
    
    # Here the next GUI screen comes up(Budget plan selection)
    # I will Implement this in the next step


def switch_to_cli(root):
    root.destroy()  # Close the GUI window
    sys.exit(0)  # Exit cleanly