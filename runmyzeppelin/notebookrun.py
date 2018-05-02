import requests
from runmyzeppelin.notebook import Notebook
from runmyzeppelin.exception import MyExceptionWithContext

class NbRun(object):

    def __init__(self):
        self.nb = Notebook()

    def getNotebookID(self):
        getURL = self.nb.get_list_of_notes()
        r = requests.get(url=getURL)
        data = r.json()
        json_data = data['body']
        subdict = {}
        for item in json_data:
            new_key=item['id']
            nameval= item['name']
            if "/" in nameval:
                new_value = item['name'].split("/")[-1]
            else :
                new_value = item['name']

            subdict[new_key]=new_value
        print(subdict)
        return subdict


    def nbExist(self,inpNB):
        if inpNB in self.getNotebookID().values():
            print("input notebook exist : "+ inpNB )
        else:
            raise MyExceptionWithContext()

    def nbRunPostRequest(self,nbName):
        self._nbID = ''
        self._nbName = ''
        for id,name in  self.getNotebookID().items():
            if name == nbName:
                self._nbID = id
                self._nbName = nbName
        # print(self.nb.post_run_all_paragraphs() + self._nbID)
        return self.nb.post_run_all_paragraphs() + self._nbID

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


