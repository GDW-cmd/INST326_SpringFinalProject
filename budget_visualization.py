# This class generates a bar chart of the budget categories and their amounts using matplotlib.

import matplotlib.pyplot as plt
from budget import Budget

class BudgetVisualization:
    
    # function to generate a bar chart of the budget categories and their amounts
    def __init__(self, expense_dict, monthly_income):
        self.budget = Budget(expense_dict)
        self.monthly_income = monthly_income

    def calculate_totals_cat(self):
        """Gets totals from budget.py and also remaining unallocated cost"""
        totals = self.budget.get_all_totals()
        totals["Remaining"] = self.monthly_income - sum(totals.values())
        return totals
    
    def user_category_chart(self):
        """Chart of all categories"""
        totals = self.calculate_totals_cat()

        labels = list(totals.keys())
        values = list(totals.values())

        pass

    def user_individual_chart(self):
        """Chart of each individual expense"""
        pass

    def comparition_chart(self):
        """Chart comparison to ideal budget"""
        pass
    