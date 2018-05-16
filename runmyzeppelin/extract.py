import requests
from runmyzeppelin.notebookrun import NbRun
import os
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')

class Extract(object):
    """
    By using this class we can extract the code present in zeppelin notebook into corresponding code files
    """

    def __init__(self):
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
        logging.info("POST Request URL " + self.nbrun.nb.get_notebook_data()+self._nbID)
        return self.nbrun.nb.get_notebook_data()+self._nbID


    def script_name(self,content={}):
        """
        return the notebook name when we pass dictionary of notebook elements
        :param content: dict
        :return: string
        """
        json_data_1 = content['body']
        json_data_2 = json_data_1['name']
        return json_data_2+"."+self.nbrun.nb.code_lang


    def code_parser(self,content={}):
        """
        this method parse the json data and return the code present in zeppelin notebook
        :param content: dict
        :return: string
        """
        logging.info("****** Parsing is strated ******")
        json_data_1 = content['body']
        json_data_2 = json_data_1['paragraphs']

        code_string = ''
        for item in json_data_2:
            if 'text' in item:
                code_string += "\n"+"\n"+item['text']
        return code_string


    def extract_dependencies(self,code_string):
        """
        method used to extract all import statement
        :param code_string:
        :return: string
        """
        dependent_lib=''
        for dependencies in code_string.split("\n"):
            if "import" in dependencies:
                dependent_lib += "\n"+dependencies
        return dependent_lib

    def code_language(self):

        """
        This function need to be implemented to avoid input from user side
        :param inp_data:
        :return: code language like Scala, Python
        """
        pass


    def create_code(self,code='',filename='',subdir=''):
        """
        method used to write the parsed zeppelin's notebook content into their respective code files
        :param code: string
        :param filename: string
        :return: None
        """

        pwd = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(pwd, subdir, filename)

        if not os.path.exists(os.path.join(pwd, subdir)):
            os.mkdir(os.path.join(pwd, subdir))
        try:
            f = open(filepath, 'w')
            f.write(code)
            f.close()
        except IOError:
            logging.error("Wrong path provided")


    def execute_get_request(self):
        """
        main method used to parse the content of zeppelin notebook and perform extraction
        :return: None
        """

        inp_nb = open(self.nbrun.nb.user_notebook_path)

        for nb in inp_nb:
            l = nb.strip().split(",")
            for j in l:
                self.nbrun.is_notebook_exist(j)
                notebook_to_exexute = self.nb_data_request(j)
                r = requests.get(url=notebook_to_exexute)
                code_data = r.json()
                parsed_data=self.code_parser(code_data)
                parsed_dependencies=self.extract_dependencies(parsed_data)
                input_script_name= self.script_name(code_data)

                logging.info("genrating code directories")

                self.create_code(parsed_data,input_script_name,'extracted_code')
                self.create_code(parsed_dependencies,'import_statement.txt','dependencies_list')
