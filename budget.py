# This file takes the user input of expense and income and calculates the total expenses, based on different categories and savings

class Budget:
    '''
    This class takes user's income and expenses and catrgorizes them into wants, needs and savings.

    Attributes:
        monthly_income (float): user's monthly income
        expenses (list): user's expenses {amount, category_name, category_type, description}
        savings (list):user savings {amount, description}
    '''



    """ Will do later

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
    """
    


    def __init__(self, expense_dict): 
        self.expense_dict = expense_dict
        

    def add_expense(self, amount, category_name, description="", category_type=None):
        """
        Function adds an expense to needs or wants categories
        """
        pass

    def get_total_savings(self):
        """Return the total of savings"""
        pass
    
    def get_total_needs(self):
        """Return sum of needs"""
        pass

    def get_total_wants(self):
        """Return sum of wants"""
        pass
    

