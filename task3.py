class Budget:
    def __init__(self):
        self.categories = {}

    def add_category(self, category, budget):
        self.categories[category] = {'budget': budget, 'expenses': 0}

    def add_expense(self, category, amount):
        if category not in self.categories:
            return "Category does not exist."
        
        if amount <= 0:
            return "Invalid expense amount."

        if self.categories[category]['budget'] < amount:
            return "Insufficient budget."

        self.categories[category]['expenses'] += amount
        self.categories[category]['budget'] -= amount
        return f"Expense of ${amount} added to {category}. Remaining budget: ${self.categories[category]['budget']}."

    def get_remaining_budget(self, category):
        if category not in self.categories:
            return "Category does not exist."
        return self.categories[category]['budget']

    def get_expenses(self, category):
        if category not in self.categories:
            return "Category does not exist."
        return self.categories[category]['expenses']

# Example usage
budget = Budget()
budget.add_category("Food", 500)
budget.add_category("Entertainment", 300)

print(budget.add_expense("Food", 50))  # Expense of $50 added to Food. Remaining budget: $450.
print(budget.add_expense("Entertainment", 100))  # Expense of $100 added to Entertainment. Remaining budget: $200.
print(budget.add_expense("Food", 600))  # Insufficient budget.
print(budget.get_remaining_budget("Food"))  # 450
print(budget.get_expenses("Entertainment"))  # 100
