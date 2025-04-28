# This class creates a basic GUI for the program using streamlit.

import streamlit as st
from budget import Budget

st.title("Basic Budget Tracker") #Title

monthly_income = st.number_input("Monthly Income", min_value = 0.0, step = 0.01, format = "%0.2f") #Monthly income input
st.write("The current number is ", monthly_income) #Shows monthly income input


            