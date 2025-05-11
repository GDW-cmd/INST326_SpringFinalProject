class Budget:
    '''
    This class gets all totals dollar amount of each category.

    Attributes:
        expense_dict (dict): user expense dict, Expense Name as key, then Category and Cost as values.
    '''


    def __init__(self, expense_dict): 
        self.expense_dict = expense_dict
        

    def get_total_savings(self):
        """
        Return sum of savings
        
        Returns:
            float: Sum of all expenses categorized as savings
        """
        return sum(
            expense['cost'] for expense in self.expense_dict.values() if expense['category'].lower() == 'savings')
        
    
    def get_total_needs(self):
        """
        Return sum of needs
        
        Returns:
            float: Sum of all expenses categorized as needs
        """
        return sum(
            expense['cost'] for expense in self.expense_dict.values() if expense['category'].lower() == 'needs')

    def get_total_wants(self):
        """
        Return sum of wants, needs, and savings
        
        Returns:
            dict: dictionary of all summed totals for each budget category:
        """
        return sum(
            expense['cost'] for expense in self.expense_dict.values() if expense['category'].lower() == 'wants') 
     
    def get_all_totals(self):
        """Returns dict of category : cost"""
        return {
            "Needs": self.get_total_needs(),
            "Wants": self.get_total_wants(),
            "Savings": self.get_total_savings()
        }
    

