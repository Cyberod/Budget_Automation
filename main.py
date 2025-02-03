from plan import choose_budget_plan, get_custom_plan

def main():
    print("💰 Welcome to the Budget Automation System! 💰")

    choice = choose_budget_plan()

    if choice == 1:
        budget_plan = {"Expenses": 50, "Investment": 30, "Savings": 20}
    elif choice == 2:
        budget_plan = {"Expenses": 60, "Investment": 20, "Savings": 20}
    elif choice == 3:
        budget_plan = {"Expenses": 70, "Investment": 10, "Savings": 20}
    elif choice == 4:
        custom_plan = get_custom_plan()
    
    print("\n📊 Your Selected Budget Plan:")
    for category, percentage in budget_plan.items():
        print(f"   -{category}: {percentage}%")


if __name__ == "__main__":
    main()
