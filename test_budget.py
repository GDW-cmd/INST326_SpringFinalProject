# This class holds unit tests for the methods of all the other classes 

import unittest
from budget import Budget 
from budget_analysis import BudgetAnalysis


def setUp(self):
    self.budget = Budget(5000) # initialize monthly income
    # add expenses
    self.budget.add_expense(100, 'need', 'Rent') 
    self.budget.add_expense(200, 'want', 'Entertainment')

def test_get_total_savings(self):
    '''  '''
    pass 

def test_get_total_needs(self):
    '''    '''
    pass

def test_get_total_wants(self):
    '''    '''
    pass