def display_menu():
    print("\nPersonal Budget Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transaction History")
    print("5. Quit")

def add_income(transactions):
    transaction = {}
    transaction['type'] = "income"

    amount = float(input("Enter amount: "))
    if amount <= 0:
        print("Amount must be greater than zero.")
        return
    transaction['amount'] = amount

    description = input("Enter description: ")
    transaction['description'] = description

    transactions.append(transaction)
    print("Transaction added successfully.")

def add_expense(transactions):
    transaction = {}
    balance = calculate_balance(transactions)
    transaction['type'] = "expense"

    amount = float(input("Enter amount: "))
    if amount <= 0:
        print("Amount must be greater than zero.")
        return
    if balance < amount:
        print("You don't have sufficient funds for this expense.")
        return
    transaction['amount'] = amount

    description = input("Enter description: ")
    transaction['description'] = description

    transactions.append(transaction)
    print("Transaction added successfully.")

def calculate_balance(transactions):
    balance = 0.0
    for transaction in transactions:
        if transaction['type'] == 'income':
            balance += transaction['amount']
        elif transaction['type'] == 'expense':
            balance -= transaction['amount']
    return balance

def view_transactions(transactions):
    if not transactions:
        print("No transactions found.")
        return
    print("\nTransaction History:")
    for i, transaction in enumerate(transactions, start=1):
        print(f"{i}. {transaction['type'].capitalize()}: {transaction['amount']} - {transaction['description']}")

def main():
    transactions = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_income(transactions)
        elif choice == '2':
            add_expense(transactions)
        elif choice == '3':
            balance = calculate_balance(transactions)
            print(f"Current Balance: {balance}")
        elif choice == '4':
            view_transactions(transactions)
        elif choice == '5':
            print("Exiting the Personal Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
