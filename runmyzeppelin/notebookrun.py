import requests
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

    # def nbExist(self):
    #     try:
    #         notebookImport = open("/Users/aloktiwari/PycharmProjects/ZeppelinAutomationScript/notebook_list")
    #         for nblist in notebookImport:
    #             if nblist.strip() in self.nbInfo.values():
    #                 print("input notebook exist : "+ nblist.strip() )
    #             else: raise MyExceptionWithContext()
    #     except IOError:
    #         print("Given File doesn't exist")

    def nbExist(self,inpNB):
        if inpNB in self.nbInfo.values():
            print("input notebook exist : "+ inpNB )
        else:
            raise MyExceptionWithContext()

    def nbRunPostRequest(self,nbName):
        self._nbID = ''
        self._nbName = ''
        for id,name in  self.nbInfo.items():
            if name == nbName:
                self._nbID = id
                self._nbName = nbName
        print('NOTEBOOK:'+self._nbName+'===>'+'http://'+self.host+":"+self.port+'/api/notebook/job/'+self._nbID)
        return 'http://'+self.host+":"+self.port+'/api/notebook/job/'+self._nbID

    def executePostRequest(self):
        inp_nb = open("/Users/aloktiwari/PycharmProjects/ZeppelinAutomationScript/notebook_list")
        for nb in inp_nb:
            l = nb.strip().split(",")
            for j in l:
                self.nbExist(j)
                notebook_to_exexute=self.nbRunPostRequest(j)
                print("**********NOTEBOOK RUN BEGINS**********")
                r = requests.post(url=notebook_to_exexute)
                data = r.json()
                print(data)
#
# a = NbRun()
# a.executePostRequest()

