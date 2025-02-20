import tkinter as tk
from tkinter import ttk
from src.core.storage import load_budget_plans

class WelcomeWindow:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        self.root.title("Budget Automation System")
        # Centers the window on screen
        window_width = 600
        window_height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}') 

    def create_widgets(self):
        # The Welcome Frame
        self.welcome_frame = ttk.Frame(self.root, padding="20")
        self.welcome_frame.pack(expand=True, fill='both')
        
        # Title
        title_label = ttk.Label(
            self.welcome_frame,
            text="💰 Welcome to the Budget Automation System! 💰",
            font=('Arial', 16, 'bold')
        )
        title_label.pack(pady=20)
        
        # Buttons
        button_frame = ttk.Frame(self.welcome_frame)
        button_frame.pack(pady=20)
        
        gui_btn = ttk.Button(
            button_frame,
            text="Graphical User Interface",
            command=self.start_gui
        )
        gui_btn.pack(pady=10)
        
        cli_btn = ttk.Button(
            button_frame,
            text="Command Line Interface",
            command=self.switch_to_cli
        )
        cli_btn.pack(pady=10)  

    def start_gui(self):
        self.welcome_frame.destroy()
        PlanSelectionWindow(self.root)
    
    def switch_to_cli(self):
        self.root.destroy()
        import sys
        sys.exit(0) 



class PlanSelectionWindow:
    def __init__(self, root):
        self.root =root
        self.create_widgets()

    def create_widgets(self):
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(expand=True, fill='both')

        # Title
        title_label = ttk.Label(
            self.main_frame,
            text = "Choose Your Budget Plan",
            font = ('Arial', 14, 'bold')

        )

        title_label.pack(pady=10)

        # Frame for the plans
        self.create_plans_frame()

    def create_plans_frame(self):
        plans_frame = ttk.Frame(self.main_frame)
        plans_frame.pack(pady=20)

        # Predefined plans
        predefined_plans = [
            ("Conservative (50-30-20)", "50-30-20"),
            ("Moderate (60-20-20)", "60-20-20"),
            ("Aggressive (70-10-20)", "70-10-20")
        ]

        for plan_name, plan_id in predefined_plans:
            btn = ttk.Button(
                plans_frame,
                text = plan_name,
                command=lambda p=plan_id: self.select_predefined_plan(p)

            )
            btn.pack(pady=5)

        # Custom Plans Section
        saved_plans = load_budget_plans()

        if saved_plans:
            ttk.Separator(plans_frame).pack(pady=10, fill='x')
            custom_label = ttk.Label(
                plans_frame,
                text = "Custom Plans:",
                font = ('Arial', 11, 'bold')
            )
            custom_label.pack(pady=5)

            for plan_name in saved_plans.keys():
                btn = ttk.Button(
                    plans_frame,
                    text = plan_name,
                    command=lambda p=plan_name: self.select_custom_plan(p)

                )
                btn.pack(pady=5)

        # Create new Plan Section
        ttk.Separator(plans_frame).pack(pady=10, fill='x')
        create_btn = ttk.Button(
            plans_frame,
            text = "Create New Custom Plan",
            command = self.create_custom_plan
        )
        create_btn.pack(pady=10)

    def select_predefined_plan(self, plan_id):
        # Creates predefined plan mappings
        predefined_plans = {
            "50-30-20": {
                "Needs": 50,
                "Wants": 30,
                "Savings": 20
            },
            "60-20-20": {
                "Needs": 60,
                "Wants": 20,
                "Savings": 20
            },
            "70-10-20": {
                "Needs": 70,
                "Wants": 10,
                "Savings": 20
            }
        }
        
        # Clears current screen
        self.main_frame.destroy()
        # Launches amount input window with selected plan(s)
        AmountInputWindow(self.root, predefined_plans[plan_id])

    def select_custom_plan(self, plan_name):
        saved_plans = load_budget_plans()
        selected_plan = saved_plans[plan_name]
        
        # Clears current screen
        self.main_frame.destroy()
        # Launches amount input window with selected custom plan
        AmountInputWindow(self.root, selected_plan)

    def create_custom_plan(self):
        # Clears current screen
        self.main_frame.destroy()
        # Launches custom plan creation window
        CustomPlanWindow(self.root)



class AmountInputWindow:
    def __init__(self, root, selected_plan):
        self.root = root
        self.plan = selected_plan
        self.create_widgets()
    
    def create_widgets(self):
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(expand=True, fill='both')
        
        title_label = ttk.Label(
            self.main_frame,
            text="Enter Total Budget Amount",
            font=('Arial', 14, 'bold')
        )
        title_label.pack(pady=10)
        
        # Amount entry field
        self.amount_var = tk.StringVar()
        amount_entry = ttk.Entry(
            self.main_frame,
            textvariable=self.amount_var
        )
        amount_entry.pack(pady=10)
        
        # Continue button
        continue_btn = ttk.Button(
            self.main_frame,
            text="Continue",
            command=self.process_amount
        )
        continue_btn.pack(pady=10)

class CustomPlanWindow:
    def __init__(self, root):
        self.root = root
        self.create_widgets()
    
    def create_widgets(self):
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(expand=True, fill='both')
        
        title_label = ttk.Label(
            self.main_frame,
            text="Create Custom Budget Plan",
            font=('Arial', 14, 'bold')
        )
        title_label.pack(pady=10)


