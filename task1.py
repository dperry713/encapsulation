class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget

    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, category_name):
        self.__category_name = category_name

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget
    def set_allocated_budget(self, allocated_budget):
        self.__allocated_budget = allocated_budget

# Example usage
food_budget = BudgetCategory("Food", 500)
print(food_budget.get_category_name())  # Output: Food
print(food_budget.get_allocated_budget())  # Output: 500
