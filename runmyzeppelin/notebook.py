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

    def getNotebookID(self):
        testURL="http://%s:%s/api/notebook" % (Notebook.host,Notebook.port)
        r = requests.get(url=testURL)
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

        return subdict

