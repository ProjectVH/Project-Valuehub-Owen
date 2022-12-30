import numpy as np
import pandas as pd
import streamlit as st
import requests
from datetime import datetime
import matplotlib.pyplot as plt
from PIL import Image
import yfinance as yf

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
data_choices = ['價格追縱', '基本面分析', '新聞分析']
function = st.sidebar.selectbox("請選擇功能", data_choices)
if function == '新聞分析':
    st.sidebar.header("請選擇新聞來源: ")
    endpoint_choices = ['Assets', 'Events', 'Rarity']
    endpoint = st.sidebar.selectbox("Event Types", endpoint_choices)
 
start = datetime(2022, 4, 18)
end = datetime(2022, 4, 22)
