import streamlit as st
import pandas as pd
from PIL import Image

st.write("""
# Stock Market Web Application
**Visually** show data on a stock! Data range From NOV 11,2020 - NOV 11, 2021
""")

image = Image.open("Stock.jpg")
st.image(image, use_column_width= True)

st.sidebar.header('User Input')

def get_input():
     start_date = st.sidebar.text_input ("Start Date", "2020-11-11")
     end_date = st.sidebar.text_input("End_Date", "2021-11-10")
     stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
     return start_date, end_date, stock_symbol


def get_comapny_name(symbol):
     if symbol == "AMZN":
          return 'Amazon'
     elif symbol == "TSLA":
          return 'Tesla'
     elif symbol == "GOOG":
          return 'ALphabet'
     else:
          'NONE'



def get_data(symbol, start, end):

     if symbol.upper() =='AMZN':
          df = pd.read_csv("AMZN.csv")
     elif symbol.upper() == 'TSLA':
          df = pd.read_csv("TSLA.csv")
     elif symbol.upper() == 'GOOG':
          df = pd.read_csv("GOOG.csv")
     else:
          df= pd.DataFrame(columns={'Date','Open','High','Low','Close','Adj Close','Volume'})  

     start = pd.to_datetime(start)
     end =  pd.to_datetime(end)  

     start_row = 0
     end_row = 0

     for i in range (0, len(df)):
          if start <= pd.to_datetime(df['Date'][i] ):
               start_row = i
               break
     for j in range (0, len(df)):
          if end >= pd.to_datetime(df['Date'][len(df)-1-j]):  
               end_row = len(df)-1-j
               break

     df = df.set_index(pd.DatetimeIndex(df['Date'].values))


     return df. iloc[start_row:end_row +1, :]

start, end, symbol = get_input()

df= get_data(symbol, start, end)

company_name = get_comapny_name(symbol.upper())

st.header(company_name+" Close price\n")
st.line_chart(df['Volume'])

st.header('Data Statistics')
st.write(df.describe())

                  



