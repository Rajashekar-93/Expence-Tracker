import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        """Load expenses from a JSON file if it exists."""
        try:
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        """Save expenses to a JSON file."""
        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file)

    def add_expense(self, amount, description, category):
        """Add a new expense to the tracker."""
        expense = {
            "amount": amount,
            "description": description,
            "category": category,
            "date": str(datetime.now().date())
        }
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully.")

    def display_expenses(self):
        """Display all recorded expenses."""
        if not self.expenses:
            print("No expenses recorded.")
            return
        
        print("\nRecorded Expenses:")
        for idx, expense in enumerate(self.expenses, start=1):
            print(f"{idx}. {expense['date']} - {expense['description']} ({expense['category']}): ${expense['amount']}")

    def monthly_summary(self):
        """Provide a summary of expenses for the current month."""
        total = 0
        category_summary = {}

        current_month = datetime.now().month
        current_year = datetime.now().year

        for expense in self.expenses:
            date = datetime.strptime(expense['date'], '%Y-%m-%d')
            if date.month == current_month and date.year == current_year:
                total += expense['amount']
                category_summary[expense['category']] = category_summary.get(expense['category'], 0) + expense['amount']

        print(f"\nTotal expenses for {datetime.now().strftime('%B %Y')}: ${total:.2f}")
        for category, amount in category_summary.items():
            print(f"{category}: ${amount:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                description = input("Enter description: ")
                category = input("Enter category: ")
                tracker.add_expense(amount, description, category)
            except ValueError:
                print("Invalid input! Please enter a valid amount.")

        elif choice == '2':
            tracker.display_expenses()

        elif choice == '3':
            tracker.monthly_summary()

        elif choice == '4':
            print("Exiting the Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid option! Please select a valid choice.")

if __name__ == "__main__":
    main()
