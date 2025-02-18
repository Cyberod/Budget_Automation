
from storage import save_budget_plan, load_budget_plans


def choose_budget_plan():
    """Allows user to select a predefined or custom budget plan."""
    print("Choose a budget plan:")
    print("1. 50-30-20 (Conservative)")
    print("2. 60-20-20 (Moderate)")
    print("3. 70-10-20 (Aggressive)")

    # load and display saved custom plans

    saved_plans = load_budget_plans()
    start_index = 4

    for i, plan_name in enumerate(saved_plans.keys(), start=start_index):
        print(f"{i}. {plan_name} (Custom)")

    print(f"{len(saved_plans) + start_index}. Create new custom Plan")

    while True:
        try:
            max_choice = len(saved_plans) + start_index 
            choice = int(input(f"Enter your chouce (1 - {max_choice})"))
            if 1 <= choice <= max_choice:
                return choice
            else:
                print("Invalid choice. Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        

def get_custom_plan():
    """"Allows user to create a custom budget plan"""

    # The System will ask the user to enter a name for the custom budget plan.
    while True:
        custom_plan_name = str(input("Enter a name for your custom budget plan: "))
        try:
            #check if name is empty
            if not custom_plan_name:
                print("Custom plan name cannot be empty. Please enter a valid name.")
                continue

            # check if name is only numbers
            if custom_plan_name.isdigit():
                print("Plan must contain Letters or a combination of Letters and numbers")
                continue

            if not any(char.isalpha() for char in custom_plan_name):
                print("plan name must contain at least one letter")
                continue
            
            break
            
        except ValueError:
            print("Input only letters for the category name.")
        

    custom_plan = {}
    total_percentage = 0

    print(f"Creating a custom budget plan for {custom_plan_name}")

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

        # Save the custom plan automatically after creation
        save_budget_plan(custom_plan_name, custom_plan)
        print(f"Custom plan '{custom_plan_name}' has been saved sucessfully!.")
    return custom_plan_name, custom_plan
