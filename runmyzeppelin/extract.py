import requests

from runmyzeppelin.notebookrun import NbRun


class Extract(NbRun):

    def nbRunPostRequest(self,nbName):
        """
        Overriding the method for get request for
        extraction of code
        """
        self._nbID = ''
        self._nbName = ''
        for id,name in  self.nbInfo.items():
            if name == nbName:
                self._nbID = id
                self._nbName = nbName
        # print('NOTEBOOK:'+self._nbName+'===>'+'http://'+self.host+":"+self.port+'/api/notebook/'+self._nbID)
        return 'http://'+self.host+":"+self.port+'/api/notebook/'+self._nbID

    def executeGetRequest(self):

        inp_nb = open("/Users/aloktiwari/PycharmProjects/ZeppelinAutomationScript/notebook_list")
        for nb in inp_nb:
            l = nb.strip().split(",")
            for j in l:
                self.nbExist(j)
                notebook_to_exexute = self.nbRunPostRequest(j)
                print("**********NOTEBOOK CONTENT EXTRACTION BEGINS**********")
                r = requests.get(url=notebook_to_exexute)
                data = r.json()
                return data

    def parser(self,content={}):

        print("****** PARSING BEGIN ******")
        json_data_1 = content['body']
        json_data_2 = json_data_1['paragraphs']
        # print(json_data_2)
        for item in json_data_2:
            new_key = item['text']
            print(new_key)


# c = Extract()
#
# print(c)
#
# c.nbRunPostRequest("spark_data_profiler_1")
#
# myelem = c.executeGetRequest()
# c.parser(myelem)


