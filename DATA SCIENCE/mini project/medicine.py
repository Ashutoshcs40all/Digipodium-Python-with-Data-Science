import streamlit as st
import pandas as pd
from PIL import Image


st.write("""
# Medicine Inventory Application
**Visually** show data on a Medicine! 
""")

image = Image.open("OIP.jpg")
st.image(image, use_column_width= True)

sidebar = st.sidebar

sidebar.header('Dashboard Home')

options = ['Add Data', 'View Data']
selOption = sidebar.selectbox('Select any option', options)

def get_input():
     Id_No = st.sidebar.text_input("Id_No")
     Customer_Name = st.sidebar.text_input("Customer")
     Medicine_Name = st.sidebar.text_input("Medicine")
     Manufectore_Date = st.sidebar.text_input("Manufectore")
     Puraches_Date = st.sidebar.text_input("Puraches_Date")
     Medicine_Stock = st.sidebar.text_input("Medicine_Stock")
     Return_Date= st.sidebar.text_input("Return_Date")

 
def viewData():
     st.header('View Data Header')

if selOption == options[0]:
     get_input()
elif selOption == options[1]:
     viewData()

btn = sidebar.button("Save Data")     



