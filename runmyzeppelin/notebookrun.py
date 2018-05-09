import requests
import time
from runmyzeppelin.notebook import Notebook
from runmyzeppelin.exception import MyExceptionWithContext

class NbRun(object):

    def __init__(self):
        self.nb = Notebook()

    def get_notebook_id(self):
        """
        this method will return dict containing notebook ID as key and notebook name as value
        :return: dict
        """
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


    def is_notebook_exist(self, inpNB):
        """
        This method will check for the existence of user given notebook in zeppelin server
        :param inpNB: dict{notebookID,notebookName}
        :return: None
        """
        if inpNB in self.get_notebook_id().values():
            print("input notebook exist : "+ inpNB)
        else:
            raise MyExceptionWithContext()


    def get_post_request_url(self, nbName):
        """
        this method accept the notebook name and create the corresponding post request URL
        :param nbName: notebook name
        :return: string
        """
        self._nbID = ''
        self._nbName = ''
        for id,name in  self.get_notebook_id().items():
            if name == nbName:
                self._nbID = id
                self._nbName = nbName
        return self.nb.post_run_all_paragraphs() + self._nbID


    def get_custom_dag(self,notebook_running):
        """
        this method will return the set of all statuses like Running, Pending, Finished, Ready.
        :param notebook_running:
        :return: set
        """
        r = requests.get(url=notebook_running)
        data = r.json()
        p_status = data['body']
        paragraph_status = set()
        for item in p_status:
            current_status = item['status']
            paragraph_status.add(current_status)
        return paragraph_status


    def get_recursive_paragraph_call(self,notebook_running):
        """

        :param notebook_running:
        :return:
        """

        paragraph_status = self.get_custom_dag(notebook_running)
        if 'RUNNING' in paragraph_status:
            time.sleep(3)
            self.get_recursive_paragraph_call(notebook_running)
        elif 'PENDING' in paragraph_status:
            time.sleep(3)
            self.get_recursive_paragraph_call(notebook_running)
        elif 'FINISHED' in paragraph_status:
            print("All paragraph ran for " + )

    def execute_post_request(self):

        """
        iterate over the user given notebook list
        generate the post URL
        run the notebook using post method
        :return: None
        """
        inp_nb = open(self.nb.user_notebook_path)
        for nb in inp_nb:
            l = nb.strip().split(",")
            print(l)
            for j in l:
                self.is_notebook_exist(j)
                notebook_to_execute=self.get_post_request_url(j)
                print("**********NOTEBOOK RUN BEGINS**********")
                r = requests.post(url=notebook_to_execute)
                self.get_recursive_paragraph_call(notebook_to_execute)
                data = r.json()
                print(data)

