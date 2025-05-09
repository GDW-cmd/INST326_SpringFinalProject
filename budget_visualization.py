# This class generates a bar chart of the budget categories and their amounts using matplotlib.

import matplotlib.pyplot as plt
from budget import Budget

class BudgetVisualization:
    
    # function to generate a bar chart of the budget categories and their amounts
    def __init__(self, expense_dict, monthly_income):
        self.budget = Budget(expense_dict)
        self.monthly_income = monthly_income
    
    def user_category_chart(self):
        """Chart of all categories"""
        pass

    def user_individual_chart(self):
        """Chart of each individual expense"""
        pass

    def comparition_chart(self):
        """Chart comparison to ideal budget"""
        pass
    