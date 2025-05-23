# This class holds unit tests for the methods of all the other classes 

import unittest
from budget import Budget 
from budget_analysis import BudgetAnalysis
from budget_visualization import BudgetVisualization 
from matplotlib.figure import Figure 

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

class TestBudgetAnalysis(unittest.TestCase): 
    def setUp(self):
        """Initialize test data before each test"""
        self.expense_dict = {
            'rent': {'cost': 1500.00, 'category': 'Needs'}, #our need 
            'groceries': {'cost': 320.00, 'category': 'Needs'}, #our need 
            'subscriptions': {'cost': 70.00, 'category': 'Wants'}, #our want 
            'video games': {'cost': 120.00, 'category': 'Wants'}, #our want  
            'saving account': {'cost': 300.00, 'category': 'Savings'} #our saving  
        } 
        #This is just a test value the customer would have to put their own income in this instance 
        self.monthly_income = 4000
        self.analysis = BudgetAnalysis(self.expense_dict, self.monthly_income) 

    #testing ideal situation 
    def test_get_ideal_spending(self):
        result = self.analysis.get_ideal_spending() 
        expected_spent = {'Needs': 2000.0 , 'Wants': 1200.0, 'Savings': 800.0}
        self.assertEqual(result, expected_spent) 
    
    # This test is to find the percent and dollar difference between real and ideal budget
    def test_budget_differences(self):
        percent_diffs, dollar_diffs = self.analysis.budget_differences()
    
        expected_percent_diffs = {'Needs': -4, 'Wants': -25 , 'Savings': -12}
        expected_dollar_diffs = {'Needs': -180.0, 'Wants': -1010.0 , 'Savings': -500.0}

        self.assertEqual(percent_diffs, expected_percent_diffs)
        self.assertEqual(dollar_diffs, expected_dollar_diffs) 


class TestBudgetVisualization(unittest.TestCase): 
    def setUp(self):
        """Initialize test data before each test"""
        self.expense_dict = {
            'rent': {'cost': 1500.00, 'category': 'Needs'}, #our need 
            'groceries': {'cost': 320.00, 'category': 'Needs'}, #our need 
            'subscriptions': {'cost': 70.00, 'category': 'Wants'}, #our want 
            'video games': {'cost': 120.00, 'category': 'Wants'}, #our want  
            'saving account': {'cost': 300.00, 'category': 'Savings'} #our saving  
        } 
        # example income 
        self.monthly_income = 4000.00 

        # makeing the budget analysis so we can test it
        self.visual = BudgetVisualization(self.expense_dict, self.monthly_income)

    #to check if totals by category and leftover money are correct
    def test_calculate_totals_cat(self):
        result = self.visual.calculate_totals_cat()
        expected_total = {'Needs': 1820.0, 'Wants': 190.0, 'Savings': 300.0, 'Remaining': 1690.0
        }
        self.assertEqual(result, expected_total) 
    

    def test_user_category_chart(self):
        chart = self.visual.user_category_chart()
        self.assertIsInstance(chart, Figure)
    
    def test_user_individual_chart(self):
        chart = self.visual.user_individual_chart()
        self.assertIsInstance(chart, Figure)
    
    def test_ideal_budget(self):
        chart = self.visual.ideal_budget()
        self.assertIsInstance(chart, Figure)
    
    def test_comparition_chart(self):
        chart = self.visual.comparition_chart()
        self.assertIsInstance(chart, Figure)


if __name__ == '__main__':
    unittest.main() 

