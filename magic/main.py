
from tools.loader import load_real_data
from tools.determiner import master_mind
from tools.action import makeAction

from tools.mockLoad import generate_mock_data, load_mock_data
from configs import *

if __name__ == "__main__":
    print("Server Start ...")
    if GEN_MOCK:
        generate_mock_data()
    # while(True):
    historical_data = None
    if ENV == 'DEV':
        historical_data = load_mock_data()
    else:
        historical_data = load_real_data()

    
    prediction = master_mind(historical_data, TIME_FRAME)


    makeAction()