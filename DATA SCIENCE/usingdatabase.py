import streamlit as st
from streamlit.elements.arrow import Data
from databse import SmartPhone
from sqlalchemy.orm import  sessionmaker   ### object relationl mapping
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mydatabase.sqlite3")
Session = sessionmaker(engine)
session= Session()

sidebar = st.sidebar

sidebar.header("Add Smart phone Data here")
sidebar.markdown('---')

brand_v = sidebar.text_input('Brand')
name_v = sidebar.text_input('Name')
price_v = sidebar.number_input('Price')
ram_v = sidebar.text_input('Ram')
storage_v = sidebar.text_input('Storage')

btn = sidebar.button("Save Data")

if btn:
    try:
        myphone= SmartPhone(brand = brand_v, name= name_v, price= price_v, ram= ram_v, storage= storage_v)
        session.add(myphone)
        session.commit()

        st.success('Data Saved!!')
    except Exception as e:
        print(e)
        st.error('Error in saving data')   

st.header("Smartphone data saved: ")
st.markdown("---")

Data = session.query(SmartPhone).all()

print(Data)

entry1 = Data[0]
entry1= Data[0]
col1, col2, col3, col4, col5, col6, = st.columns(6)

col1.subheader("ID")
col2.subheader("BRAND")
col3.subheader("NAME")
col4.subheader("PRICE")
col5.subheader("RAM")
col6.subheader("STORAGE")

for entry in Data:
    col1.text(entry.id)
    col2.text(entry.brand)
    col3.text(entry.name)
    col4.text(entry.price)
    col5.text(entry.ram)
    col6.text(entry.storage)

st.header("Delete SmartPhone Data: ")
st.markdown("---")

search_id = st.text_input("Enter id to serch")
serch_btn = st.button("Serch")

if search_id and serch_btn:
    res = session.query(SmartPhone).filter_by(id=search_id).first()
    col7, col8, col9, col10, col11, col12 = st.columns(6)
    if res:
        col7.text(res.id)
        col8.text(res.brand)
        col9.text(res.name)
        col10.text(res.price)
        col11.text(res.ram)
        col12.text(res.storage)


