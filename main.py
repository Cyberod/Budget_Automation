from src.cli.cli import run_cli
from src.gui.gui import run_gui

import sys



def main():
    print(" 💰 Welcome to the Budget Automation System! 💰")
    print("1. Graphical User Interface")
    print("2. Command Line Interface")
    print("3. type 'quit' to Exit")
    
    choice = input("Choose interface (1/2): ")
    
    if choice == "1":
        run_gui()
    elif choice == "2":
        run_cli()  # run the system in the command line

    elif choice == "quit":
        print("Thank you for Using Budget Automation. Goodbye! 👋")
        sys.exit(0) # Quit the System

    else:
        print("Invalid choice. Please restart and select either 1 or 2.")
        sys.exit(1)

if __name__ == "__main__":
    main()

