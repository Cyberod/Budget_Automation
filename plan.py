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

    # The System will ask the user to enter a name for the custom budget plan.
    while True:
        custom_plan_name = input("Enter a name for your custom budget plan: ")
        try:
            if str(custom_plan_name):
                break
            print("Custom plan name cannot be empty. Please enter a valid name.")
        except ValueError:
            print("Input only letters for the category name.")
        

    
    custom_plan = {}
    total_percentage = 0

    print(f"creating a custom budget plan for {custom_plan_name}")

    while total_percentage < 100:
        category = input("Enter a category (or 'done' to exit custom plan): ")

        # Handling the done command
        if category.lower() == 'done':
            if total_percentage < 100:
                print("You have successfully exited the the custom plan.")
                choose_budget_plan()
        
        # validate category name
        if not all(char.isalpha() or char.isspace() for char in category):
            print("category name must only contain letters and spaces.")
            continue

        if category.strip() == "":
            print("Category name cannot be empty. Please enter a valid category name.")
            continue

        if category in custom_plan:
            print(f"Category '{category}' already exists. Please choose a different category name.")
            continue

        # Get and validate percentage
        while True:
            try:
                percentage = float(input(f"Enter the percentage for {category}: "))
                if percentage <= 0 or (total_percentage + percentage) > 100:
                    print("Percentage must be greater than zero and total percentage must not exceed 100%.")
                else:
                    custom_plan[category] = percentage
                    total_percentage += percentage
                    break
            except ValueError:
                    print("Invalid input. Please enter a valid number.")

        if total_percentage == 100:
            break
    
    return custom_plan_name, custom_plan
