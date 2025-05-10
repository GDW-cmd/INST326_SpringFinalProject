from budget import Budget

class BudgetAnalysis:
    """
    Replace comment later
    """
    def __init__(self, expense_dict, monthly_income):
        self.budget = Budget(expense_dict) #User inputs of all expenses, name : category, cost
        self.monthly_income = monthly_income #User input of income
        self.ideal_percents = {'Needs': 0.5, 'Wants': 0.3, 'Savings': 0.2} #Dictionary of ideal budget
        pass

    def get_ideal_spending(self):
        """
        Returns users budget percentages with dictionary, key (Category), value (Percentage)
        """
        if self.monthly_income <= 0:
            return {'Needs': 0, 'Wants': 0, 'Savings': 0}
        totals = self.budget.get_all_totals()
        return {
            'Needs': self.monthly_income * self.ideal_percents['Needs'],
            'Wants': self.monthly_income * self.ideal_percents['Wants'],
            'Savings': self.monthly_income * self.ideal_percents['Savings']
        }


    def compare_with_ideal(self):
        """will compare user's expenses with ideal budget and return values that will be used in chart."""

        user_budget = self.user_category_percent_budget()
        


        pass
        