import json
import os

transactions = []

def load_transactions():
    if os.path.exists("transactions.json"):
        with open("transactions.json", "r") as file:
            return json.load(file)
    return []

def save_transactions():
    with open("transactions.json", "w") as file:
        json.dump(transactions, file)

def add_transaction():
    category = input("Enter transaction category (income/expense): ").lower()
    amount = float(input("Enter transaction amount: "))
    description = input("Enter transaction description: ")

    transactions.append({
        "category": category,
        "amount": amount,
        "description": description
    })
    save_transactions()
    print(f"Transaction added successfully!")

def calculate_budget():
    income = sum(t["amount"] for t in transactions if t["category"] == "income")
    expenses = sum(t["amount"] for t in transactions if t["category"] == "expense")
    remaining_budget = income - expenses
    return remaining_budget

def analyze_spending():
    expense_categories = {}
    for t in transactions:
        if t["category"] == "expense":
            category = t["description"]
            amount = t["amount"]
            expense_categories.setdefault(category, 0)
            expense_categories[category] += amount

    print("\n--- Spending Analysis ---")
    for category, amount in expense_categories.items():
        print(f"{category}: ${amount:.2f}")
    print("-------------------------\n")

def main():
    global transactions
    transactions = load_transactions()

    while True:
        print("\n===== Budget Tracker =====")
        print("1. Add Transaction")
        print("2. Calculate Remaining Budget")
        print("3. Analyze Spending Trends")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            remaining_budget = calculate_budget()
            print(f"Remaining Budget: ${remaining_budget:.2f}")
        elif choice == "3":
            analyze_spending()
        elif choice == "4":
            print("Exiting")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()