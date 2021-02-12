# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:45:55 2021

@author: Bruker
"""
import yfinance as yf
from notion.client import NotionClient
from datetime import datetime

client = NotionClient(token_v2="ae22232f92cbfd4c3bf027ed2f5ce55b8b8f471dc74025f3335b7b4d258e5d2e774dce7d1118f5ec40bb149b50afa43588ccc0d5bdaa2f488f4ad12e3637a5bbf91508521808fb2342509584a208")

cv = client.get_collection_view("https://www.notion.so/43532570e34542c58408b23a43712f32?v=0dcc7d519c354a2ab56fcb3fc9499e5d")
cv.collection.add_row()

tickers = ['AAPL', 'PLTR', 'PEP']

for ticker in tickers:
    price = yf.Ticker(ticker)
    row = cv.collection.add_row()
    
    hist = price.history(period="1d")
    
    #information:
    row.Stock = ticker   
    row.Date = datetime.today().strftime('%Y-%m-%d')
    row.Close = float(round((hist.Close[0]), 2))
    row.Open = float(round((hist.Open[0]), 2))
    row.Volume = float(round((hist.Volume[0]), 2))
    row.High = float(round((hist.High[0]),2))
    row.DayReturn = float(round(((hist.Close[0])-(hist.Open[0]))/(hist.Open[0])*100, 2))
    