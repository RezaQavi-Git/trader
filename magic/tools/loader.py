from datetime import datetime, timedelta
import pandas as pd

from configs import *
from tools.utils import market_api_call, json_to_df


def load_real_data():
    print("Loading realtime data ...")
    data = market_api_call(
        symbol=SYMBOL, 
        resolution=RESOLUTION, 
        from_ts=str(round((CURRENT_DATE - timedelta(SHORT_PERIOD)).timestamp())),
        to_ts=str(round(CURRENT_DATE.timestamp())),
    )
    df = json_to_df(data)
    print("Loading realtime data completed ...")

    return df
