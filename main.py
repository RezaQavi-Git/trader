
from tools.loader import dataLoader
from tools.determiner import determiner
from tools.action import makeAction

def main():

    print("Server Start ...")
    # while(True):
    dataLoader()
    determiner()
    makeAction()




main()
