from src.core.plan import choose_budget_plan, get_custom_plan
from src.cli.utils import get_valid_number
from src.core.calculations import calculate_category_amounts
from src.core.storage import save_budget_plan, load_budget_plans
from src.core.subcategories import get_subcategories

def run_cli():
    print("💰 Welcome to the Budget Automation System! 💰")

    # choose the total amount to budget
    total_amount = get_valid_number("Enter the total amount to budget: ")

    choice = choose_budget_plan()
    saved_plans = load_budget_plans()

    max_choice = len(saved_plans) + 4
    category_subcategories = {}

    if choice == 1:
        budget_plan = {"Expenses": 50, "Investment": 30, "Savings": 20}
        plan_name = "Conservative (50-30-20)"
    elif choice == 2:
        budget_plan = {"Expenses": 60, "Investment": 20, "Savings": 20}
        plan_name = "Moderate (60-20-20)"
    elif choice == 3:
        budget_plan = {"Expenses": 70, "Investment": 10, "Savings": 20}
        plan_name = "Aggressive (70-10-20)"
    elif choice == max_choice:
        plan_name, budget_plan = get_custom_plan()

        # Calculate amounts for each category
        category_amounts = calculate_category_amounts(total_amount, budget_plan)

        for category, amount in category_amounts.items():
            if input(f"Would you like to add subcategories for {category}? (y/n): ").lower() == 'y':
                category_subcategories[category] = get_subcategories(category, amount)
        save_budget_plan(plan_name, budget_plan, {
            category: {
                subcat: {"percentage": details["percentage"]}
                for subcat, details in subcats.items()
        }
            for category, subcats in category_subcategories.items()
            })


    else:
        # Get the saved custom Plan
        plan_name = list(saved_plans.keys())[choice -4]
        saved_plan = saved_plans[plan_name]

        # Extracts the categories and Percentages from the saved custom Plan
        budget_plan = {
            category: data["percentage"]
            for category, data in saved_plan["categories"].items()
        }

        # calsulates the amount for each category
        category_amounts = calculate_category_amounts(total_amount, budget_plan)

        # Initializes subcategories with saved data
        category_subcategories = {}
        for category, data in saved_plan["categories"].items():
            if data["subcategories"]:
                subcategory_amounts = {}
                category_amount = category_amounts[category]

                for subcat, subdata in data["subcategories"].items():
                    amount = category_amount * (subdata["percentage"] / 100)
                    subcategory_amounts[subcat] = {
                        "percentage": subdata["percentage"],
                        "amount": round(amount, 2)
                    }

                category_subcategories[category] = subcategory_amounts






    
    # Print final complete breakdown
    print(f"\n📊 Your Budget Breakdown for {plan_name}")
    print(f"Total Amount: ${total_amount:,.2f}")
    print("\nCategory Breakdown:")
    
    for category, amount in category_amounts.items():
        percentage = budget_plan[category]
        print(f"\n{category}: ${amount:.2f} ({percentage}%)")
        
        if category in category_subcategories:
            for subcat, details in category_subcategories[category].items():
                print(f"   - {subcat}: ${details['amount']:.2f} ({details['percentage']}%)")
