
from tools.loader import dataLoader
from tools.determiner import determiner
from tools.action import makeAction
from configs import *

def main():

    print("Server Start ...")
    # while(True):
    historicalData = dataLoader()
    determiner(historicalData, TIME_FRAME)
    makeAction()




main()
