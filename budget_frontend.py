# This class creates a basic GUI for the program using streamlit.

import streamlit as st
from budget import Budget

st.title("Basic Budget Tracker") #Title

monthly_income = st.number_input("Monthly Income", min_value = 0.0, step = 0.01, format = "%0.2f") #Monthly income input
st.write("The current number is ", monthly_income) #Shows monthly income input

with st.form("expense_form"): #Expense form for all expense inputs, expense: cost, category[want, need, or saving] 
    expense_name = st.text_input("Expense Name", placeholder="e.g., Rent, Groceries, Subscriptions") #Text input for the expense name/description
    expense_category = st.selectbox("Category", options = ["Need", "Want", "Saving"], help = "Select whether this expense is a Need, Want, or Saving") #Select box for the expense category
    expense_cost = st.number_input("Expense monthly cost", min_value = 0.0, step = 0.01,format = "%0.2f") #Number input for expense cost
    submitted = st.form_submit_button("Add Expense") #Submit button