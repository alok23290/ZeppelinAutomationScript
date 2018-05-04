import requests

class Notebook(object):

    host = ''
    port = ''
    code_lang = ''

    # IMPLEMENT ZEPPELIN SERVER PROPERTIES FILE AS DICTIONARY OBJECT

    def __init__(self):
        try:
            f = open("/Users/aloktiwari/PycharmProjects/ZeppelinAutomationScript/zeppelin-server.properties" , "r")
            inpHostPort = []
            for line in f:
                inpHostPort.append(line)
            Notebook.host = inpHostPort[0].split("=")[1].strip()
            Notebook.port = inpHostPort[1].split("=")[1].strip()
            Notebook.code_lang = inpHostPort[2].split("=")[1]

        except IOError:
            print("file not found")

    def get_list_of_notes(self):
        """
        GET method to list of all notebook present in zeppelin server
        :return: string of GET URL
        """
        return "http://%s:%s/api/notebook" % (Notebook.host, Notebook.port)

    def get_status_of_paragraphs(self):
        """
        GET method to know the status of all paragraph in zeppelin notebook
        :return:
        """
        pass

    def get_notebook_data(self):
        """
        GET method to fetch the notebook data
        :return:
        """
        return 'http://' + self.host + ":" + self.port + '/api/notebook/'

    def post_run_all_paragraphs(self):
        """
        POST method to run all paragraph synchronously
        :return:
        """
        return 'http://' + self.host + ":" + self.port + '/api/notebook/job/'

    def post_paragraph_run_asynchronously(self):
        """
        POST method to run all paragraph asynchronously
        :return:
        """
        pass



