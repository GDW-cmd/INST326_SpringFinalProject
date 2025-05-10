from budget import Budget

class BudgetAnalysis:
    """
    Replace comment later
    """
    def __init__(self, expense_dict, monthly_income):
        self.budget = Budget(expense_dict) #User inputs of all expenses, name : category, cost
        self.monthly_income = monthly_income #User input of income
        self.ideal_percents = {'Needs': 0.5, 'Wants': 0.3, 'Savings': 0.2} #Dictionary of ideal budget

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


    def budget_differences(self):
        """will compare user's expenses with ideal budget and return values that will be used in chart."""
        ideal_spending = self.get_ideal_spending() #Ideal spending percentages per category, dict
        actual_spending = self.budget.get_all_totals() #Instance of getting on totals $ of categories, dict

        percent_diffs = {
            'Needs': round((actual_spending['Needs']/self.monthly_income - self.ideal_percents['Needs']) * 100),
            'Wants': round((actual_spending['Wants']/self.monthly_income - self.ideal_percents['Wants']) * 100),
            'Savings': round((actual_spending['Savings']/self.monthly_income - self.ideal_percents['Savings']) * 100)
        } #Gets percentage difference of actual spending vs ideal, rounds up to integer
        dollar_diffs = {
            'Needs': round(actual_spending['Needs'] - ideal_spending['Needs'], 2),
            'Wants': round(actual_spending['Wants'] - ideal_spending['Wants'], 2),
            'Savings': round(actual_spending['Savings'] - ideal_spending['Savings'], 2)
        } #Gets the dollar difference between actual spending vs ideal, rounds up 2 decimals
        
        return percent_diffs, dollar_diffs #Returns tuple individually
        