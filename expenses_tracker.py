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
        choice = int(input("Choose an option: "))
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
        elif choice==5:
            delete_expense(expenses)
        elif choice == 8:
            print("Goodbye!")
            break


def create_expense():
    expense = {
        "Amount": int(input("Amount: ")),
        "Category": input("Category: ").strip().capitalize(),
        "Description": input("Description: "),
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
    return category
def delete_expense(expenses):
    if len(expenses)<=0:
        print("No expense record yet")
        return
    view_expenses(expenses)
    index= int(input("what expense do you want to delete? "))
    expenses.pop(index-1)
main()
