# Expense Tracker project

expenseList = []
print("Welcome to the Expense Tracker!")

while True:
    print("\nMenu:")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = int(input("Choose an option: "))

# ADD EXPENSE:
    if choice == 1:
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category (e.g., Food, Transport): ")
        description = input("Enter a description for remember: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expenseList.append(expense)
        print("\n Expense added successfully!")

# VIEW ALL EXPENSES:
    elif (choice == 2):
        if(len(expenseList)== 0):
            print("\n No expenses recorded yet.")
        else:
            print("\nAll Expenses:")
            count = 1
            for expense in expenseList: 
                print(f"{count}. Date: {expense['date']}, Category: {expense['category']}, Description: {expense['description']}, Amount: {expense['amount']:.2f}")
                count += 1

# VIEW TOTAL EXPENSE:
    elif (choice ==3):
        total = 0
        for expense in expenseList:
            total = total + expense["amount"]

        print(f"\n Total Cost: {total:.2f}")

# Exit:
    elif (choice == 4):
        print("Exiting the Expense Tracker. Goodbye!")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN !")


