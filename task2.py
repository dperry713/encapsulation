class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self._category_name = category_name
        self._allocated_budget = allocated_budget

    # Getter for category_name
    @property
    def category_name(self):
        return self._category_name

    # Setter for category_name
    @category_name.setter
    def category_name(self, value):
        if isinstance(value, str) and value.strip():
            self._category_name = value
        else:
            raise ValueError("Category name must be a non-empty string.")

    # Getter for allocated_budget
    @property
    def allocated_budget(self):
        return self._allocated_budget

    # Setter for allocated_budget
    @allocated_budget.setter
    def allocated_budget(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._allocated_budget = value
        else:
            raise ValueError("Allocated budget must be a positive number.")

# Example usage
try:
    category = BudgetCategory("Food", 500)
    print(category.category_name)  # Output: Food
    print(category.allocated_budget)  # Output: 500

    category.category_name = "Groceries"
    category.allocated_budget = 600
    print(category.category_name)  # Output: Groceries
    print(category.allocated_budget)  # Output: 600

    # This will raise a ValueError
    category.allocated_budget = -100
except ValueError as e:
    print(e)
