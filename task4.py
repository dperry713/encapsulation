class BudgetCategory:
    def __init__(self, name, allocated_budget):
        self.name = name
        self.allocated_budget = allocated_budget
        self.expenses = 0

    def add_expense(self, amount):
        self.expenses += amount

    def display_details(self):
        remaining_budget = self.allocated_budget - self.expenses
        print(f"Category: {self.name}")
        print(f"Allocated Budget: ${self.allocated_budget:.2f}")
        print(f"Remaining Budget: ${remaining_budget:.2f}")

# Example usage
food_budget = BudgetCategory("Food", 500)
food_budget.add_expense(150)
food_budget.add_expense(50)
food_budget.display_details()
