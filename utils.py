def get_valid_number(prompt):
    """ Get a vlid number from the user"""

    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than Zero")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")