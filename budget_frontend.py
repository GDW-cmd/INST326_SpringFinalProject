# This class creates a basic GUI for the program using streamlit.

import streamlit as st
from budget import Budget
from budget_visualization import BudgetVisualization
import pandas as pd



#Initialize Empty Dictionary
if 'expenses' not in st.session_state:
    st.session_state.expenses = {}
if 'expenses_df' not in st.session_state:
    st.session_state.expenses_df = pd.DataFrame(columns=["Expense", "Cost", "Category"])

st.title("Personal Budget Tracker 💰") #Title 


tab1, tab2, tab3 = st.tabs(["Input 📝", "Spending Analysis 📊", "Comparitive Analysis 🎯"]) #Creates tab for input and output(charts for now)

with tab1:
    monthly_income = st.number_input("Monthly Income", min_value = 0.0, step = 0.01, format = "%0.2f") #Monthly income input
    


    with st.form("expense_form"): #Expense form for all expense inputs, expense: cost, category[want, need, or saving] 
        expense_name = st.text_input("Expense Name", placeholder="e.g., Rent, Groceries, Subscriptions") #Text input for the expense name/description
        expense_category = st.selectbox("Categorize your expense", options = ["Need", "Want", "Saving"], help = "Select whether this expense is a Need, Want, or Saving") #Select box for the expense category
        expense_cost = st.number_input("Enter monthly cost", min_value = 0.0, step = 0.01,format = "%0.2f") #Number input for expense cost
        submitted = st.form_submit_button("Add") #Submit button 

        if submitted:
            if not expense_name:
                st.warning("Please enter an expense name.") #If no expense name.
            else:
                new_expense = pd.DataFrame(
                [{"Expense": expense_name, "Cost": expense_cost, "Category": expense_category}]
            )
            st.session_state.expenses_df = pd.concat(
                [st.session_state.expenses_df, new_expense], ignore_index=True
            )

    st.subheader("Your Expenses")
    if not st.session_state.expenses_df.empty:
        st.dataframe(st.session_state.expenses_df)
    else:
        st.write("None")

with tab2:
    if not st.session_state.expenses_df.empty and monthly_income > 0:

        # Convert dataFrame to dictionary
        expenses = {
            row["Expense"]: {"cost": row["Cost"], "category": row["Category"]}
            for _, row in st.session_state.expenses_df.iterrows()
        }

        viz = BudgetVisualization(expenses, monthly_income)

        #Category Pie Chart
        st.pyplot(viz.user_category_chart())
        st.subheader("Category Details")
        category_totals = viz.calculate_totals_cat()
        for category, cost in category_totals.items():
            st.write(f"{category}: ${cost:.2f}")

        #Individual Pie Chart
        st.pyplot(viz.user_individual_chart())
        st.subheader("Expense Details")
        for _, row in st.session_state.expenses_df.iterrows():
            st.write(f"Expense: {row['Expense']}, Category: {row['Category']}, \nCost: ${row['Cost']:.2f}")


with tab3:
    expenses = {
        row["Expense"]: {"cost": row["Cost"], "category": row["Category"]}
        for _, row in st.session_state.expenses_df.iterrows()
    }

    viz = BudgetVisualization(expenses, monthly_income)
    st.pyplot(viz.ideal_budget())
    st.subheader("This is an basic ideal budget")
    st.pyplot(viz.comparition_chart())
    st.text("After this we will give a more detailed anaylsis of user data. Probably show in a data structure of percentage differences, and also show differences in text data in money/percent")

