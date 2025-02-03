def budget_split(income):
    expenses = income * 0.50
    investment = income * 0.30
    savings = income * 0.20

    return expenses, investment, savings

def main():
    try:
        income = float(input("Enter your total income: "))
        if income <= 0:
            print("Please enter a valid positive number for income.")
            return

        expenses, investment, savings = budget_split(income)

        print("\nBudget Breakdown:")
        print(f"Expenses (50%): ${expenses:.2f}")
        print(f"Investment (30%): ${investment:.2f}")
        print(f"Savings (20%): ${savings:.2f}")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
