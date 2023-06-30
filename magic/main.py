import time

from tools.loader import load_real_data
from tools.determiner import master_mind
from tools.action import make_action

from tools.mockLoad import generate_mock_data, load_mock_data

from configs import *

if __name__ == "__main__":
    print("Server Start ...")
    if GEN_MOCK:
        generate_mock_data()

    for i in range(300):
    # while True:
        print("turn: ", str(i))
        historical_data = None
        if ENV == "DEV":
            historical_data = load_mock_data()
        else:
            historical_data = load_real_data()

        prediction = master_mind(historical_data, TIME_FRAME)

        make_action(last_record=historical_data.iloc[-1], prediction=prediction)
        time.sleep(300)

    print("Server Shutdown ...")