def get_subcategories(category_name, category_amount):
    """ Adds sub-categories to a Category
        Args:
        category_name (str): The name of the category
        category_amount (float): The amount allocated to the category

        Returns:
        dict: A dictionary with subcategory name as keys and their respective amounts as values.
    """

    subcategories = {}
    total_percentage = 0

    print(f"Adding subcategories for {category_name} (Total amount): {category_amount}")

    while total_percentage < 100:
        subcategory = input(f" Enter subcategory name for {category_name} (or 'done' to exit)").strip()

        if subcategory.lower() == 'done':
            if total_percentage < 100:
                print(f"Current allocation is {total_percentage}%. subcategories allocation must be up to 100%.")
                continue

        if not all(char.isalpha() or char.isspace() for char in subcategory):
            print("Subcategory name must only contain letters and spaces.")
            continue

        while True:
            try:
                percentage = float(input(f"Enter the percentage for {subcategory}: "))
                if percentage <= 0 or (total_percentage + percentage) > 100:
                    print("Percentage must be greater than zero and total percentage must not exceed 100%.")
                else:
                    amount = category_amount * (percentage / 100)
                    subcategories[subcategory] = {"percentage": percentage, "amount": round(amount, 2)}
                    total_percentage += percentage
                    break

            except ValueError:
                print("Invalid input. Kindly enter a valid number.")
        if total_percentage == 100:
            break

    return subcategories
