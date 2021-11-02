import streamlit as st
import pandas as pd

sidebar = st.sidebar
import plotly.graph_objs as go
import plotly.express as px

sidebar.title("Sidebar Title Here") 

btn1 = sidebar.button("Get Ballons")

if btn1:
    st.balloons()

st.title("Pokemon Data")

NAME =st.text_input("Enter Your Name")
btn = st.button("Submit")
 

if btn:
     st.text(f"You entered name {NAME}")


st.image("bit.jpg")  
df = pd.read_csv("Pokemon.csv")  
st.dataframe(df) 
fig= px.bar( data_frame= df, x=  'Name', y= 'Speed', color="Type 1" )
st.plotly_chart(fig, use_container_width= True)
fig1 = px.scatter_3d( data_frame=df, x = "Attack", y = "Defense", z = "HP", opacity=0.7, height=1000, template='plotly_dark', color= "Type 1" )
st.plotly_chart(fig1)


