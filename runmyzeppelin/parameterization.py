import configparser
import os

class Parameter(object):


    def get_config_file_path(self):
        pwd = os.path.dirname(os.path.realpath(__file__))
        print("CURRENT WORKING DIRECTORY" + pwd)
        config_file=''
        try:
            for files in os.listdir(pwd):
                if files.endswith("properties"):
                    config_file += files
        except IOError:
            print("config file doesn't exist at current working directory" + pwd)
        return pwd+"/"+config_file


    def inp_parameter(self):
        config_file=self.get_config_file_path()
        config = configparser.RawConfigParser()
        config.read(config_file)
        details_dict = dict(config.items('SERVER'))
        # value_1 = details_dict['hostname']

        print(details_dict)

        return details_dict



z = Parameter()

z.inp_parameter()