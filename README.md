## Expense Tracker

A simple terminal-based expense tracker built with Python. The application allows users to record, view, analyze, delete, save, and load personal expenses.

This project was built as part of my Python fundamentals learning journey, with a focus on practicing core Python concepts through a practical application.

\*_Features_

- Add new expenses
- View all recorded expenses
- Calculate total spending
- View spending by category
- Delete an expense
- Save expenses to a JSON file
- Load previously saved expenses
- Basic input validation
- Handles missing expense files

**Technologies Used**

- **Python 3**
- **JSON**
- Python built-in `json` module
- File handling
- Exception handling

**Data Structure**

Each expense is stored as a dictionary containing:

```python
{
    "Amount": 3000,
    "Category": "Food",
    "Description": "Dinner"
}
```

Multiple expenses are stored inside a list:

```python
expenses = []
```

## How to Run

**1. Clone the repository**

```bash
git clone http://github.com/theonlyabdulhamid/Expense-Tracker.git
```

**2. Navigate into the project directory**

```bash
cd Expense-Tracker
```

**3. Run the application**
without a python virtual env active

```bash
python3 expenses_tracker.py
```

with a python virtual env active

```bash
python expenses_tracker.py
```

## Menu

```text
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
```

## What I Learned

Through this project, I practiced and strengthened my understanding of:

- Lists and dictionaries
- Functions and function parameters
- `for` and `while` loops
- Conditional statements
- User input and validation
- `try` and `except`
- List methods such as `append()`, `pop()`, `clear()`, and `extend()`
- Reading and writing files
- Working with JSON using `json.dump()` and `json.load()`
- Handling `FileNotFoundError`
- Breaking a larger problem into smaller functions
- Debugging and testing my own code

## Project Structure

```text
expense-tracker/
    expenses_tracker.py
    expenses.json
    learning_json.py
    README.md
```

> `expenses.json` is created when expenses are saved from the application.
> learning_json.py was created to practice pythons json model before implementing it on expense_tracker.py

## Future Improvements

Possible improvements for future versions include:

- Better validation for expense amounts
- Preventing negative expense values
- Handling invalid JSON files
- Adding dates to expenses
- Improved terminal formatting
- More detailed spending reports
- Unit tests
- Exporting expenses to CSV
- Building a good UI to improve users exprence

## Author

**Abdulhamid Umar**

This project represents one of my early practical projects while strengthening my Python programming fundamentals.
