

expenses = []

# Set Monthly Budget
budget = float(input("Enter Monthly Budget (Rs.): "))


# Function to validate amount
def validate_amount():
    while True:
        try:
            amount = float(input("Enter Amount (Rs.): "))
            if amount > 0:
                return amount
            else:
                print("Amount must be positive!")
        except ValueError:
            print("Invalid Amount!")


# Function to add expense
def add_expense():
    description = input("Enter Expense Description: ")
    category = input(
        "Enter Category (Food/Travel/Bills/Entertainment/Other): ")
    amount = validate_amount()
    date = input("Enter Date (DD-MM-YYYY): ")

    expense = {
        "description": description,
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)
    print("Expense Added Successfully!")


# Function to view all expenses
def view_expenses():
    if len(expenses) == 0:
        print("No Expenses Found!")
        return

    print("\n------ ALL EXPENSES ------")

    print("No.\tDescription\tCategory\tAmount\tDate")

    for i, expense in enumerate(expenses, start=1):
        print(i, "\t",
              expense["description"], "\t",
              expense["category"], "\t",
              expense["amount"], "\t",
              expense["date"])


# Function for category summary
def category_summary():
    if len(expenses) == 0:
        print("No Expenses Found!")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print("\n------ CATEGORY SUMMARY ------")

    for category, total in summary.items():
        print(category, ":", "Rs.", total)


# Function for budget report
def budget_report():
    total_spent = sum(expense["amount"] for expense in expenses)

    remaining = budget - total_spent
    percentage = (total_spent / budget) * 100

    print("\n------ BUDGET REPORT ------")
    print("Total Spent : Rs.", total_spent)
    print("Budget      : Rs.", budget)
    print("Remaining   : Rs.", remaining)
    print("Used        :", round(percentage, 2), "%")

    if percentage >= 100:
        print("WARNING! Budget Exceeded!")
    elif percentage >= 80:
        print("WARNING! You have used 80% of your budget!")


# Function to get top spending category
def get_top_category():
    if len(expenses) == 0:
        print("No Expenses Found!")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    top_category = max(summary, key=summary.get)

    print("\nTop Spending Category :", top_category)
    print("Amount : Rs.", summary[top_category])


# Function to filter expenses by category
def filter_category():
    cat = input("Enter Category: ")

    found = False

    for expense in expenses:
        if expense["category"].lower() == cat.lower():
            found = True
            print(expense)

    if not found:
        print("No Expenses Found!")


# Function to save data into file
def save_to_file():
    file = open("expenses.txt", "w")

    for expense in expenses:
        file.write(str(expense))
        file.write("\n")

    file.close()


# Main Menu
while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category Summary")
    print("4. Budget Report")
    print("5. Top Spending Category")
    print("6. Filter by Category")
    print("7. Exit")

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_expense()

        elif choice == 2:
            view_expenses()

        elif choice == 3:
            category_summary()

        elif choice == 4:
            budget_report()

        elif choice == 5:
            get_top_category()

        elif choice == 6:
            filter_category()

        elif choice == 7:
            save_to_file()
            print("Expenses saved in expenses.txt")
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please Enter Numbers Only!")

