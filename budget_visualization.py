import matplotlib.pyplot as plt
from budget import Budget
from budget_analysis import BudgetAnalysis
import numpy as np

class BudgetVisualization:
    """
    This class creates all charts used for the website, such as user analysis charts that display user data in a visual format, or comparative charts that compare data to a standard ideal budget.

    Attributes:
        budget (Budget): Budget object of user expense dict, Expense Name as key, then Category and Cost as values.
        monthly_income (float): Users monthly income
    """

    def __init__(self, expense_dict, monthly_income):
        self.budget = Budget(expense_dict) #Iniatilize class
        self.monthly_income = float(monthly_income) if not isinstance(monthly_income, (int, float)) else monthly_income 

    def calculate_totals_cat(self):
        """
        Gets totals amount spend on each user category
        
        totals (dict) - Returns categories including 'Wants', 'Needs', 'Saving', 'Unallocated' as key, and total cost for each category as value.
        """

        totals = self.budget.get_all_totals() #Variable dict of categories, and cost.
        totals["Remaining"] = self.monthly_income - sum(totals.values()) #Appends remaining category of unallocated income.

        return totals
    
    def user_category_chart(self):
        """
        Category pie chart, showing users percent cost of each category
        
        Returns:
            fig - pie chart of percent cost of each category
        """

        totals = self.calculate_totals_cat() #Variable of total cost by category
        labels = list(totals.keys())
        values = list(totals.values())
        fig, ax = plt.subplots(figsize=(10, 6))
        
        fig.savefig('myplot.png', transparent=True)
        fig.set_facecolor('none')
        ax.set_facecolor('none')
        ax.pie(values, labels=labels, autopct='%1.1f%%', textprops={'color':"w"})
        ax.set_title("Categorical Expenses", color='white', pad=20, fontweight='bold') #Title

        return fig


    def user_individual_chart(self):
        """
        Individual expense pie chart, showing percent cost of each expense by name

        Returns:
            fig - pie chart of percent cost of each expense
        """
       
        labels = list(self.budget.expense_dict.keys())
        values = [expense['cost'] for expense in self.budget.expense_dict.values()]
        fig, ax = plt.subplots(figsize=(10, 7))
        
        
        fig.savefig('myplot.png', transparent=True)
        fig.set_facecolor('none')
        ax.set_facecolor('none')
        ax.pie(values, labels=labels, autopct='%1.1f%%', textprops={'color':"w"})
        ax.set_title("Individual Expenses", color='white', pad=20, fontweight='bold') #Title
        
        return fig
    
    def ideal_budget(self):
        """
        Basic ideal pie chart of ideal budget using 50/30/20 rule

        Returns:
            fig - pie chart of an ideal budget
        """
        values = [0.5, 0.3, 0.2]
        labels = ["Needs", "Wants", "Savings"]
        fig, ax = plt.subplots(figsize=(6, 4), dpi = 160)
        fig.savefig('myplot.png', transparent=True)
        fig.set_facecolor('none')
        ax.set_facecolor('none')
        ax.pie(values, labels=labels, autopct='%1.1f%%', textprops={'color':'w', 'fontsize': 7})
        
        return fig

    def comparition_chart(self):
        """
        Bar graph, that is a chart comparison from user budget to ideal budget by dollar difference

        Returns:
            fig - bar graph that compares ideal budget to user budget by dollar difference
        """
        #Data to compare, actual spending vs ideal
        analysis = BudgetAnalysis(self.budget.expense_dict, self.monthly_income)
        ideal = analysis.get_ideal_spending()
        actual = self.budget.get_all_totals()
        total_spent = sum(actual.values()) #Gets total spent
        unallocated = self.monthly_income - total_spent #unallocated money
        #Categories, differences, and values
        categories = ['Needs', 'Wants', 'Savings', 'Unallocated']
        ideal_values = [ideal['Needs'], ideal['Wants'], ideal['Savings'], 0]
        actual_values = [actual['Needs'], actual['Wants'], actual['Savings'], unallocated]
        #Graph
        w, x = 0.4, np.arange(len(categories))
        fig, ax = plt.subplots()
        fig.savefig('myplot.png', transparent=True)
        fig.set_facecolor('none')
        ax.set_facecolor('none')
        ax.bar(x - w/2, ideal_values, width=w, label='Ideal',)
        ax.bar(x + w/2, actual_values, width=w, label='Actual')
        ax.set_xticks(x)
        ax.set_xticklabels(categories, color='white', fontweight='bold')
        ax.set_ylabel('Amount ($)', color='white', fontweight='bold')
        ax.set_title('Ideal vs Actual Spending', color='white', fontweight='bold') #Title
        #Making sure other text is white and bold
        ax.yaxis.set_tick_params(colors='white')
        for label in ax.get_yticklabels():
            label.set_fontweight('bold')
        for spine in ax.spines.values():
            spine.set_color('white')
        legend = ax.legend()
        for text in legend.get_texts():
            text.set_color("white")
            
        return fig
    