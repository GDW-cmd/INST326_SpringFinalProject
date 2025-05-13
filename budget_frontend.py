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

    date_selected = st.date_input("Select Date", datetime.now())   #Date input for the month of the budget
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
    selected_month = st.selectbox("Analyze month:", options=available_months, index=0,key="analysis_month")
    month_data = st.session_state.expenses[selected_month]
    
    if month_data['expenses'] and month_data['income'] > 0:
        viz = BudgetVisualization(month_data['expenses'], month_data['income'])
        #Category Pie Chart
        st.pyplot(viz.user_category_chart())
        st.subheader("Category Details")
        st.divider()
        category_totals = viz.calculate_totals_cat()
        if category_totals:
            category_df = pd.DataFrame({
                "Category": category_totals.keys(),
                "Total": [f"${cost:.2f}" for cost in category_totals.values()]

            })
            st.dataframe(category_df)
            
        #Individual Pie Chart
        st.pyplot(viz.user_individual_chart())
        st.subheader("Expense Details")
        #Displays Individual Expenses
        if month_data['expenses']:
            selected_df = pd.DataFrame.from_dict(month_data['expenses'], orient='index').reset_index()
            selected_df.columns = ["Expense", "Cost", "Category"]
        else:
            selected_df = pd.DataFrame(columns=["Expense", "Cost", "Category"])
        st.dataframe(selected_df)



with tab3:
   with tab3:
    selected_month = st.selectbox("Compare month:", options=available_months,index=0,key="compare_month")
    month_data = st.session_state.expenses[selected_month]

    #Check and convert to DataFrame
    if month_data['expenses']:
        selected_df = pd.DataFrame.from_dict(month_data['expenses'], orient='index').reset_index()
        selected_df.columns = ["Expense", "Cost", "Category"]
    else:
        selected_df = pd.DataFrame(columns=["Expense", "Cost", "Category"])

    #Display message if income is not set
    if month_data['income'] == 0.0:
        st.warning(f"No income set for {selected_month}. Please enter income.")
    elif selected_df.empty:
        st.warning(f"No expenses recorded for {selected_month}. Please enter expense.")
    else:
        #Display charts if data is present
        st.subheader(f"Data for {selected_month}")
        st.dataframe(selected_df)
        viz = BudgetVisualization(month_data['expenses'], month_data['income'])
        st.pyplot(viz.ideal_budget())
        st.pyplot(viz.comparition_chart())
        st.text("After this we will give a more detailed analysis of user data. Probably show in a data structure of percentage differences, and also show differences in text data in money/percent")

