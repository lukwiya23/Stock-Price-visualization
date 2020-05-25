import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

shown below are the stock closing price and volume of Google

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

#define the ticker symbol
tickerSymbol = 'GOOGL'

#get data of the ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices of the year

tickerDf = tickerData.history(period='1d', start='2015-5-31',end='2020-5-31')

#Open  High  Low close  Volume  Dividends  Stock splits