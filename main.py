import numpy as np
import pandas as pd
import streamlit as st
import requests
from datetime import datetime
import yfinance as yf
from iexfinance.stocks import Stock, get_historical_data
import matplotlib.pyplot as plt
from PIL import Image
# from secrets import IEX_CLOUD_API_TOKEN
IEX_CLOUD_API_TOKEN = "pk_8e2a036135224e6986bdcc0151e51f2d"
# from secrets import IEX_CLOUD_API_TOKEN
#GET /ref-data/cryptos/symbols
base_url = 'https://cloud.iexapis.com/v1'
st.write("""
# All-in-one Crypto Website

This Website illustrates essential data for your journey in cryptocurrency investments
""")
month = ['January', 'February', 'March', 'April', 'May', 'June',
'July', 'August', 'September', 'October', 'November', 'December']
image = Image.open('PVhub.png')
st.image(image, caption='Project Valuehub, Designed for New Generation Investors')
st.sidebar.header("Select Currencies")
currency_choices = ['ETH', 'BTC', 'USD', 'BNB', 'USDT']
currency = st.sidebar.selectbox("Choose an Endpoint", currency_choices)
st.subheader("All Cryptos information allow for selection")
st.sidebar.header('Select Date and Time')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950, 2020))))
selected_month = st.sidebar.selectbox('Month', month)
end_point = '/ref-data/crypto/symbols'
api_url = f'{base_url}{end_point}?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()
df = pd.DataFrame(data=data)
df2 = df[df['currency'] == currency]
st.write(df2)
st.write("Current Price")
list = ['btcusd', 'ethusd', 'avaxusdt', 'usdcusdt']
for i in range(4):
    symbol = list[i]
    end_point = f'/crypto/{symbol}/price'
    api_url = f'{base_url}{end_point}?token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(api_url).json()
    df = pd.DataFrame(data=data, index = [0])
    st.write(df)

st.write("Current Booking Information")
for i in range(4):
    symbol = list[i]
    end_point = f'/crypto/{symbol}/quote'
    api_url = f'{base_url}{end_point}?token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(api_url).json()
    df = pd.DataFrame(data=data, index = [0])
    st.write(df)

cryptocurrencies = ['BTC-USD', 'ETH-USD', 'XRP-USD','DOGE-USD']
for i in range(4):
    tickerData = yf.Ticker(cryptocurrencies[i])
    tickerDf = tickerData.history(period = '1d', start = '2018-5-31', end = '2022-6-12')
    st.write("The graph of Closing " + cryptocurrencies[i] + " are as follows:")
    st.line_chart(tickerDf.Close)
    st.write("The graph of Volume " + cryptocurrencies[i] + " are as follows:")
    st.line_chart(tickerDf.Volume)

st.sidebar.header("Crypto News")
endpoint_choices = ['Assets', 'Events', 'Rarity']
endpoint = st.sidebar.selectbox("Event Types", endpoint_choices)

spy = Stock("SPY", output_format = 'pandas', token = IEX_CLOUD_API_TOKEN)
start = datetime(2022, 4, 18)
end = datetime(2022, 4, 22)
df = get_historical_data("TSLA", start, end, output_format = 'pandas', token = IEX_CLOUD_API_TOKEN)
st.write(df)


st.title(f"Cryptocurrencies News and Events")
crypto_lst = ['BTC', 'ETH', 'XRP','DOGE']
# for item in crypto_lst:
#     endpoint = f'/stock/{symbol}/news/last/{last}'
#     data = requests.get(url).json()
#     df = pd.DataFrame(data=data)

    





