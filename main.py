from cli import run_cli
from gui import run_gui


def main():
    print("💰 Welcome to the Budget Automation System! 💰")
    print("1. Command Line Interface")
    print("2. Graphical User Interface")
    
    choice = input("Choose interface (1/2): ")
    
    if choice == "2":
        run_gui()
    else:
        run_cli()  # Your existing command-line interface

if __name__ == "__main__":
    main()

