class BudgetAnalysis:
    """
    Analyzes budget data by comparing it to the 50/30/20 budgeting rule.
    
    Attributes:
        budget (Budget): Budget object 
    """
    def __init__(self, budget):
        self.budget = budget

    def calculate_ideal(self):
        """This will be used for the 50/30/20 rule."""
        income = self.budget.monthly_income
        return {
            'need': income * 0.5,
            'want': income * 0.3,
            'saving': income * 0.2
       }
    
    def compare_with_ideal(self):
        """will compare user's expenses with ideal budget."""
        actual = {
            'need': self.budget.get_category_total('need'),
            'want': self.budget.get_category_total('want'),
            'saving': self.budget.get_total_savings()
        }
        ideal = self.calculate_ideal()
        difference = {
            key: actual[key] - ideal[key] for key in ideal
        }
        return {'actual': actual, 'ideal': ideal, 'difference': difference} 
