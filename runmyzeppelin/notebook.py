import requests

class Notebook(object):

    host = ''
    port = ''
    def __init__(self):
        try:
            f = open("/Users/aloktiwari/PycharmProjects/ZeppelinAutomationScript/zeppelin-server.properties" , "r")
            inpHostPort = []
            for line in f:
                inpHostPort.append(line)
            Notebook.host = inpHostPort[0].split("=")[1].strip()
            Notebook.port = inpHostPort[1].split("=")[1]
        except IOError:
            print("file not found")

    """
    Below are the get and post request function
    """

    def get_list_of_notes(self):
        return "http://%s:%s/api/notebook" % (Notebook.host, Notebook.port)

    def get_status_of_paragraphs(self):
        pass

    def get_notebook_data(self):
        return 'http://' + self.host + ":" + self.port + '/api/notebook/'

    def post_run_all_paragraphs(self):
        return 'http://' + self.host + ":" + self.port + '/api/notebook/job/'

    def post_paragraph_run_asynchronousely(self):
        pass



