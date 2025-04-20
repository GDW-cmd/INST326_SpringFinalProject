# This file takes the user input of expense and income and calculates the total expenses, based on different categories and savings
#Testtt

class Budget:
    '''
    This class takes user's income and expenses and catrgorizes them into wants, needs and savings.

    Attributes:
        monthly_income (float): user's monthly income
        expenses (list): user's expenses {amount, category_name, category_type, description}
        savings (list):user savings {amount, description}
    '''

    # create a dictionary of default categories
    DEFAULT_CATEGORIES = {
        'rent': 'need',
        'mortgage': 'need',
        'groceries': 'need',
        'dine-in/take out': 'want',
        'insurance': 'need',
        'utilities': 'need',
        'entertainment subscriptions': 'want',
        'social events': 'want',
        'gas': 'need',
        'phone bill': 'need',
        'internet bills': 'need'
    }
    
    def __init__(self, monthly_income): 
        self.monthly_income = monthly_income
        self.expenses = []
        self.savings = [] 
