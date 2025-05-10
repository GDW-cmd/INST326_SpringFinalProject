class BudgetAnalysis:
    """
    """
    def __init__(self, expenses_dict, monthly_income):
        self.expenses_dict = expenses_dict #User inputs of all expenses, name : category, cost
        self.monthly_income = monthly_income #User input of income
        self.ideal_budget = {'Needs': 0.5, 'Wants': 0.3, 'Savings': 0.2} #Dictionary of ideal budget
        pass
     
    def compare_with_ideal(self):
        """will compare user's expenses with ideal budget and return values that will be used in chart."""
        pass
        