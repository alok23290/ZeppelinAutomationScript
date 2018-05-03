import sys
from runmyzeppelin.extract import Extract
from runmyzeppelin.notebookrun import NbRun


class Run(object):

    if __name__ == "__main__":
        if sys.argv[1] == 'extract':
            c = Extract()
            c.executeGetRequest()
        elif sys.argv[1] == 'notebook':
            d = NbRun()
            d.executePostRequest()
        else : print("Given Mode is not defined " + sys.argv[1])


