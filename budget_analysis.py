from budget import Budget

class BudgetAnalysis:
    """
    Replace comment later
    """
    def __init__(self, expense_dict, monthly_income):
        self.budget = Budget(expense_dict) #User inputs of all expenses, name : category, cost
        self.monthly_income = monthly_income #User input of income
        self.ideal_budget = {'Needs': 0.5, 'Wants': 0.3, 'Savings': 0.2} #Dictionary of ideal budget
        pass

    def user_category_percent_budget(self):
        """
        Returns users budget percentages with dictionary, key (Category), value (Percentage)
        """
        if self.monthly_income <= 0:
            return {'Needs': 0, 'Wants': 0, 'Savings': 0}
        totals = self.budget.get_all_totals()
        return {
            'Needs': totals['Needs'] / self.monthly_income,
            'Wants': totals['Wants'] / self.monthly_income,
            'Savings': totals['Savings'] / self.monthly_income
            }


     
    def compare_with_ideal(self):
        """will compare user's expenses with ideal budget and return values that will be used in chart."""
        pass
        