def choose_budget_plan():
    """Allows user to select a predefined or custom budget plan."""
    print("Choose a budget plan:")
    print("1. 50-30-20 (Conservative)")
    print("2. 60-20-20 (Moderate)")
    print("3. 70-10-20 (Aggressive)")
    print("4. Custom Budget Plan")

    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")	
        except ValueError:
            print("Invalid input. Please enter a number.")

        

def get_custom_plan():
    """"Allows user to create a custom budget plan"""
    custom_plan_name = input("Enter a name for your custom budget plan: ")
    custom_plan = {}
    total_percentage = 0

    print("Enter your custom budget plan:")

    while total_percentage < 100:
        category = input("Enter a category name or type 'done' to finish: ").strip()
        percentage = int(input("Enter the percentage for {}: ".format(category)))

        if category.lower() == 'done':
            if total_percentage == 100:
                break
            else:
                print(f"The total percentage must be{total_percentage}%. Please adjust your percentages.")
                continue

        while True:
            try:
                percentage = float(input("Enter the percentage for {}: ".format(category)))
                if percentage <= 0 or (total_percentage + percentage) > 100:
                    print("Invalid percentage. Please enter a positive value less than or equal to 100.")
                else:
                    custom_plan[category] = percentage
                    total_percentage += percentage
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric percentage.")

        return custom_plan_name, custom_plan
