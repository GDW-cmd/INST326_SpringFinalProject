# File 1: budget.py
# This file takes the user input of expense and income and calculates the total expenses, based on different categories,
# and savings.


class Budget:
    '''
    This class takes user's income and expenses and catrgorizes them into wants, needs and savings.

    Attributes:
        monthly_income (float): user's monthly income
        expenses (list): user's expenses {amount, category_name, category_type, description}
        savings (list):user savings {amount, description}
    '''
