# This class generates a bar chart of the budget categories and their amounts using matplotlib.

import matplotlib.pyplot as plt
from budget import Budget
from budget_analysis import BudgetAnalysis
import numpy as np

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
        fig, ax = plt.subplots()
        fig.savefig('myplot.png', transparent=True)
        fig.set_facecolor('none')
        ax.set_facecolor('none')
        ax.pie(values, labels=labels, autopct='%1.1f%%', textprops={'color':"w"})

        #title
        ax.set_title("Categorical Expenses", color='white', pad=20, fontweight='bold')
        return fig


    def user_individual_chart(self):
        """Chart of each individual expense"""
       
        labels = list(self.budget.expense_dict.keys())
        values = [expense['cost'] for expense in self.budget.expense_dict.values()]
        fig, ax = plt.subplots()
        fig.savefig('myplot.png', transparent=True)
        fig.set_facecolor('none')
        ax.set_facecolor('none')
        ax.pie(values, labels=labels, autopct='%1.1f%%', textprops={'color':"w"})
        
        #title
        ax.set_title("Individual Expenses", color='white', pad=20, fontweight='bold')
        
        return fig
    def ideal_budget(self):
        values = [0.5, 0.3, 0.2]
        labels = ["Needs", "Wants", "Savings"]

        fig, ax = plt.subplots()
        fig.savefig('myplot.png', transparent=True)
        fig.set_facecolor('none')
        ax.set_facecolor('none')
        ax.pie(values, labels=labels, autopct='%1.1f%%', textprops={'color':"w"})

        #title
        ax.set_title("Ideal Budget", color='white', pad=20, fontweight='bold')

        return fig

    def comparition_chart(self):
        """Chart comparison to ideal budget"""
        #Data going to compare, actual spending vs ideal
        analysis = BudgetAnalysis(self.budget.expense_dict, self.monthly_income)
        ideal = analysis.get_ideal_spending()
        actual = self.budget.get_all_totals()
        total_spent = sum(actual.values()) #Gets total spent
        unallocated = self.monthly_income - total_spent #unallocated money

        #Categories, differences, and values
        categories = ['Needs', 'Wants', 'Savings', 'Unallocated']
        ideal_values = [ideal['Needs'], ideal['Wants'], ideal['Savings'], 0]
        actual_values = [actual['Needs'], actual['Wants'], actual['Savings'], unallocated]
        differences = [actual[i] - ideal[i] for i in categories]

        pass
    