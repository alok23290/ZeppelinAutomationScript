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
                    print("input notebook exist : "+ nblist.strip() )
                else: raise MyExceptionWithContext()
        except IOError:
            print("Given File doesn't exist")

    def nbRunPostRequest(self,nbName):
        self._nbID = ''
        for id,name in  self.nbInfo.items():
            if name == nbName:
                self._nbID = id

        print('http://'+self.host+":"+self.port+'/api/notebook/job/'+self._nbID)

        return 'http://'+self.host+":"+self.port+'/api/notebook/job/'+self._nbID


b = NbRun()

b.nbExist()

b.nbRunPostRequest("spark_data_profiler")

print(b.nbInfo)



