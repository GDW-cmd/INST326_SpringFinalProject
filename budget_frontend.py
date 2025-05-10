# This class creates a basic GUI for the program using streamlit.

import streamlit as st
from budget import Budget
from budget_visualization import BudgetVisualization
import pandas as pd
from datetime import datetime




#Initialize Empty Dictionary
if 'expenses' not in st.session_state:
    st.session_state.expenses = {}  


st.title("Personal Budget Tracker 💰") #Title 


tab1, tab2, tab3 = st.tabs(["Input 📝", "Spending Analysis 📊", "Comparitive Analysis 🎯"]) #Creates tab for input and output(charts for now)

with tab1:

    date_selected = st.date_input("Select a date", datetime.now())   #Date input for the month of the budget
    mm_yr_format = date_selected.strftime("%Y-%m")          #Format date to YYYY-MM

    if mm_yr_format not in st.session_state.expenses:
        st.session_state.expenses[mm_yr_format] = {
            'expenses': {},
            'income': 0.0
        }

    data_current = st.session_state.expenses[mm_yr_format]


    monthly_income = st.number_input("Monthly Income", min_value = 0.0, step = 0.01, format = "%0.2f", value=data_current['income'],key=f"income_{mm_yr_format}") #Monthly income input
    data_current['income'] = monthly_income


    with st.form("expense_form"): #Expense form for all expense inputs, expense: cost, category[want, need, or saving] 
        expense_name = st.text_input("Expense Name", placeholder="e.g., Rent, Groceries, Subscriptions") #Text input for the expense name/description
        expense_category = st.selectbox("Categorize your expense", options = ["Needs", "Wants", "Savings"], help = "Select whether this expense is a Need, Want, or Saving") #Select box for the expense category
        expense_cost = st.number_input("Enter monthly cost", min_value = 0.0, step = 0.01,format = "%0.2f") #Number input for expense cost
        submitted = st.form_submit_button("Add") #Submit button 

        if submitted:
            if not expense_name:
                st.warning("Please enter an expense name.")
            else:
                data_current['expenses'][expense_name] = {
                    'cost': expense_cost,
                    'category': expense_category
                }
                st.success("Expense added successfully!")

    # select and view separate months
    available_months = sorted(st.session_state.expenses.keys(), reverse=True)
    selected_view_month = st.selectbox(
        "View expenses for:", 
        options=available_months,
        index=0
    )
    
    #Display the expenses for selected month
    st.subheader(f"Expenses for {selected_view_month}")
    selected_data = st.session_state.expenses[selected_view_month]['expenses']
    if selected_data:
        st.session_state.expenses_df = pd.DataFrame.from_dict(
            selected_data,
            orient='index'
        ).reset_index()
        st.session_state.expenses_df.columns = ["Expense", "Cost", "Category"]
        st.dataframe(st.session_state.expenses_df)
    else:
        st.session_state.expenses_df = pd.DataFrame(columns=["Expense", "Cost", "Category"])
        st.write("No expenses in this month")



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

