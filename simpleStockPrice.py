import yfinance as yf 
import streamlit as st
import pandas as pd

#Markdown language is used to write down text using streamlit
st.write("""
# Simple Stock Price App

The below are the stocks closing down price and volume of Google stocks

""")

#defining ticker symbols
# a ticket symbol for Google is assigned to an object
tickerSymbol = 'GOOGL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the data from tickerData
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

#Open High Low Close Volume Dividents Stock Splits -- this is the columns of the data.

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)