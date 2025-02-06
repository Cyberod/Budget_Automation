def calculate_category_amounts(total_amount, budget_plan):
    """Calculate the amount for each category based on the budget plan.
        Args:
        total_amount (float): The total amount to be distributed.
        budget_plan (dict): The budget plan with category percentages.

        Returns:
        dict: A dictionary with category names as keys and their respective amounts as values.
    """

    category_amounts = {}

    for category, percentage in budget_plan.items():
        amount = total_amount * (percentage / 100)
        category_amounts[category] = round(amount, 2)

    return category_amounts
