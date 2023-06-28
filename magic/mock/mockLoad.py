import requests
import json
import pandas as pd
from datetime import datetime, timedelta

from ..configs import *
from core.configs import (MARKET_URL, 
                           SYMBOL, 
                           RESOLUTION, 
                           TIME_FRAME,
                           CURRENT_DATE,
                           LONG_PERIOD,
                           SHORT_PERIOD
                           )


def getMarketData(symbol: str, resolution: str, from_ts: int, to_ts:int):

    params = {
        'symbol': symbol,
        'resolution': resolution,
        'from': str(from_ts),
        'to': str(to_ts)
    }
    response = requests.get(MARKET_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Error:', response.status_code)
        return None


def dataLoader():
    print("Loading data ...")

    data = getMarketData(symbol=SYMBOL, 
                         resolution=  RESOLUTION, 
                         from_ts=1657653939, 
                         to_ts=1687756939
                         ) 

    df = pd.DataFrame(data)
    df = df[['t', 'c']]
    df.columns = ['ds', 'y']
    df['ds'] = pd.to_datetime(df['ds'], unit='s') 
    print("Data Loaded ...")
    return df

def generateMockData():
    print("Loading data ...")
    data = getMarketData(symbol= SYMBOL, 
                         resolution= RESOLUTION, 
                         from_ts= (CURRENT_DATE - timedelta(LONG_PERIOD).timestamp()), 
                         to_ts=CURRENT_DATE.timestamp()
                         ) 
    
    print("Data Loaded ...")
    with open('mock_{0}_{1}.json'.format(SYMBOL, RESOLUTION), 'w') as outfile:
        outfile.write(data)


generateMockData()