import streamlit as st, pandas as pd
import requests
from bs4 import BeautifulSoup
import time

st.header('Indian Stock Dashboard')


ticker = st.sidebar.text_input('Symbol Code','INFY')
exchange = st.sidebar.text_input('Exchange','NSE')

url = 'https://www.google.com/finance/quote/' + ticker + ':' + exchange + '?hl=en' 

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
price = float(soup.find(class_="YMlKec fxKbKc").text.strip()[1:].replace(",",""))
previous_close = float(soup.find(class_="P6K39c").text.strip()[1:].replace(",",""))
revenue = soup.find(class_="QXDnM").text
about = soup.find(class_="bLLb2d").text

dict1 = {'Price': price,
         'Previous Price': previous_close,
         'Revenue': revenue,
         'About': about
        }

df = pd.DataFrame(dict1, index=['Extracted Data']).T

st.write(df)

#st.write(previous_close)
#st.write(revenue)
#st.write(about)