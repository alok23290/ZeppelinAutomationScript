from runmyzeppelin.notebook import Notebook
from runmyzeppelin.exception import MyExceptionWithContext

class NbRun(object):

    nbInfo = {}
    host =''
    port =''
    def __init__(self):
        nb = Notebook()
        self.nbInfo = nb.getNotebookID()
        self.host = Notebook.host
        self.port = Notebook.port

    def nbExist(self):
        try:
            notebookImport = open("/Users/aloktiwari/PycharmProjects/ZeppelinAutomationScript/notebook_list")
            for nblist in notebookImport:
                if nblist.strip() in self.nbInfo.values():
                else: raise MyExceptionWithContext()
        except IOError:
            print("Given File doesn't exist")

b = NbRun()

b.nbExist()
print(b.nbInfo)

