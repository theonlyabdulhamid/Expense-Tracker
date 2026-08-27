import json

expenses = []


def main():
    while True:
        menu = """
================================
       EXPENSE TRACKER
================================

1. Add Expense
2. View Expenses
3. Total Spending
4. Spending by Category
5. Delete Expense
6. Save Expenses
7. Load Expenses
8. Exit
                """
        print(menu)
        choice = input("Choose an option: ").strip()
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a valid number")
            continue
        if choice == 1:
            add_expense(expenses)
        elif choice == 2:
            view_expenses(expenses)
        elif choice == 3:
            total = calculate_total(expenses)
            print(f"Your total expense is ₦{total}")
        elif choice == 4:
            category_totals = spending_by_category(expenses)
            count = 1
            for category, amount in category_totals.items():
                print(f"{count}. {category} ---> {amount}")
                count += 1
        elif choice == 5:
            delete_expense(expenses)
        elif choice == 6:
            save_expenses(expenses)
        elif choice == 7:
            load_expenses(expenses)
        elif choice == 8:
            print("Goodbye!")
            break
        else:
            print("Please enter a valid number")


def create_expense():
    while True:
        Amount = input("Amount: ").strip()
        try:
            Amount = int(Amount)
            break
        except ValueError:
            print("please enter a valid amount")
    while True:
        Category=input("Category: ").strip().capitalize()
        if len(Category)>3:
            break
        else:
            print("Category must be above 3 letters")
    while True:
        descrip=input("Description: ").strip().capitalize()
        if len(descrip)>3:
            break
        else:
            print("Category must be above 3 letters")
        
    expense = {
        "Amount": Amount,
        "Category": Category,
        "Description": descrip,
    }
    return expense


def add_expense(expenses):
    expenses.append(create_expense())


def view_expenses(expenses):
    count = 1
    if len(expenses) <= 0:
        print("No expense record yet.")
        return
    for expense in expenses:
        print(
            f"Expense {count}\n Amount: {expense['Amount']}\n Category: {expense['Category']}\n Description: {expense['Description']}"
        )
        count += 1


def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["Amount"]
    return total


def spending_by_category(expenses):
    category = {}
    for expense in expenses:
        if expense["Category"] not in category:
            category[expense["Category"]] = expense["Amount"]
        else:
            category[expense["Category"]] += expense["Amount"]
    if not category:
        print("No expense record yet")
    return category


def delete_expense(expenses):
    if len(expenses) <= 0:
        print("No expense record yet")
        return
    view_expenses(expenses)
    try:
        index = int(input("what expense do you want to delete? "))
    except ValueError:
        print("Please enter a valid number")
        return
    if (index <= len(expenses)) and index > 0:
        expenses.pop(index - 1)
    else:
        print("Expense not found")


def save_expenses(expenses):
    if expenses:
        with open("expenses.json", "w") as file:
            json.dump(expenses, file)
            print("Successfully saved")
    else:
        print("you cannot save an empty file")


def load_expenses(expenses):
    try:
        with open("expenses.json", "r") as output:
            loaded_expenses = json.load(output)
            if loaded_expenses:
                expenses.clear()
                expenses.extend(loaded_expenses)
                print("Expenses loaded successfully.")
            else:
                print("Empty expenses")
    except FileNotFoundError:
        print("No saved expenses found")


main()
