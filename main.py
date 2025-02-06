from plan import choose_budget_plan, get_custom_plan
from utils import get_valid_number
from calculations import calculate_category_amounts
from storage import save_budget_plan, load_budget_plans

def main():
    print("💰 Welcome to the Budget Automation System! 💰")

    # choose the total amount to budget
    total_amount = get_valid_number("Enter the total amount to budget: ")

    choice = choose_budget_plan()
    saved_plans = load_budget_plans()

    if choice == 1:
        budget_plan = {"Expenses": 50, "Investment": 30, "Savings": 20}
        plan_name = "Conservative (50-30-20)"
    elif choice == 2:
        budget_plan = {"Expenses": 60, "Investment": 20, "Savings": 20}
        plan_name = "Moderate (60-20-20)"
    elif choice == 3:
        budget_plan = {"Expenses": 70, "Investment": 10, "Savings": 20}
        plan_name = "Aggressive (70-10-20)"
    elif choice == len(saved_plans) + 4:
        plan_name, budget_plan = get_custom_plan()
        save_budget_plan(plan_name, budget_plan)

    else:
        # Get the saved custom Plan
        plan_name = list(saved_plans.keys())[choice -4]
        budget_plan = saved_plans[plan_name]

    # Calculate amounts for each category
    
    category_amounts = calculate_category_amounts(total_amount, budget_plan)

    # Display the budget plan
    print(f"\n📊 Your Budget Breakdown for {plan_name}")
    print(f"Total Amount: ${total_amount:.2f}")
    print(f" Category Breakdown")

    for category, amount in category_amounts.items():
        percentage = budget_plan[category]
        print(f"    - {category}: ({percentage}%) : ${amount:.2f} ")


if __name__ == "__main__":
    main()
