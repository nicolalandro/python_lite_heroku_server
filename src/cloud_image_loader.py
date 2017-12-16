import json
import os
from pcloud import PyCloud


class CloudImageLoader(object):
    def __init__(self):
        self.pc = PyCloud('nicolaxx94@live.it', 'cloudperimmagini')

    def add_file(self, json_body):
        number = self._get_progressive_number()
        testfile = os.path.join(os.path.dirname(__file__), 'temp', str(number) + '.json')
        print(testfile)
        f = open(testfile, "w+")
        f.write(json_body)
        f.close()
        result = self.pc.uploadfile(files=[testfile])
        os.remove(testfile)
        return result

    def _get_progressive_number(self):
        try:
            json_list = str(self.pc.listfolder(folderid=0)).replace("'", '"')
            json_list = json_list.replace("False", '"False"').replace("True", '"True"')
            lis = json.loads(json_list)
            numer_str = lis['metadata']['contents'][-1]['name'].replace('.json', '')
            integer_progressive_number = int(numer_str) + 1
            print(integer_progressive_number)
            return integer_progressive_number
        except:
            return 0
