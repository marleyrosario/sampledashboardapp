# File: trends_app.py

import streamlit as st
from pytrends.request import TrendReq
import pandas as pd

# title of the app
st.title('Google Trends Visualizer')

# user input
keyword = st.text_input("Enter a keyword", '')

if keyword:
    # create a pytrends object
    pytrends = TrendReq(hl='en-US', tz=360)
    
    # build the payload
    pytrends.build_payload([keyword], timeframe='today 1-m')
    
    # get Google Trends data
    df = pytrends.interest_over_time()
    
    # plot data
    st.line_chart(df[keyword])
