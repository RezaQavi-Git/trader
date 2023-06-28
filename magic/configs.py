import os
from datetime import datetime

MARKET_URL = 'https://api.nobitex.ir/market/udf/history'

SYMBOL = 'TRXUSDT'
RESOLUTION = '5'
TIME_FRAME = '5m'

CURRENT_DATE = datetime.now()
LONG_PERIOD = 720
MID_PERIOD = 180
SHORT_PERIOD = 180



MOCK_D_PATH = os.getcwd() + '/../mockD/'


ENV = 'DEV'
GEN_MOCK = False