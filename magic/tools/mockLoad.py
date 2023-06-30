import requests
import json
import pandas as pd
from datetime import datetime, timedelta

from tools.utils import market_api_call, json_to_df, convert_period

from configs import (
    MARKET_URL,
    SYMBOL,
    API_RESOLUTION,
    TIME_FRAME,
    CURRENT_DATE,
    LONG_PERIOD,
    SHORT_PERIOD,
    MOCK_D_PATH,
    ENV
)


def generate_mock_data():
    print("Generating mock data ...")
    data = None
    now = datetime.now()
    data = market_api_call(
        symbol=SYMBOL,
        resolution=API_RESOLUTION,
        from_ts=str(round((now - timedelta(hours= convert_period(LONG_PERIOD))).timestamp())),
        to_ts=str(round(now.timestamp())),
    )
    with open(MOCK_D_PATH + "mock_{0}_{1}.json".format(SYMBOL, API_RESOLUTION), "w") as outfile:
        outfile.write(json.dumps(data, indent=4))

        outfile.close()
    print("Mock data generated ...")


def load_mock_data():
    print("Loading mock data ...")
    data = None
    with open(MOCK_D_PATH + "mock_{0}_{1}.json".format(SYMBOL, API_RESOLUTION), "r") as file:
        data = json.load(file)

        file.close()
    df = json_to_df(data)
    return df