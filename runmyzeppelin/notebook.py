import os
import configparser
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')

class Notebook(object):

    host = ''
    port = ''
    code_lang = ''
    user_notebook_path = ''

    def __init__(self):
        configuration=self.get_configuration_settings()
        self.host = configuration['hostname']
        self.port = configuration['port']
        self.code_lang = configuration['code.language']
        self.user_notebook_path = configuration['notebook.path']
        logging.info("notebook object created with host : " + self.host + ", port : " + self.port)


    def get_config_file_path(self):
        """
        method will return the path of properties file
        :return: String
        """
        pwd = os.path.dirname(os.path.realpath(__file__))
        logging.info("current working directory to find SERVER.PROPERTIES file : " + pwd)
        config_file=''
        try:
            for files in os.listdir(pwd):
                if files.endswith("properties"):
                    config_file += files
        except IOError:
            logging.ERROR("config file doesn't exist at current working directory" + pwd)
        return pwd+"/"+config_file


    def get_configuration_settings(self):
        """
        method will return every configuration given in properties file as a dictionary object
        :return: dict
        """
        config_file=self.get_config_file_path()
        config = configparser.RawConfigParser()
        config.read(config_file)
        details_dict = dict(config.items('SERVER'))
        return details_dict


    def get_list_of_notes(self):
        """
        GET method to list of all notebook present in zeppelin server
        :return: string of GET URL
        """
        return "http://%s:%s/api/notebook" % (self.host, self.port)


    def get_status_of_paragraphs(self):
        """
        GET method to know the status of all paragraph in zeppelin notebook
        :return:
        """
        return "http://%s:%s/api/notebook/job/" % (self.host, self.port)


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

