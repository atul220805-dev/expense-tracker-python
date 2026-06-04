

from database1 import (
    create_table,
    add_transaction,
    view_transactions,
    delete_transaction,
    update_transaction,
    search_by_category
)

from analytics import (
    total_income,
    total_expense,
    savings,
    spending_by_category,
    financial_health_score,
    budget_alert
)


# Create database table when app starts
create_table()


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Update Transaction")
    print("4. Delete Transaction")
    print("5. Search By Category")
    print("6. Financial Report")
    print("7. Budget Alert")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # 1. Add Transaction
    if choice == "1":

        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        type = input("Enter type (Income/Expense): ")
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")

        add_transaction(
            amount,
            category,
            type,
            date,
            description
        )

        print("Transaction Added Successfully!")

    # 2. View Transactions
    elif choice == "2":

        data = view_transactions()

        print("\n===== ALL TRANSACTIONS =====")

        for row in data:
            print(row)

    # 3. Update Transaction
    elif choice == "3":

        transaction_id = int(input("Enter transaction ID: "))
        amount = float(input("New amount: "))
        category = input("New category: ")
        type = input("New type (Income/Expense): ")
        date = input("New date: ")
        description = input("New description: ")

        update_transaction(
            transaction_id,
            amount,
            category,
            type,
            date,
            description
        )

        print("Transaction Updated!")

    # 4. Delete Transaction
    elif choice == "4":

        transaction_id = int(input("Enter transaction ID to delete: "))

        delete_transaction(transaction_id)

        print("Transaction Deleted!")

    # 5. Search by category
    elif choice == "5":

        category = input("Enter category: ")

        results = search_by_category(category)

        print("\n===== SEARCH RESULTS =====")

        for row in results:
            print(row)

    # 6. Financial Report
    elif choice == "6":

        print("\n===== FINANCIAL REPORT =====")

        print(f"Total Income: ₹{total_income()}")
        print(f"Total Expense: ₹{total_expense()}")
        print(f"Savings: ₹{savings()}")

        print("\nSpending By Category:")

        for category, amount in spending_by_category():
            print(f"{category}: ₹{amount}")

        print("\nFinancial Health Score:")
        print(financial_health_score())

    # 7. Budget Alert
    elif choice == "7":

        category = input("Enter category: ")
        budget = float(input("Enter budget amount: "))

        result = budget_alert(category, budget)

        print(result)

    # 8. Exit
    elif choice == "8":

        print("Goodbye!")
        break

    else:
        print("Invalid choice")