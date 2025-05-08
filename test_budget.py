# This class holds unit tests for the methods of all the other classes 

import unittest
from budget import Budget 
from budget_analysis import BudgetAnalysis

class TestBudget(unittest.TestCase):
    def setUp(self):
        self.predefined_expense_dict = {
            'rent': {'cost': 1500.00, 'category': 'Need'},
            'groceries': {'cost': 320.00, 'category': 'Need'},
            'subscriptions': {'want': 70.00, 'category': 'Want'},
            'video games': {'want': 120.00, 'category': 'Want'},
            'saving account': {'want': 300.00, 'category': 'Saving'}
        }
        self.budget = Budget(self.predefined_expense_dict) 
    
    def test_get_total_savings(self):
        self.assertEqual(self.budget.get_total_savings(),300) 
        
    
    def test_get_total_needs(self):
        self.assertEqual(self.budget.get_total_needs(),1820)
        

    def test_get_total_wants(self):
        self.assertEqual(self.budget.get_total_wants(),190)
      
if __name__ == '__main__':
    unittest.main() 