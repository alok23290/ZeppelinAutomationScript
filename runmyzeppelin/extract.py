import requests

from runmyzeppelin.notebook import Notebook
from runmyzeppelin.notebookrun import NbRun
import os

class Extract(object):


    def __init__(self):
        self.nb1 = Notebook()
        self.nbrun = NbRun()


    def nb_data_request(self, nbName):
        """
        this method is used to construct the GET method for fetching the code from zeppelin notebook
        :param nbName: Notebook Name
        :return: string
        """
        self._nbID = ''
        self._nbName = ''
        for id,name in  self.nbrun.get_notebook_id().items():
            if name == nbName:
                self._nbID = id
                self._nbName = nbName
        # return 'http://'+self.host+":"+self.port+'/api/notebook/'+self._nbID
        print(self.nb1.get_notebook_data()+self._nbID)
        return self.nb1.get_notebook_data()+self._nbID


    def script_name(self,content={}):
        """
        return the notebook name when we pass dictionary of notebook elements
        :param content: dict
        :return: string
        """
        json_data_1 = content['body']
        json_data_2 = json_data_1['name']
        return json_data_2+"."+self.nb1.code_lang


    def code_parser(self,content={}):
        """
        this method parse the json data and return the code present in zeppelin notebook
        :param content: dict
        :return: string
        """
        print("****** PARSING BEGIN ******")
        json_data_1 = content['body']
        json_data_2 = json_data_1['paragraphs']

        code_string = ''
        for item in json_data_2:
            if 'text' in item:
                code_string += "\n"+"\n"+item['text']
        return code_string


    def code_language(self):

        """
        This function need to be implemented to avoid input from user side
        :param inp_data:
        :return: code language like Scala, Python
        """
        pass


    def create_code(self,code='',filename=''):
        """
        method used to write the parsed zeppelin's notebook content into their respective code files
        :param code: string
        :param filename: string
        :return: None
        """

        pwd = os.path.dirname(os.path.realpath(__file__))
        print("CURRENT DIRECTORY "+pwd)
        subdir = "code"

        filepath = os.path.join(pwd, subdir, filename)

        if not os.path.exists(os.path.join(pwd, subdir)):
            os.mkdir(os.path.join(pwd, subdir))

        # create an empty file.
        try:
            f = open(filepath, 'w')
            f.write(code)
            f.close()
        except IOError:
            print("Wrong path provided")


    def execute_get_request(self):
        """
        main method used to parse the content of zeppelin notebook and perform extraction
        :return: None
        """

        inp_nb = open("/Users/aloktiwari/PycharmProjects/ZeppelinAutomationScript/notebook_list")
        for nb in inp_nb:
            l = nb.strip().split(",")
            for j in l:
                self.nbrun.is_notebook_exist(j)
                notebook_to_exexute = self.nb_data_request(j)
                print("**********NOTEBOOK CONTENT EXTRACTION BEGINS**********")
                r = requests.get(url=notebook_to_exexute)
                code_data = r.json()

                # print(code_data)
                parsed_data=self.code_parser(code_data)
                input_script_name= self.script_name(code_data)

                print(input_script_name)

                print("STARTING CREATING CODE FILES")

                self.create_code(parsed_data,input_script_name)


