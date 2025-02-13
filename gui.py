import tkinter as tk
from tkinter import ttk, messagebox
from plan import get_custom_plan
from utils import get_valid_number
from calculations import calculate_category_amounts
from storage import save_budget_plan, load_budget_plans
from subcategories import get_subcategories

def run_gui():
    root = tk.Tk()
    root.title("Budget Automation System")
    root.geometry("600x500")
    
    def create_custom_plan():
        custom_window = tk.Toplevel(root)
        custom_window.title("Create Custom Budget Plan")
        custom_window.geometry("400x300")
        
        ttk.Label(custom_window, text="Enter Custom Plan Name:").pack()
        plan_name_entry = ttk.Entry(custom_window)
        plan_name_entry.pack()
        
        category_entries = []
        category_labels = []
        percentage_entries = []
        
        def add_category():
            frame = ttk.Frame(custom_window)
            frame.pack()
            
            category_label = ttk.Label(frame, text="Category:")
            category_label.pack(side=tk.LEFT)
            category_labels.append(category_label)
            
            category_entry = ttk.Entry(frame)
            category_entry.pack(side=tk.LEFT)
            category_entries.append(category_entry)
            
            percentage_label = ttk.Label(frame, text="Percentage:")
            percentage_label.pack(side=tk.LEFT)
            
            percentage_entry = ttk.Entry(frame)
            percentage_entry.pack(side=tk.LEFT)
            percentage_entries.append(percentage_entry)
        
        ttk.Button(custom_window, text="Add Category", command=add_category).pack()
        
        def save_custom_plan():
            plan_name = plan_name_entry.get().strip()
            if not plan_name:
                messagebox.showerror("Invalid Input", "Plan name cannot be empty.")
                return
            
            budget_plan = {}
            total_percentage = 0
            
            for category_entry, percentage_entry in zip(category_entries, percentage_entries):
                category = category_entry.get().strip()
                try:
                    percentage = float(percentage_entry.get())
                except ValueError:
                    messagebox.showerror("Invalid Input", "Enter valid percentage values.")
                    return
                
                if category in budget_plan:
                    messagebox.showerror("Duplicate Category", f"Category '{category}' already exists.")
                    return
                
                budget_plan[category] = percentage
                total_percentage += percentage
                
            if total_percentage != 100:
                messagebox.showerror("Invalid Percentage", "Total percentage must add up to 100%.")
                return
            
            save_budget_plan(plan_name, budget_plan)
            plan_choice['values'] = list(load_budget_plans().keys())
            messagebox.showinfo("Success", "Custom budget plan saved successfully.")
            custom_window.destroy()
        
        ttk.Button(custom_window, text="Save Plan", command=save_custom_plan).pack()
    
    def calculate_budget():
        try:
            total_amount = float(amount_entry.get())
            if total_amount <= 0:
                messagebox.showerror("Invalid Input", "Amount must be greater than zero.")
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return
        
        choice = plan_choice.get()
        saved_plans = load_budget_plans()
        
        if choice == "Conservative (50-30-20)":
            budget_plan = {"Expenses": 50, "Investment": 30, "Savings": 20}
        elif choice == "Moderate (60-20-20)":
            budget_plan = {"Expenses": 60, "Investment": 20, "Savings": 20}
        elif choice == "Aggressive (70-10-20)":
            budget_plan = {"Expenses": 70, "Investment": 10, "Savings": 20}
        else:
            budget_plan = saved_plans.get(choice, {})
        
        category_amounts = calculate_category_amounts(total_amount, budget_plan)
        
        # Display results
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"\nBudget Breakdown for {choice}\n")
        result_text.insert(tk.END, f"Total Amount: ${total_amount:,.2f}\n\n")
        
        for category, amount in category_amounts.items():
            result_text.insert(tk.END, f"{category}: ${amount:.2f} ({budget_plan[category]}%)\n")
    
    # UI Components
    ttk.Label(root, text="Enter Total Budget:").pack()
    amount_entry = ttk.Entry(root)
    amount_entry.pack()
    
    ttk.Label(root, text="Select Budget Plan:").pack()
    plan_choice = ttk.Combobox(root, values=[
        "Conservative (50-30-20)", "Moderate (60-20-20)", "Aggressive (70-10-20)", "Custom Plan"
    ] + list(load_budget_plans().keys()))
    plan_choice.pack()
    
    ttk.Button(root, text="Create Custom Plan", command=create_custom_plan).pack()
    ttk.Button(root, text="Calculate Budget", command=calculate_budget).pack()
    
    result_text = tk.Text(root, height=10, width=50)
    result_text.pack()

    
    root.mainloop()

if __name__ == "__main__":
    launch_gui()
