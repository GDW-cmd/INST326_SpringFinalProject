# This class creates a basic GUI for the program using streamlit.

import streamlit as st
from budget import Budget
from budget_visualization import BudgetVisualization


#Initialize Empty Dictionary
if 'expenses' not in st.session_state:
    st.session_state.expenses = {}

st.title("Basic Budget Tracker") #Title 


tab1, tab2, tab3 = st.tabs(["Input", "Output:Charts", "Ideal Budget Comparitive"]) #Creates tab for input and output(charts for now)

with tab1:
    monthly_income = st.number_input("Monthly Income", min_value = 0.0, step = 0.01, format = "%0.2f") #Monthly income input
    st.write("The current number is ", monthly_income) #Shows monthly income input

    with st.form("expense_form"): #Expense form for all expense inputs, expense: cost, category[want, need, or saving] 
        expense_name = st.text_input("Expense Name", placeholder="e.g., Rent, Groceries, Subscriptions") #Text input for the expense name/description
        expense_category = st.selectbox("Category", options = ["Need", "Want", "Saving"], help = "Select whether this expense is a Need, Want, or Saving") #Select box for the expense category
        expense_cost = st.number_input("Expense monthly cost", min_value = 0.0, step = 0.01,format = "%0.2f") #Number input for expense cost
        submitted = st.form_submit_button("Add Expense") #Submit button 

        if submitted:
            if not expense_name:
                st.warning("Please enter an expense name.") #If no expense name.
            else:
                st.session_state.expenses[expense_name] = {'cost': expense_cost, 'category': expense_category}
                st.success(f"Added '{expense_name}' as a {expense_category} with monthly cost of ${expense_cost}.") #Displays last expense and category + cost.

    st.subheader("Your Expenses")
    if st.session_state.expenses:
        st.write(st.session_state.expenses)
    else:
        st.write("None")

with tab2:
    if st.session_state.expenses and monthly_income > 0:
        viz = BudgetVisualization(st.session_state.expenses, monthly_income)

        #Category Pie Chart
        st.pyplot(viz.user_category_chart())
        st.subheader("Category Details")
        category_totals = viz.calculate_totals_cat()
        for category, cost in category_totals.items():
            st.write(f"{category}: ${cost:.2f}")

        #Individual Pie Chart
        st.pyplot(viz.user_individual_chart())
        st.subheader("Expense Details")
        for name, values in st.session_state.expenses.items():
            category = values["category"]
            cost = values["cost"]
            st.write(f"Expense: {name}, Category: {category}, Cost: ${cost:.2f}")

with tab3:
    st.subheader("Brief summary about 20/30/50 rule which is ideal base budget, and then shows data on how far or close user is to it.")

