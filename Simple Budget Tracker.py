from decimal import Decimal, ROUND_HALF_UP
import locale as lc

# Set locale for currency formatting
lc.setlocale(lc.LC_ALL, "en_US")

# Custom exception for negative values
class NegativeValueError(Exception):
    pass

def get_income():
    while True:
        try:
            income_input = input("Enter your total income: $")
            income = Decimal(income_input)
            if income < 0:
                raise NegativeValueError("Income cannot be negative.. Please enter a valid income amount.")
            return income.quantize(Decimal("1.00"), ROUND_HALF_UP)
        except NegativeValueError as e:
            print("Invalid input:", e)
        except Exception as e:
            print(f"Invalid input: could not convert string to float: '{income_input}'. Please enter a valid income amount.")

def get_expenses():
    expenses = []
    while True:
        try:
            expense_input = input("Enter an expense amount (or 0 to exit): ")
            amount = Decimal(expense_input)
            if amount < 0:
                raise NegativeValueError("Expense cannot be negative.. Please enter a valid expense amount or 0.")
            elif amount == 0:
                break
            else:
                expenses.append(amount.quantize(Decimal("1.00"), ROUND_HALF_UP))
        except NegativeValueError as e:
            print("Invalid input:", e)
        except Exception as e:
            print(f"Invalid input: could not convert string to float: '{expense_input}'. Please enter a valid expense amount or 0.")
    return expenses

def display_results(income, expenses):
    total_expenses = sum(expenses)
    total_expenses = total_expenses.quantize(Decimal("1.00"), ROUND_HALF_UP)
    remaining = income - total_expenses

    print("\nBudget Results:")
    print("-" * 30)
    print(f"Total Income: {lc.currency(income, grouping=True)}")
    print(f"Total Expenses: {lc.currency(total_expenses, grouping=True)}")
    print(f"Remaining Budget: {lc.currency(remaining, grouping=True)}")
    print()

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}: {lc.currency(expense, grouping=True)}")

def main():
    print("Welcome to the Simple Budget Tracker")
    print("-" * 32)
    income = get_income()
    expenses = get_expenses()
    display_results(income, expenses)
    print("\nCompleted by, Jonathan Jewell")

if __name__ == "__main__":
    main()