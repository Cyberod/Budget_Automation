import tkinter as tk
from tkinter import ttk, messagebox
from plan import get_custom_plan
from calculations import calculate_category_amounts
from storage import load_budget_plans, save_budget_plan
from subcategories import get_subcategories

class BudgetApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Budget Automation System")
        self.geometry("800x600")
        
        # Main container
        self.main_frame = ttk.Frame(self, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Amount Entry
        ttk.Label(self.main_frame, text="Enter Total Amount ($):").grid(row=0, column=0, pady=10)
        self.amount_entry = ttk.Entry(self.main_frame)
        self.amount_entry.grid(row=0, column=1)
        
        # Budget Plan Selection
        ttk.Label(self.main_frame, text="Select Budget Plan:").grid(row=1, column=0, pady=10)
        self.plan_var = tk.StringVar()
        self.plan_combo = ttk.Combobox(self.main_frame, textvariable=self.plan_var)
        self.update_plan_options()
        self.plan_combo.grid(row=1, column=1)
        
        # Calculate Button
        ttk.Button(self.main_frame, text="Calculate Budget", 
                  command=self.calculate_budget).grid(row=2, column=0, columnspan=2, pady=20)
        
        # Results Display
        self.result_text = tk.Text(self.main_frame, height=15, width=60)
        self.result_text.grid(row=3, column=0, columnspan=2, pady=10)

    def update_plan_options(self):
        saved_plans = load_budget_plans()
        options = [
            "Conservative (50-30-20)",
            "Moderate (60-20-20)",
            "Aggressive (70-10-20)",
            "Create Custom Plan"
        ] + list(saved_plans.keys())
        self.plan_combo['values'] = options
        self.plan_combo.set(options[0])

    def calculate_budget(self):
        try:
            total_amount = float(self.amount_entry.get())
            if total_amount <= 0:
                messagebox.showerror("Error", "Amount must be greater than zero")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
            return

        plan_choice = self.plan_var.get()
        
        if plan_choice == "Conservative (50-30-20)":
            budget_plan = {"Expenses": 50, "Investment": 30, "Savings": 20}
        elif plan_choice == "Moderate (60-20-20)":
            budget_plan = {"Expenses": 60, "Investment": 20, "Savings": 20}
        elif plan_choice == "Aggressive (70-10-20)":
            budget_plan = {"Expenses": 70, "Investment": 10, "Savings": 20}
        elif plan_choice == "Create Custom Plan":
            self.open_custom_plan_window()
            return
        else:
            saved_plans = load_budget_plans()
            budget_plan = saved_plans[plan_choice]

        category_amounts = calculate_category_amounts(total_amount, budget_plan)
        self.display_results(total_amount, plan_choice, category_amounts, budget_plan)

    def display_results(self, total_amount, plan_name, category_amounts, budget_plan):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"📊 Budget Breakdown for {plan_name}\n")
        self.result_text.insert(tk.END, f"Total Amount: ${total_amount:,.2f}\n\n")
        
        for category, amount in category_amounts.items():
            percentage = budget_plan[category]
            self.result_text.insert(tk.END, 
                f"{category}: ${amount:,.2f} ({percentage}%)\n")

def run_gui():
    app = BudgetApp()
    app.mainloop()
