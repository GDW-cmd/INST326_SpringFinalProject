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
        self.expense_dict = {
            'rent': {'cost': 1500.00, 'category': 'Need'}, #our need 
            'groceries': {'cost': 320.00, 'category': 'Need'}, #our need 
            'subscriptions': {'cost': 70.00, 'category': 'Want'}, #our want 
            'video games': {'cost': 120.00, 'category': 'Want'}, #our want  
            'saving account': {'cost': 300.00, 'category': 'Saving'} #our saving  
        } 
        #This is just a test value the customer would have to put their own income in this instance 
        self.monthly_income = 4000
        self.analysis = (self.expense_dict, self.monthly_income)

    #testing ideal situation 
    def test_get_ideal_spending(self):
        result = self.analysis 
        expected_spent = {'Needs': 2000 , 'Wants': 1200, 'Saving': 8000}
        self.assertEqual(result, expected_spent) 
    
    # This test is to find the percent and dollar difference between real and ideal budget
    def test_budget_differences(self):
        percent_diffs, dollar_diffs = self.analysis.budget_differences()

    
    


      
if __name__ == '__main__':
    unittest.main() 

