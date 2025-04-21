# This class holds unit tests for the methods of all the other classes 

import unittest
from budget import Budget 


def setUp(self):
    self.budget = Budget(5000) # initialize monthly income
    # add expenses
    self.budget.add_expense(100, 'need', 'Rent') 
    self.budget.add_expense(200, 'want', 'Entertainment')
