# Expense Tracker (Python)

A simple command-line based Expense Tracker built using Python.  
This project helps users record daily expenses, view all expenses, and calculate the total amount spent.

---

## Features

- Add new expenses (date, category, description, amount)
- View all recorded expenses
- Calculate total expense
- Exit option to safely close the program
- Beginner-friendly and easy to understand

---

## Technologies Used

- Python 
- Command Line Interface (CLI)

---

## Project Structure
Expense_Tracker/
│
├── main.py # Main Python file containing expense tracker logic
└── README.md # Project documentation


---

## How to Run the Project

1. Make sure Python is installed on your system.
   Check using:
   ```bash
   python --version
2. Open terminal in the project folder.
3. Run the program:
python main.py

---

##Menu Options##
'''
1. Add Expense
2. View All Expenses
3. View Total Expense
4. Exit
'''

---

## Sample Output

Welcome to the Expense Tracker!

Menu:
1. Add Expense
2. View All Expenses
3. View Total Expense
4. Exit
Choose an option: 1
Enter the date (YYYY-MM-DD): 06-01-2026
Enter the category (e.g., Food, Transport): food
Enter a description for remember: Bdy Party!
Enter the amount: 2000

Expense added successfully!

Menu:
1. Add Expense
2. View All Expenses
3. View Total Expense
4. Exit
Choose an option: 1
Enter the date (YYYY-MM-DD): 10-01-2026
Enter the category (e.g., Food, Transport): laptop repairing
Enter a description for remember: none
Enter the amount: 800

Expense added successfully!

Menu:
1. Add Expense
2. View All Expenses
3. View Total Expense
4. Exit
Choose an option: 2

All Expenses:
1. Date: 06-01-2026, Category: food, Description: Bdy Party!, Amount: 2000.00
2. Date: 10-01-2026, Category: laptop repairing, Description: none, Amount: 800.00

Menu:
1. Add Expense
2. View All Expenses
3. View Total Expense
4. Exit
Choose an option: 3

Total Cost: 2800.00

Menu:
1. Add Expense
2. View All Expenses
3. View Total Expense
4. Exit
Choose an option: 4
Exiting the Expense Tracker. Goodbye!

---
## Future Improvements

- Store expenses in a file (CSV or JSON)
- Monthly expense summary
- Category-wise expense analysis
- Input validation and error handling
- GUI or web-based version

---

## Author
Kanchan Kumari
