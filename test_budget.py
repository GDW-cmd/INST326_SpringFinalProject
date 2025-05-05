# This class holds unit tests for the methods of all the other classes 

import unittest
from budget import Budget 
from budget_analysis import BudgetAnalysis


def setUp(self):
    self.budget = Budget(5000) # initialize monthly income
    # add expenses
    self.budget.add_expense(100, 'need', 'Rent') 
    self.budget.add_expense(200, 'want', 'Entertainment')

def test_add_expense(self):
    '''
    test add_expense method
    '''
    pass 

def test_add_saving(self):
    '''
    test add_saving method
    '''
    pass

def test_get_category_total(self):
    '''
    test get_category_total method
    '''
    pass

def test_calculate_ideal(self):
    '''
    test calculate_ideal method
    '''
    pass

def test_compare_with_ideal(self):
    '''
    test compare_with_ideal method
    '''
    pass