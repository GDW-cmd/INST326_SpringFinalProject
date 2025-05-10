# This class holds unit tests for the methods of all the other classes 

import unittest
from budget import Budget 
from budget_analysis import BudgetAnalysis

class TestBudget(unittest.TestCase):
    def setUp(self):
        """Initialize test data before each test"""
        self.predefined_expense_dict = {
            'rent': {'cost': 1500.00, 'category': 'Needs'}, #our need 
            'groceries': {'cost': 320.00, 'category': 'Needs'}, #our need 
            'subscriptions': {'cost': 70.00, 'category': 'Wants'}, #our want 
            'video games': {'cost': 120.00, 'category': 'Wants'}, #our want  
            'saving account': {'cost': 300.00, 'category': 'Savings'} #our saving  
        }
        self.budget = Budget(self.predefined_expense_dict) 
    
    def test_get_total_savings(self):
        self.assertEqual(self.budget.get_total_savings(),300)
        
    
    def test_get_total_needs(self):
        self.assertEqual(self.budget.get_total_needs(),1820)
        

    def test_get_total_wants(self):
        self.assertEqual(self.budget.get_total_wants(),190)

class TestBudget_analysis(unittest.TestCase): 
    def setUp(self):
        """Initialize test data before each test"""
        self.predefined_expense_dict = {
            'rent': {'cost': 1500.00, 'category': 'Need'}, #our need 
            'groceries': {'cost': 320.00, 'category': 'Need'}, #our need 
            'subscriptions': {'cost': 70.00, 'category': 'Want'}, #our want 
            'video games': {'cost': 120.00, 'category': 'Want'}, #our want  
            'saving account': {'cost': 300.00, 'category': 'Saving'} #our saving  
        }

      
if __name__ == '__main__':
    unittest.main() 

